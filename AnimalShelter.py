from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, userName, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        #self.client = MongoClient('mongodb://aacuser:pass1234@localhost:38423/AAC')
        self.client = MongoClient('mongodb://' + userName + ':' + password +'@localhost:38423/AAC')
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            print("Success")
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            return self.database.animals.findOne(data)
            print("Success")
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# Create method to implement the R in CRUD.
    def readAll(self, data):
        if data is not None:
            return self.database.animals.find(data,{"_id":False})
            print("Success")
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# Method to update
    def update(self, data, data2):
        if data is not None:
            self.database.animals.update_one(data, {"$set":data2})
            print("Update success")
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# Method to delete
    def delete(self, data):
        if data is not None:
            self.database.animals.delete_one(data)
            print("Delete success")
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
        