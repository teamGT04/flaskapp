import os

from flask import Flask, request, url_for, render_template
from flask_pymongo import PyMongo
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

img = os.path.join('static', 'Image')
@app.route('/rickroll')
def home():
    file = os.path.join(img, 'GP.png')
    return render_template('image_render.html', image=file)

if __name__=='__main__':
    app.run(debug=True)
