from pymongo import MongoClient
import os
from ds4se.mgmnt.db.mongo import SemeruCollection


def create_documents_from_eTour(ground_truth_file, req_dir, source_dir, db):

    requirements_to_source = create_requirement_to_source_or_test_dicts(ground_truth_file, " ")
    req_collection = db["requirement_raw"]
    source_collection = db["source_raw"]

    for requirement in requirements_to_source.keys():

        req_path = os.path.join("../traceability_data/raw/eTOUR_semeru_format", req_dir, requirement)

        with open(req_path, encoding="ISO-8859-1") as req_file:
            requirement_contents = req_file.read()

        req_document = {"name": requirement, "system": "eTour", "applied_transformations": [],
                        "ground_truth": [], "contents": requirement_contents}

        print(req_document)

        req_id = req_collection.insert_one(req_document).inserted_id

        for source in requirements_to_source[requirement]:
            source_path = os.path.join("../traceability_data/raw/eTOUR_semeru_format", source_dir, source)

            with open(source_path, encoding="ISO-8859-1") as source_file:
                source_contents = source_file.read()
            source_document = {"name": source, "system": "eTour", "applied_transformations": [],
                               "ground_truth": [], "contents": source_contents}

            source_id = source_collection.insert_one(source_document).inserted_id

            req_query = {"_id": req_id}
            new_req_values = {"$addToSet": {"ground_truth": ("source_raw", source_id)}}

            source_query = {"_id": source_id}
            new_source_values = {"$addToSet": {"ground_truth": ("requirement_raw", req_id)}}

            req_collection.update_one(req_query, new_req_values)
            source_collection.update_one(source_query, new_source_values)


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
    create_documents_from_eTour('../traceability_data/raw/eTOUR_semeru_format/ground.txt', 'use_cases', 'source_code', db)


if __name__ == "__main__":
    main()




