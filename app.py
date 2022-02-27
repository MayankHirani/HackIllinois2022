import os
from flask import Flask, request
from flask_cors import CORS
import json
#from lib.meetup_cache import MeetupCache

app = Flask(__name__, static_folder='./dist', static_url_path='/')
CORS(app)

#meetups = MeetupCache()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))