from pymongo import MongoClient
from pymongo.collection import Collection
from jsonschema import validate
from jsonschema import exceptions as json_exceptions
from json import loads
import warnings


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
            return self.__insert_raw_document(document, bypass_document_validation, session)
        else:
            return self.__insert_transform_document(document, bypass_document_validation, session)

    def __insert_raw_document(self, document, bypass_document_validation=False, session=None):

        db = self.database
        associated_files = document["ground_truth"]

        for file in associated_files:
            print(file)

            with warnings.catch_warnings():

                # Turn on warnings for this section of code, regardless of user preferences
                warnings.simplefilter('always')

                # Default to using a document_id.
                if "document_id" in file.keys():
                    if db[file["collection"]].find_one({"_id": file["document_id"]}) is None:
                        raise Warning("Document references file with document id \'{}\', which cannot be found in "
                                      "collection \'{}\'. \n Please add related document to collection \'{}\'".format(
                                        file["document_id"],
                                        file["collection"],
                                        file["collection"]))

                # But use the name/system pair if necessary
                elif "name_and_system" in file.keys():
                    if db[file["collection"]].find_one({"name": file["name_and_system"][0],
                                                        "system": file["name_and_system"][1]}) is None:
                        raise Warning(
                            "Document references file with system \'{}\' and name \'{}\', which cannot be found "
                            "in collection \'{}\'. \n Please add related document to collection \'{}\'".format(
                                file["name_and_system"][1],
                                file["name_and_system"][0],
                                file["collection"],
                                file["collection"]))

        raw_id = super().insert_one(document, bypass_document_validation, session)
        return raw_id

    def __insert_transform_document(self, document, bypass_document_validation, session):

        db = self.database

        # The document needs to have a valid transformation history to be inserted
        if document["transformed_from"].len() == 0:
            raise Exception("Transformation Document has no \"transformed_from\" field.")

        # The transformed_from fields must map to valid documents in the database
        for transformed_from in document["transformed_from"]:
            transformed_from_collection = db[transformed_from["collection"]]
            if transformed_from_collection.find_one({"_id": transformed_from["document_id"]}) is None:
                raise Exception("Cannot locate document with id {} in collection \'{}\'".format(
                    transformed_from["document_id"], transformed_from_collection))

        transformation_identifier = document["transformation_identifier"]
        transform_id = super().insert_one(document, bypass_document_validation, session)

        # Add the new transformed document to the applied transformation fields of the transformed_from documents
        for transformed_from in document["transformed_from"]:
            transformed_from_collection = db[transformed_from["collection"]]

            update_applied_transform = {"$addToSet": {"applied_transformations": {
                "collection": self.full_name,
                "document_id": transform_id,
                "transformation_identifier": transformation_identifier}}}

            transformed_from_collection.update_one({"_id": transformed_from["document_id"]}, update_applied_transform)

        return transform_id

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

    def run_transformation(self, query, function, transformation_collection_name):

        import datetime
        transformation_identifier = {"function_name": function.__name__, "timestamp": datetime.datetime.now()}

        # Takes a function, and runs the transformation on each document which matches the query
        for document in self.find(query):
            transformed_text = function(document["contents"])

            # construct and stores new transformed version of the document with transformed from field
            transform_document = {"name": document["name"],
                                  "system": document["system"],
                                  "applied_transformations": [],
                                  "contents": transformed_text,
                                  "transformation_identifier": transformation_identifier,
                                  "transformed_from": [{"collection": self.full_name,
                                                        "document_id": document["_id"]}]
                                  }

            # update the document with the applied transformation
            db = self.database
            transformation_collection = db[transformation_collection_name]
            transform_doc_id = transformation_collection.insert_one(transform_document)

            update_applied_transform = {"$addToSet": {"applied_transformations": {
                "collection": transformation_collection_name,
                "document_id": transform_doc_id,
                "transformation_identifier": transformation_identifier}}}

            self.update_one({"_id": document["_id"]}, update_applied_transform)

            # transformation_identifier [(date, function_string)]
            # applied transformation [(collection, document_id, transformation_identifier), ... ]
            # transformed from [(collection, document_id), ... ]


client = MongoClient('localhost', 27017)
db = client.test
test = SemeruCollection(database=db, name="source_raw", raw_schema="./traceability_data/raw_schema.json",
                        transform_schema="./traceability_data/transformed_schema.json")

sample = {'name': 'UC58.TXT', 'system': 'test_system', 'applied_transformations': [], 'ground_truth': [{"collection":
                                                                                                      "Collection_name",
                                                                                                  "name_and_system":
                                                                                                      ["eTour",
                                                                                                       "ground.txt"]
                                                                                                  }],
          'contents': 'Use case name VISUALIZZASCHEDASITO \nView the details of a particular site. \nPartecipating '
                      '\nActor initialized by Tourist \nEntry \nconditions \x95 The Tourist has successfully '
                      'authenticated to the system and is located in one of the following areas: Research Results, '
                      'List of Sites Visited Sites and List of Favorites \nFlow of events User System \n1. Select the '
                      'function for displaying the card on a site chosen. \n2 Upload data from the database. \nExit '
                      'conditions \x95 The system displays the details of the selected site. \n\x95 Interruption of '
                      'the connection to the server ETOUR. \nQuality \nrequirements'}

test.insert_one(sample)
