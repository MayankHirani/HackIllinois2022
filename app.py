import os
from turtle import distance
from flask import Flask, request
from flask_cors import CORS
import json
from lib.location import Location
from lib.meetup_cache import MeetupCache
from lib.database import RestaurantDatabase

app = Flask(__name__, static_folder='./dist', static_url_path='/')
CORS(app)

db = RestaurantDatabase("data/restaurant_data.json")

meetups = MeetupCache()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


@app.route('/validate', methods=['POST'])
def validate():
    cube = np.array(json.loads(request.form["cube"]))
    pass

@app.route('/getmymeetups', methods=['GET'])
def solvePassed():
    user_id = request.args.get('id', type=str)
    my_meetups = []
    for meetup in meetups.get_user_meetups(user_id):
        my_meetups.append(meetup.json())
    return json.dumps(my_meetups)

@app.route('/getmeetups', methods=['GET'])
def solvePassed():
    user_id = request.args.get('id', type=str)
    latitude = request.args.get('lat', type=float)
    longitude = request.args.get('lon', type=float)
    distance = request.args.get('distance', type=int)
    my_meetups = []
    for meetup in meetups.get_available_meetups(user_id, Location(latitude, longitude), distance):
        my_meetups.append(meetup.json())
    return json.dumps(my_meetups)

@app.route('/getmeetups', methods=['GET'])
def solvePassed():
    user_id = request.args.get('id', type=str)
    latitude = request.args.get('lat', type=float)
    longitude = request.args.get('lon', type=float)
    distance = request.args.get('distance', type=int)
    my_meetups = []
    for meetup in meetups.get_available_meetups(user_id, Location(latitude, longitude), distance):
        my_meetups.append(meetup.json())
    return json.dumps(my_meetups)

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))