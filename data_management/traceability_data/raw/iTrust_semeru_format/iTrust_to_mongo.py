from pymongo import MongoClient
import os


def create_documents_from_iTrust(ground_truth_file, use_dir, source_dir, db):
    # pair requirements with source_code files
    use_to_source = create_requirement_to_source_or_test_dicts(ground_truth_file, " ")
    use_to_source = clean_iTrust_paths(use_to_source, source_dir)

    use_collection = db["requirement_raw"]
    source_collection = db["source_raw"]

    for use in use_to_source.keys():

        use_path = os.path.join(".", use_dir, use)

        with open(use_path, encoding="ISO-8859-1") as use_file:
            use_contents = use_file.read()

        use_document = {"name": use, "system": "iTrust", "applied_transformations": [],
                        "ground_truth": [], "contents": use_contents}

        use_id = use_collection.insert_one(use_document).inserted_id
        use_query = {"_id": use_id}

        create_and_link_source_documents(use, use_to_source, source_dir, source_collection, use_id,
                                         use_collection, use_query)


def create_and_link_source_documents(requirement, requirements_to_source, source_dir, source_collection,
                                     req_id, req_collection, req_query):

    try:
        for source in requirements_to_source[requirement]:

            exists = source_collection.find_one({"name": source})

            if exists is None:

                source_path = os.path.join(".", source_dir, source)

                with open(source_path, encoding="ISO-8859-1") as source_file:
                    source_contents = source_file.read()

                source_document = {"name": source, "system": "iTrust", "applied_transformations": [],
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


def clean_iTrust_paths(use_to_source, source_dir):

    for use_case in use_to_source.keys():
        for i in range(len(use_to_source[use_case])):
            split_path = use_to_source[use_case][i].split(".")
            path = ""

            for j in range(0, len(split_path)-2):
                path = os.path.join(path, split_path[j])

            file_name = split_path[-2] + "." + split_path[-1]
            path = os.path.join(path, file_name)

            use_to_source[use_case][i] = path

    return use_to_source


def main():
    client = MongoClient('localhost', 27017)
    db = client.test
    create_documents_from_iTrust('ground.txt', 'use_cases', 'source_code', db)


if __name__ == "__main__":
    main()




