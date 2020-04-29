from pymongo import MongoClient
import os
import glob
from ds4se.mgmnt.db.mongo import SemeruCollection


def create_documents_from_EBT(code_ground, tests_ground, test_to_code_ground, req_dir, test_dir, source_dir,
                                 req_collection, test_collection, source_collection):

    # pair requirements with source_code files
    requirements_to_source = create_requirement_to_source_or_test_dicts(code_ground, " ")

    # pair requirements with test files
    requirements_to_test = create_requirement_to_source_or_test_dicts(tests_ground, " ")

    # pair tests with source_code files
    test_to_source = create_requirement_to_source_or_test_dicts(test_to_code_ground, " ")

    # Insert all the requirements
    req_to_id = insert_from_file(dict(), 'data/traceability/semeru-format/EBT_semeru_format/requirements.txt', "\t",
                                 req_collection, "EBT")

    # Insert all of the source
    source_to_id = insert_raw(dict(), source_dir, source_collection, "*.java", "EBT")

    # Insert all of the tests
    test_to_id = insert_from_file(dict(), 'data/traceability/semeru-format/EBT_semeru_format/test_cases.txt', " ",
                                 test_collection, "EBT")

    link_docs(requirements_to_source, req_to_id, req_collection, source_to_id, source_collection)
    link_docs(requirements_to_test, req_to_id, req_collection, test_to_id, test_collection)
    link_docs(test_to_source, test_to_id, test_collection, source_to_id, source_collection)


def link_docs(ground_dict, key_ids, key_collection, value_ids, value_collection):

    for key in ground_dict.keys():

        key_id = key_ids[key]

        for value in ground_dict[key]:

            if value != '':

                value_id = value_ids[value]

                key_collection.link_ground_truth(key_id, key_collection, value_id, value_collection)


def insert_raw(doc_id_dict, dir, collection, ext, system):

    files = []
    for file in glob.glob(os.path.join(dir, ext)):
        files.append(file)

    # print(files)

    for file in files:

        with open(file, encoding="ISO-8859-1") as open_file:
            contents = open_file.read()

        file_name = os.path.split(file)[1]

        req_document = {"name": file_name, "system": system, "applied_transformations": [],
                        "ground_truth": [], "contents": contents}

        id = collection.insert_one(req_document).inserted_id
        doc_id_dict[file_name] = id

    return doc_id_dict


def insert_from_file(doc_id_dict, file, split_on,  collection, system):

    # read in the lines and split
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            req_or_test_id = line.split(split_on)[0]
            contents = line.split(split_on, 1)[1]

            document = {"name": req_or_test_id, "system": system, "applied_transformations": [],
                            "ground_truth": [], "contents": contents}

            id = collection.insert_one(document).inserted_id
            doc_id_dict[req_or_test_id] = id

    # print(req_or_test)
    return doc_id_dict


def create_requirement_to_source_or_test_dicts(ground_file, split_on):

    requirement_associations = dict()

    # pair requirements with source_code or test files
    with open(ground_file) as f:
        for line in f:
            line = line.rstrip()
            files = line.split(split_on)

            requirement_associations[files[0]] = files[1:]

    return requirement_associations


def main():
    client = MongoClient('localhost', 27017)
    db = client.traceability
    req_collection = SemeruCollection(database=db, name="requirement_raw", raw_schema="nbs/DB_Schema/raw_schema.json",
                        transform_schema="nbs/DB_Schema/transformed_schema.json")
    test_collection = SemeruCollection(database=db, name="test_raw", raw_schema="nbs/DB_Schema/raw_schema.json",
                        transform_schema="nbs/DB_Schema/transformed_schema.json")
    source_collection = SemeruCollection(database=db, name="source_raw", raw_schema="nbs/DB_Schema/raw_schema.json",
                        transform_schema="nbs/DB_Schema/transformed_schema.json")


    create_documents_from_EBT('data/traceability/semeru-format/EBT_semeru_format/code_ground.txt',
                                 'data/traceability/semeru-format/EBT_semeru_format/tests_ground.txt',
                                 'data/traceability/semeru-format/EBT_semeru_format/test_to_source.txt',
                                 'data/traceability/semeru-format/EBT_semeru_format/requirements.txt',
                                 'data/traceability/semeru-format/EBT_semeru_format/test_cases.txt',
                                 'data/traceability/semeru-format/EBT_semeru_format/source_code',
                                 req_collection,
                                 test_collection,
                                 source_collection)


if __name__ == "__main__":
    main()



