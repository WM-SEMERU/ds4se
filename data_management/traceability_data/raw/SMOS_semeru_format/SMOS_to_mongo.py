from pymongo import MongoClient
import os
import glob
from data_management.Semeru_Collection import SemeruCollection


def create_documents_from_SMOS(ground, source_dir, use_dir, source_collection, use_collection):

    # pair requirements with source_code files
    requirements_to_source = create_requirement_to_source_or_test_dicts(ground, " ")

    # Insert all the requirements
    req_to_id = insert_raw(dict(), use_dir, use_collection, "*.txt", "SMOS")

    # Insert all of the source
    source_to_id = insert_raw(dict(), source_dir, source_collection, "*.java", "SMOS")

    link_docs(requirements_to_source, req_to_id, use_collection, source_to_id, source_collection)


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
    db = client.test
    use_collection = SemeruCollection(database=db, name="requirement_raw", raw_schema="/Users/megretson/Projects/SE/ds4se/data_management/traceability_data/raw_schema.json",
                        transform_schema="/Users/megretson/Projects/SE/ds4se/data_management/traceability_data/transformed_schema.json")
    source_collection = SemeruCollection(database=db, name="source_raw", raw_schema="/Users/megretson/Projects/SE/ds4se/data_management/traceability_data/raw_schema.json",
                        transform_schema="/Users/megretson/Projects/SE/ds4se/data_management/traceability_data/transformed_schema.json")

    create_documents_from_SMOS("ground.txt", "source_code", "use_cases", source_collection, use_collection)


if __name__ == "__main__":
    main()

