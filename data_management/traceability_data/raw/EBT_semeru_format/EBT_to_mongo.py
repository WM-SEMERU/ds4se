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


def create_requirement_to_source_or_test_dicts(ground_file, split_on):

    requirement_associations = dict()

    # pair requirements with source_code or test files
    with open(ground_file) as f:
        for line in f:
            line = line.rstrip()
            files = line.split(split_on)

            requirement_associations[files[0]] = files[1:]

    print(requirement_associations)
    return requirement_associations


def parse_requirement_or_test_file(file, split_on):

    req_or_test = dict()

    # read in the lines and split
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            req_or_test_id = line.split(split_on)[0]
            req_or_test[req_or_test_id] = line

    print(req_or_test)
    return req_or_test


def main():
    client = MongoClient('localhost', 27017)
    db = client.test
    create_documents_from_EBT('code_ground.txt', 'tests_ground.txt', 'requirements.txt', 'test_cases.txt',
                              'source_code', db)


if __name__ == "__main__":
    main()

