from pymongo import MongoClient
from pymongo.collection import Collection
from jsonschema import validate
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

        # try to validate against raw schema
        try:
            validate(document, raw_schema)
        except Exception as raw_error:
            pass
        # if it passes, set type to raw and validate the collection name, so that it is of style XXXX_raw
        # if it fails, try to validate against transform schema
        # if it passes, set type to transform and validate the collection name, so that is is of style XXX_transform
        # if it fails, throw an unrecognized type error, and say it couldn't be validated against either schema. Print
        # links to the schema
        #
        pass

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
print(test.full_name)


with open("./traceability_data/raw_schema.json") as f:
    raw_schema = f.read()
    raw_schema = loads(raw_schema)

sample = {'name': 'UC58.TXT', 'system': 'eTour', 'applied_transformations': [], 'ground_truth': [{"collection": "Collection_name", "name_and_system": ["eTour", "ground.txt"]}],
          'contents': 'Use case name VISUALIZZASCHEDASITO \nView the details of a particular site. \nPartecipating '
                      '\nActor initialized by Tourist \nEntry \nconditions \x95 The Tourist has successfully '
                      'authenticated to the system and is located in one of the following areas: Research Results, '
                      'List of Sites Visited Sites and List of Favorites \nFlow of events User System \n1. Select the '
                      'function for displaying the card on a site chosen. \n2 Upload data from the database. \nExit '
                      'conditions \x95 The system displays the details of the selected site. \n\x95 Interruption of '
                      'the connection to the server ETOUR. \nQuality \nrequirements'}

print(validate(sample, raw_schema))
