from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import bcrypt

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.QuestionsDatabase
questions = db['questions']


class storeQuestion(Resource):
    def post(self):
        postedData = request.get_json()
        questionDescription = postedData["questionDescription"]

        questions.insert({
            # '_id': 2,
            'questionDesc': questionDescription
        })

        retJson = {
            "status": 200,
            "message": "Question saved successfully"
        }

        return jsonify(retJson)


class getQuestionList(Resource):
    def get(self):
        question = list(questions.find({}, {'_id': 0}))

        retJson = {
            "status": 200,
            "questionsList": question
        }

        return jsonify(retJson)

        # return jsonify([question for question in questionList])


class getQuestion(Resource):
    def post(self, id):
        postedData = request.get_json()

        self.id = id

        users.update({
            "Username": username,
        }, {
            "$set": {
                "Tokens": num_tokens - 1
            }
        })

        sentence = users.find({
            "Username": username,
        })[0]["Sentence"]

        retJson = {
            "status": 200,
            "message": sentence
        }

        return jsonify(retJson)


api.add_resource(storeQuestion, '/storeQuestion')
api.add_resource(getQuestion, '/getQuestion/<int:id>')
api.add_resource(getQuestionList, '/getQuestionList')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
