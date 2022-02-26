from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from lib.meetup_cache import MeetupCache

app = Flask(__name__)
api = Api(app)
CORS(app)

meetups = MeetupCache()

class Default(Resource):
    def get(self):
        return {"status": "ok"}

api.add_resource(Default, '/')

if __name__ == '__main__':
    app.run()