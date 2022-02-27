import os
from flask import Flask, request
from flask_cors import CORS
import json
from lib.location import Location
from lib.meetup_cache import MeetupCache
from lib.database import RestaurantDatabase
from lib.attendee import Attendee

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

@app.route('/getmymeetups', methods=['GET'])
def getmymeetups():
    user_id = str(request.args.get('id', type=str))
    my_meetups = []
    for meetup in meetups.get_user_meetups(user_id):
        my_meetups.append(meetup.json())
    return { "meetups" : json.dumps(my_meetups) }

@app.route('/getmeetups', methods=['GET'])
def getmeetups():
    user_id = str(request.args.get('id', type=str))
    latitude = float(request.args.get('lat', type=float))
    longitude = float(request.args.get('lon', type=float))
    distance = int(request.args.get('distance', type=int))
    my_meetups = []
    for meetup in meetups.get_available_meetups(user_id, Location(latitude, longitude), distance):
        my_meetups.append(meetup.json())
    return { "meetups" : json.dumps(my_meetups) }

@app.route('/getrestaurants', methods=['GET'])
def getrestaurants():
    latitude = float(request.args.get('lat', type=float))
    longitude = float(request.args.get('lon', type=float))
    distance = int(request.args.get('distance', type=int))
    my_restaurants = []
    for restaurant in db.get_restaurants_available(Location(latitude, longitude), distance):
        my_restaurants.append(restaurant.json())
    return { "restaurants" : json.dumps(my_restaurants) }

@app.route('/createmeetup', methods=['GET'])
def createmeetup():
    print(request.form)
    rid = str(request.args.get('rid', type=str))
    restaurant = db.get_restaurant(rid)
    time = str(request.args.get('time', type=str))
    user_id = str(request.args.get('id', type=str))
    emoji = str(request.args.get('emoji', type=str))
    size = int(request.args.get('size', type=int))
    meetups.create_meetup(restaurant, time, Attendee(user_id, emoji), size)
    return json.dumps({ "status" : "ok" })

@app.route('/joinmeetup', methods=['GET'])
def joinmeetup():
    user_id = str(request.args.get('id', type=str))
    emoji = str(request.args.get('emoji', type=str))
    mid = str(request.args.get('mid', type=str))
    meetups.get_meetup(mid).add_attendee(Attendee(user_id, emoji))
    return json.dumps({ "status" : "ok" })

@app.route('/leavemeetup', methods=['GET'])
def leavemeetup():
    user_id = str(request.args.get('id', type=str))
    mid = str(request.args.get('mid', type=str))
    meetups.get_meetup(mid).remove_attendee(user_id, meetups)
    return json.dumps({ "status" : "ok" })

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))