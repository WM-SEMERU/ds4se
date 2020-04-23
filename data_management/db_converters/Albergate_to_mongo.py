from pymongo import MongoClient
import os
from ds4se.mgmnt.db.mongo import SemeruCollection


def create_documents_from_albergate(ground_truth_file, req_dir, source_dir, db):

    req_to_source = create_requirement_to_source_or_test_dicts(ground_truth_file, " ")

    use_collection = db["requirement_raw"]
    source_collection = db["source_raw"]

    for requirement in req_to_source.keys():
        use_path = os.path.join("", req_dir, requirement)

        with open(use_path, encoding="ISO-8859-1") as req_file:
            req_contents = req_file.read()

        req_document = {"name": requirement, "system": "Albergate", "applied_transformations": [],
                        "ground_truth": [], "contents": req_contents}

        req_id = use_collection.insert_one(req_document).inserted_id
        req_query = {"_id": req_id}

        create_and_link_source_documents(requirement, req_to_source, source_dir, source_collection, req_id,
                                         use_collection, req_query)


def create_and_link_source_documents(requirement, requirements_to_source, source_dir, source_collection,
                                     req_id, req_collection, req_query):

    try:
        for source in requirements_to_source[requirement]:

            exists = source_collection.find_one({"name": source})

            if exists is None:

                source_path = os.path.join("", source_dir, source)

                with open(source_path, encoding="ISO-8859-1") as source_file:
                    source_contents = source_file.read()

                source_document = {"name": source, "system": "Albergate", "applied_transformations": [],
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


def main():

    client = MongoClient('localhost', 27017)
    db = client.test
    create_documents_from_albergate('../traceability_data/raw/Albergate_semeru_format/ground.txt', 'requirements', 'source_code', db)


if __name__ == "__main__":
    main()




