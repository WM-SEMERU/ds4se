from pymongo import MongoClient
import os
from ds4se.mgmnt.db.mongo import SemeruCollection


def create_documents_from_eTour(ground_truth_file, source_dir, use_dir, source_collection, use_collection):
    # pair requirements with source_code files
    use_to_source = create_requirement_to_source_or_test_dicts(ground_truth_file, " ")

    for use in use_to_source.keys():

        use_path = os.path.join(use_dir, use)

        with open(use_path, encoding="ISO-8859-1") as use_file:
            use_contents = use_file.read()

        use_document = {"name": use, "system": "eTour", "applied_transformations": [],
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

                source_path = os.path.join(source_dir, source)

                with open(source_path, encoding="ISO-8859-1") as source_file:
                    source_contents = source_file.read()

                source_document = {"name": source, "system": "eTour", "applied_transformations": [],
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
    db = client.traceability

    source_collection = SemeruCollection(database=db, name="source_raw", raw_schema="nbs/DB_Schema/raw_schema.json",
                        transform_schema="nbs/DB_Schema/transformed_schema.json")
    use_collection = SemeruCollection(database=db, name="requirement_raw", raw_schema="nbs/DB_Schema/raw_schema.json",
                        transform_schema="nbs/DB_Schema/transformed_schema.json")

    create_documents_from_eTour('data/traceability/semeru-format/eTOUR_semeru_format/ground.txt',
                                 'data/traceability/semeru-format/eTOUR_semeru_format/source_code',
                                 'data/traceability/semeru-format/eTOUR_semeru_format/use_cases',
                                 source_collection, use_collection)


if __name__ == "__main__":
    main()









