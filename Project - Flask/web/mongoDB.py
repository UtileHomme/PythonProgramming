from pymongo import MongoClient

class MongoDB:
    @classmethod
    def connect(cls, collection_name):
        client = MongoClient("mongodb://localhost:27017/")
        # client = MongoClient('localhost', 27017)
        # client = MongoClient(host="localhost", port=27017)
        # client = MongoClient("mongodb://localhost:27017")
        db = client.QuestionsDatabase
        questions = db[collection_name]
        return questions
