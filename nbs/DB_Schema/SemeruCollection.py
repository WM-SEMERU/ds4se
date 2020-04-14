from pymongo import MongoClient
from pymongo.collection import Collection
from jsonschema import validate
from jsonschema import exceptions as json_exceptions
from json import loads
import warnings


class SemeruCollection(Collection):
    """
    Get / create a Mongo collection, with overriden insertion and deletion rules.

    Overriden from PyMongo class object: documentation can be found here
    https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection


    :Attributes:
        - `full_name`: The full name of this :class:`Collection`. The full name is of the form
        `database_name.collection_name`.
        - `name`: The name of this :class:`Collection`.
        - `database`: The :class:`~pymongo.database.Database` that this :class:`Collection` is a part of.
        - `raw_schema`: The json schema for raw documents inserted into this collection, stored as dict
        - `transform_schema`: The json schema for transformed documents inserted into this collection, stored as dict

    """

    def __init__(self, database, name, raw_schema, transform_schema, create=False, codec_options=None,
                 read_preference=None, write_concern=None, read_concern=None, session=None, **kwargs):
        """
        Get / create a Semeru Mongo collection
        ...

        :Args:
          - `database`: the database to get a collection from
          - `name`: the name of the collection to get
          - `raw_schema`: the path to a json schema for raw documents
          - `transform_schema`: the path to a json schema for transformed documents
          - `create` (optional): if ``True``, force collection
            creation even without options being set
          - `codec_options` (optional): An instance of
            :class:`~bson.codec_options.CodecOptions`. If ``None`` (the
            default) database.codec_options is used.
          - `read_preference` (optional): The read preference to use. If
            ``None`` (the default) database.read_preference is used.
          - `write_concern` (optional): An instance of
            :class:`~pymongo.write_concern.WriteConcern`. If ``None`` (the
            default) database.write_concern is used.
          - `read_concern` (optional): An instance of
            :class:`~pymongo.read_concern.ReadConcern`. If ``None`` (the
            default) database.read_concern is used.
          - `collation` (optional): An instance of
            :class:`~pymongo.collation.Collation`. If a collation is provided,
            it will be passed to the create collection command. This option is
            only supported on MongoDB 3.4 and above.
          - `session` (optional): a
            :class:`~pymongo.client_session.ClientSession` that is used with
            the create collection command
          - `**kwargs` (optional): additional keyword arguments will
            be passed as options for the create collection command
        """

        super(SemeruCollection, self).__init__(database, name, create, codec_options, read_preference,
                                               write_concern, read_concern, session, **kwargs)

        with open(raw_schema) as raw:
            self.raw_schema = loads(raw.read())

        with open(transform_schema) as transform:
            self.transform_schema = loads(transform.read())

    def insert_one(self, document, bypass_document_validation=False,
                   session=None):
        """Insert a single document, enforcing schema rules.

        :Parameters:
          - `document`: The document to insert. Must be a Python Dict. If the document does
          not have an _id field one will be added automatically.
          - `bypass_document_validation`: (optional) If ``True``, allows the
            write to opt-out of document level validation. Default is
            ``False``. All SemeruCollection documents are validated regardless of this param.
          - `session` (optional): a
            :class:`~pymongo.client_session.ClientSession`.


        :Returns:
          The result document.
        """

        # validate the document
        document_type = self.__validate_document(document)

        # if the document is raw, then insert it into the database
        if document_type == "raw":
            return self.__insert_raw_document(document, bypass_document_validation, session)
        else:
            return self.__insert_transform_document(document, bypass_document_validation, session)

    def __insert_raw_document(self, document, bypass_document_validation=False, session=None):
        """ Internal insertion helper for raw documents

        This method turns on warnings regardless of user preferences, and raises a warning if a document is inserted
        which references documents (either by ID or system/name pair) that are not found in the database.

        :Parameters:
          - `document`: The document to insert. Must be a mutable mapping
            type. If the document does not have an _id field one will be
            added automatically.
          - `bypass_document_validation`: (optional) If ``True``, allows the
            write to opt-out of document level validation. Default is
            ``False``. All SemeruCollection documents are validated regardless of this param.
          - `session` (optional): a
            :class:`~pymongo.client_session.ClientSession`.

        :Returns:
          The result document.
        """

        db = self.database
        associated_files = document["ground_truth"]

        for file in associated_files:
            print(file)

            with warnings.catch_warnings():

                # Turn on warnings for this section of code, regardless of user preferences
                warnings.simplefilter('always')

                # Default to using a document_id, check if referenced document can be found
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

        raw_doc = super().insert_one(document, bypass_document_validation, session)
        return raw_doc

    def __insert_transform_document(self, document, bypass_document_validation, session):
        """ Internal insertion helper for transform documents

        This method raises an error if the document this document is transformed from cannot be found.

        :Parameters:
          - `document`: The document to insert. Must be a mutable mapping
            type. If the document does not have an _id field one will be
            added automatically.
          - `bypass_document_validation`: (optional) If ``True``, allows the
            write to opt-out of document level validation. Default is
            ``False``. All SemeruCollection documents are validated regardless of this param.
          - `session` (optional): a
            :class:`~pymongo.client_session.ClientSession`.

        :Returns:
          The result document.
        """

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
        transform_doc = super().insert_one(document, bypass_document_validation, session)
        transform_id = transform_doc.inserted_id

        # Add the new transformed document to the applied transformation fields of the transformed_from documents
        for transformed_from in document["transformed_from"]:
            transformed_from_collection = db[transformed_from["collection"]]

            update_applied_transform = {"$addToSet": {"applied_transformations": {
                "collection": self.full_name,
                "document_id": transform_id,
                "transformation_identifier": transformation_identifier}}}

            transformed_from_collection.update_one({"_id": transformed_from["document_id"]}, update_applied_transform)

        return transform_doc

    def __validate_document(self, document):
        """ Internal document validation helper, uses Object's raw and transform schema attributes

        :Parameters:
          - `document`: The document to insert. Must be a mutable mapping
            type. If the document does not have an _id field one will be
            added automatically.

        :Returns:
          The document type: ["transform", "raw"]
        """

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
        """ Run a transformation on a set of documents

        :Parameters:
          - `query`: A query to select a subset of documents on which to run the transformation. EX.
          {} selects all documents in the collection, {"system": "Albergate"} selects documents with system "Albergate".
          Documentation on this query string can be found here: https://docs.mongodb.com/manual/tutorial/query-documents/
          - `function`: A function to run on selected documents. The function must take file_contents as a string, and
          return file_contents as a string.
          - `transformed_collection_name`: The name of the collection to place the new transformed documents in

        """

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
            transform_doc_id = transformation_collection.insert_one(transform_document).inserted_id

            update_applied_transform = {"$addToSet": {"applied_transformations": {
                "collection": transformation_collection_name,
                "document_id": transform_doc_id,
                "transformation_identifier": transformation_identifier}}}

            self.update_one({"_id": document["_id"]}, update_applied_transform)

            ## Format information:
            # transformation_identifier [(date, function_string)]
            # applied transformation [(collection, document_id, transformation_identifier), ... ]
            # transformed from [(collection, document_id), ... ]

    @staticmethod
    def link_ground_truth(id_1, collection_1, id_2, collection_2):
        """ Static helper to link ground truth documents

        :Parameters:
          - `id_1`: Mongo Document_ID string of first document
          - `collection_1`: Collection object where first document is located
          - `id_2`: Mongo Document_ID string of second document
          - `collection_2`: Collection object where second document is located

        """

        query_1 = {"_id": id_1}
        new_query_1_value = {"$addToSet": {"ground_truth": (collection_2.full_name, id_2)}}

        query_2 = {"_id": id_2}
        new_query_2_value = {"$addToSet": {"ground_truth": (collection_1.full_name, id_1)}}

        collection_1.update_one(query_1, new_query_1_value)
        collection_2.update_one(query_2, new_query_2_value)