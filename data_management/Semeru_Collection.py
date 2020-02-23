from pymongo import MongoClient
from pymongo.collection import Collection
import pymongo
class SemeruCollection(Collection):
    pass


client = MongoClient('localhost', 27017)
db = client.test
test = SemeruCollection(database=db, name="source_raw")
print(pymongo.get_version_string())