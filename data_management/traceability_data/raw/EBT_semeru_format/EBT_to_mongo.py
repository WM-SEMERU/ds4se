from pymongo import MongoClient
import os


def create_documents_from_EBT(code_ground, tests_ground, req_file, test_file, source_dir, db):

    # pair requirements with source_code files
    requirements_to_source = create_requirement_to_source_or_test_dicts(code_ground, " ")

    # pair requirements with source_code files
    requirements_to_test = create_requirement_to_source_or_test_dicts(tests_ground, " ")

    # Read in the requirement file
    requirements = parse_requirement_or_test_file(req_file, "\t")

    # Read in the test file
    tests = parse_requirement_or_test_file(test_file, " ")

    req_collection = db["requirement_raw"]
    source_collection = db["source_raw"]
    test_collection = db["test_raw"]

    for requirement in requirements.keys():

        req_document = {"name": requirement, "system": "EBT", "applied_transformations": [],
                        "ground_truth": [], "contents": requirements[requirement]}

        req_id = req_collection.insert_one(req_document).inserted_id
        req_query = {"_id": req_id}

        create_and_link_source_documents(requirement, requirements_to_source, source_dir, source_collection, req_id,
                                         req_collection, req_query)

        create_and_link_test_documents(requirement, requirements_to_test, test_collection, tests, req_id,
                                       req_collection, req_query)

        link_source_and_tests(req_query, req_collection, source_collection, test_collection)


def link_source_and_tests(req_query, req_collection, source_collection, test_collection):

    req_document = req_collection.find_one(req_query)
    source_ids = list()
    test_ids = list()

    for file in req_document["ground_truth"]:
        if file[0] == "source_raw":
            source_ids.append(file[1])
        elif file[0] == "test_raw":
            test_ids.append(file[1])
        else:
            print("Unrecognizable artifact type")
            raise KeyError

    for source_id in source_ids:

        source_query = {"_id": source_id}

        for test_id in test_ids:
            test_query = {"_id": test_id}

            new_source_values = {"$addToSet": {"ground_truth": ("test_raw", test_id)}}
            new_test_values = {"$addToSet": {"ground_truth": ("source_raw", source_id)}}

            source_collection.update_one(source_query, new_source_values)
            test_collection.update_one(test_query, new_test_values)


def create_and_link_source_documents(requirement, requirements_to_source, source_dir, source_collection,
                                     req_id, req_collection, req_query):

    try:
        for source in requirements_to_source[requirement]:

            exists = source_collection.find_one({"name": source})

            if exists is None:

                source_path = os.path.join(".", source_dir, source)

                with open(source_path, encoding="ISO-8859-1") as source_file:
                    source_contents = source_file.read()

                source_document = {"name": source, "system": "EBT", "applied_transformations": [],
                                   "ground_truth": [], "contents": source_contents}

                # Check if a source_document of this name already exists
                source_id = source_collection.insert_one(source_document).inserted_id

            else:
                source_id = exists["_id"]

            new_req_values = {"$addToSet": {"ground_truth": ("source_raw", source_id)}}

            source_query = {"_id": source_id}
            new_source_values = {"$addToSet": {"ground_truth": ("requirement_raw", req_id)}}

            req_collection.update_one(req_query, new_req_values)
            source_collection.update_one(source_query, new_source_values)

    except KeyError:
        # print("There is no corresponding source for this requirement")
        pass


def create_and_link_test_documents(requirement, requirements_to_test, test_collection, tests, req_id,
                                   req_collection, req_query):

    try:
        for test in requirements_to_test[requirement]:

            exists = test_collection.find_one({"name": test})

            if exists is None:

                test_contents = tests[test]
                test_document = {"name": test, "system": "EBT", "applied_transformations": [], "ground_truth": [],
                                 "contents": test_contents}

                test_id = test_collection.insert_one(test_document).inserted_id

            else:
                test_id = exists["_id"]

            new_req_values = {"$addToSet": {"ground_truth": ("test_raw", test_id)}}

            test_query = {"_id": test_id}
            new_test_values = {"$addToSet": {"ground_truth": ("requirement_raw", req_id)}}

            req_collection.update_one(req_query, new_req_values)
            test_collection.update_one(test_query, new_test_values)

    except KeyError:
        # print("There is no corresponding test for this requirement")
        pass


def create_requirement_to_source_or_test_dicts(ground_file, split_on):

    requirement_associations = dict()

    # pair requirements with source_code or test files
    with open(ground_file) as f:
        for line in f:
            line = line.rstrip()
            files = line.split(split_on)

            requirement_associations[files[0]] = files[1:]

    # print(requirement_associations)
    return requirement_associations


def parse_requirement_or_test_file(file, split_on):

    req_or_test = dict()

    # read in the lines and split
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            req_or_test_id = line.split(split_on)[0]
            req_or_test[req_or_test_id] = line

    # print(req_or_test)
    return req_or_test


def main():
    client = MongoClient('localhost', 27017)
    db = client.test
    create_documents_from_EBT('code_ground.txt', 'tests_ground.txt', 'requirements.txt', 'test_cases.txt',
                              'source_code', db)


if __name__ == "__main__":
    main()

