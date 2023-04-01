import os

from flask import Flask, request, url_for, render_template
from flask_pymongo import PyMongo
import pymongo
app=Flask(__name__)
app.config['MONGO_URI']="mongodb://camnode:camnode@10.147.18.11:27017/?authSource=crimedb"
mongo=PyMongo(app)

@app.route('/')
def index():
    return '''1
    <form method="POST" action="/create" enctype="multipart/form-data">
    <input type="text" name="username">
    <input type="file" name="profile_image">
    <input type="submit">
    </form>
    
    '''
client=pymongo.MongoClient('mongodb://admin:admin@10.147.18.11:27017/')

crimedb=client['crimedb']

crime = crimedb["crime"]

img = os.path.join('static', 'img')
@app.route('/rickroll')
def home():
    os.system("scp raspi@192.168.205.244:/images/latest.jpg ./static/img/")
    file = os.path.join(img, 'latest.jpg')
    return render_template('image_render.html', image=file)
def add():
    response=request.form['approvalStatus']
    crimedb.crime.insert_one({'approvalStatus':response})

@app.route('/maps')
def map():
    markers = [
        {
            'lat': 12.986914,
            'lon': 79.972192,
            'popup': 'chennai'
        },

    ]
    return render_template('map.html', markers=markers)


if __name__=='__main__':
    app.run(debug=True)
