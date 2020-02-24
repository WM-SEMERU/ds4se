from pymongo import MongoClient
from pymongo.collection import Collection
from jsonschema import validate
from jsonschema import exceptions as json_exceptions
from json import loads


class SemeruCollection(Collection):

    def __init__(self, database, name, raw_schema, transform_schema, create=False, codec_options=None,
                 read_preference=None, write_concern=None, read_concern=None, session=None, **kwargs):

        super(SemeruCollection, self).__init__(database, name, create, codec_options, read_preference,
                                               write_concern, read_concern, session, **kwargs)

        with open(raw_schema) as raw:
            self.raw_schema = loads(raw.read())

        with open(transform_schema) as transform:
            self.transform_schema = loads(transform.read())

    def insert_one(self, document, bypass_document_validation=False,
                   session=None):

        # validate the document
        document_type = self.__validate_document(document)

        # if the document is raw, then insert it into the database
        # NOTE:
        if document_type == "raw":
            self.insert_raw_document(document, bypass_document_validation, session)
        else:
            self.insert_transform_document(document)

    def __insert_raw_document(self, document, bypass_document_validation=False, session=None):

        db = self.database
        associated_files = document["ground_truth"]

        for file in associated_files:

            # Check
            if "document_id" in file.keys:
                if db[file["collection"]].find({"_id": file["document_id"]}) is None:
                    raise Warning("Document references file with document id \'{}\', which cannot be found in "
                                  "collection \'{}\'".format(file["document_id"],
                                                             file["collection"]))
            elif "name_and_system" in file.keys:
                if db[file["collection"]].find({"name": file["name_and_system"][0],
                                                "system": file["name_and_system"][1]}) is None:
                    raise Warning("Document references file with system \'{}\' and name \'{}\', which cannot be found "
                                  "in collection \'{}\'".format(file["name_and_system"][1],
                                                                file["name_and_system"][0],
                                                                file["collection"]))

        super().insert_one(document, bypass_document_validation, session)

    def __insert_transform_document(self, document):
        pass

    def __validate_document(self, document):
        # try to validate against raw schema
        try:
            validate(document, self.raw_schema)

            # if it passes, set type to raw and validate the collection name, so that it is of style XXXX_raw
            document_type = "raw"
            if self.full_name.split("_")[-1] != "raw":
                raise TypeError("Document validates against raw_schema, but current collection is not a raw collection")

        except json_exceptions.ValidationError as raw_error:

            # if it fails, try to validate against transform schema
            try:
                validate(document, self.transform_schema)

                # if it passes, set type to transform and validate the collection name, so that is is of
                # style XXX_transform
                document_type = "transform"
                if self.full_name.split("_")[-1] != "transform":
                    raise TypeError("Document validates against transform_schema, but current collection is not a "
                                    "transform collection")

            except json_exceptions.ValidationError as transform_error:

                # if it fails, throw an unrecognized type error, and say it couldn't be validated against either schema.
                raise TypeError("Document does not validate against raw or transform schema. ",
                                raw_error, transform_error)
        return document_type

    def delete_one(self, filter, collation=None, session=None):

        # a delete can only be run if the document is a child node.
        pass

    def run_transformation(self, query, function):

        # Takes a function, and runs the transformation on each document which matches the query, then constructs
        # and stores new transformed versions of the document
        pass




client = MongoClient('localhost', 27017)
db = client.test
test = SemeruCollection(database=db, name="source_raw", raw_schema="./traceability_data/raw_schema.json",
                        transform_schema="./traceability_data/transformed_schema.json")

sample = {'name': 'UC58.TXT', 'system': 'eTour', 'applied_transformations': [], 'ground_truth': [{"collection": "Collection_name", "name_and_system": ["eTour", "ground.txt"]}],
          'contents': 'Use case name VISUALIZZASCHEDASITO \nView the details of a particular site. \nPartecipating '
                      '\nActor initialized by Tourist \nEntry \nconditions \x95 The Tourist has successfully '
                      'authenticated to the system and is located in one of the following areas: Research Results, '
                      'List of Sites Visited Sites and List of Favorites \nFlow of events User System \n1. Select the '
                      'function for displaying the card on a site chosen. \n2 Upload data from the database. \nExit '
                      'conditions \x95 The system displays the details of the selected site. \n\x95 Interruption of '
                      'the connection to the server ETOUR. \nQuality \nrequirements'}

sample = {"blah": "cool"}

test.insert_one(sample)
