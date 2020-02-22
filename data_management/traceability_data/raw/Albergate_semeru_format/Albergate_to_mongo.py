from pymongo import MongoClient
import os


def create_documents_from_albergate(ground_truth_file, req_dir, source_dir, db):

    pairs = dict()

    with open(ground_truth_file) as f:
        for line in f:
            line = line.rstrip()
            line_pair = line.split(" ")

            if line_pair[0] in pairs.keys():
                pairs[line_pair[0]].append(line_pair[1])
            else:
                pairs[line_pair[0]] = list()
                pairs[line_pair[0]].append(line_pair[1])

    for requirement in pairs.keys():

        req_path = os.path.join(".", req_dir, requirement)
        req_collection = db["requirement_raw"]

        with open(req_path, encoding= "ISO-8859-1") as req_file:
            requirement_contents = req_file.read()

        req_document = {"name": requirement, "system": "Albergate", "applied_transformations": [],
                        "ground_truth": [], "contents": requirement_contents}

        req_id = req_collection.insert_one(req_document).inserted_id
        
        for source in pairs[requirement]:

            source_path = os.path.join(".", source_dir, source)

            with open(source_path, encoding="ISO-8859-1") as source_file:
                source_collection = db["source_raw"]
                source_contents = source_file.read()
            source_document = {"name": source, "system": "Albergate", "applied_transformations": [],
                               "ground_truth": [], "contents": source_contents}

            source_id = source_collection.insert_one(source_document).inserted_id

            req_query = {"_id": req_id}
            new_req_values = {"$addToSet": {"ground_truth": ("source_raw", source_id)}}

            source_query = {"_id": source_id}
            new_source_values = {"$addToSet": {"ground_truth": ("requirement_raw", req_id)}}

            req_collection.update_one(req_query, new_req_values)
            source_collection.update_one(source_query, new_source_values)


def main():

    client = MongoClient('localhost', 27017)
    db = client.test
    create_documents_from_albergate('ground.txt', 'requirements', 'source_code', db)


if __name__ == "__main__":
    main()




