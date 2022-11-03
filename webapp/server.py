from flask import Flask, render_template, request, redirect, send_file, Response, jsonify, stream_with_context
#from s3_functions import upload_file, show_image
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import re
import requests
import uuid
from werkzeug.datastructures import Headers
import json
import cv2
import tensorflow
import boto3
import botocore

# init app
basedir = os.path.abspath(os.path.dirname(__file__))  # base directory
app = Flask(__name__)
BUCKET = "cloudstoragevideotest"
UPLOAD_FOLDER = "uploads"


# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ip address of the stream
''''
camera = cv2.VideoCapture('rtsp://192.168.0.25:8557/h264')
def get_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Conent-Type:image\r\n\r\n' + frame + b'\r\n')
'''

# init db and ma
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Database classes
class USER(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __rep__(self):
        return f"Name: {self.first_name}, {self.last_name}"
   # def __init__(self, id, first_name, last_name):
    #    self.id = id
     #   self.first_name = first_name
      #  self.last_name = last_name

class VIDEO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    event_type = db.Column(db.String(10))
    duration = db.Column(db.String(100))
    fps = db.Column(db.Integer, nullable=False)
    original_fps = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(100))
    time = db.Column(db.String(100))
    size = db.Column(db.Float)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    url = db.Column(db.String(100))

    def __rep__(self):
        return f"Name: {self.name}, {self.event_type}"
    #def __init__(self, name, event_type, duration, fps, original_fps, date, time, size, width, height, url):
     #   self.id = id
      #  self.name = name
      #  self.event_type = event_type
      #  self.duration = duration
      #  self.fps = fps
      #  self.original_fps = original_fps
      #  self.date = date
      #  self.time = time
      #  self.size = size
      #  self.width = width
      #  self.height = height
      #  self.url = url

# Database schemas
class VideoSchema(ma.Schema):
    class Meta: # symptom number, symptom, symptom value
        fields = ('id', 'name', 'event_type', 'duration', 'fps', 'original_fps', 'date', 'time', 'size', 'width', 'height', 'url')

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email')

# Init schema

video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)

user_schema = UserSchema()
user_schema = UserSchema(many=True)

#db.drop_all()
#db.create_all()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/live', methods=['GET'])
def test():
    return render_template("live.html")

# linked to /live, to sumbit users to database
@app.route('/add_video', methods=["POST"])
def post_video():
    name = request.form.get("name")
    event_type = request.form.get("event_type")
    duration = request.form.get("duration")
    fps = int(request.form.get("fps"))
    original_fps = int(request.form.get("original_fps"))
    date = request.form.get("date")
    time = request.form.get("time")
    size = float(request.form.get("size"))
    if request.form.get("resolution") == "4k":
        width = 3840
        height = 2160
    elif request.form.get("resolution") == "1080p":
        width=1920
        height=1080
    url = request.form.get("url")

    test_vid = VIDEO(name=name,
                          event_type=event_type,
                          duration=duration,
                          fps=fps,
                          original_fps=original_fps,
                          date=date,
                          time=time,
                          size=size,
                          width=width,
                          height=height,
                          url=url)

    db.session.add(test_vid)
    db.session.commit()

    # upload the file to S3

    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        upload_file(f"uploads/{f.filename}", BUCKET)
    return render_template('live.html')

@app.route('/delete_user/<int:id>')
def delete_user_record(id):
    data = USER.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return render_template('live.html')

@app.route('/delete_video/<int:id>')
def delete_video_record(id):
    data = VIDEO.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return render_template('live.html')

@app.route('/download_video/<string:name>')
def download_video_record(name):
    key = f'uploads/{name}'
    s3 = boto3.resource('s3', aws_access_key_id="AKIAWHZ7WWMI246QZBN5",
         aws_secret_access_key="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")

    try:
        file = s3.Bucket(BUCKET).Object(key).get()
        return Response(
            file['Body'].read(),
            mimetype='text/plain',
            headers={"Content-Disposition": "attachment;filename={}".format(key)}
    )          

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The file selected to download does not exist.")
        else:
            raise Exception

    return render_template('live.html')

@app.route('/archieve', methods=['GET'])
def archieve():
    users = USER.query.all()
    videos = VIDEO.query.all()
    return render_template('results.html', users=users,videos=videos)

@app.route('/event_type_search', methods=['POST'])
def search_by_type():
    event_type_test = request.form.get("event_type")
    #search = VIDEO.query.filter_by(VIDEO.event_type.in_(event_type_test))

    type_search = VIDEO.query.filter(VIDEO.event_type==event_type_test)
    return render_template('home.html', type_search=type_search)

@app.route('/date_search', methods=['POST'])
def search_by_date():
    date_test = request.form.get("date")
    date_search = VIDEO.query.filter(VIDEO.date==date_test)
    return render_template('home.html', date_search=date_search)

@app.route('/date_time_search', methods=['POST'])
def search_by_date_time():
    date_t = request.form.get("date")
    time_t = request.form.get("time")
    date_time_search = VIDEO.query.filter((VIDEO.date==date_t) & (VIDEO.time==time_t))
    return render_template('home.html', date_time_search=date_time_search)

# temporarily create account page
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

# linked to /about, to sumbit users to database
@app.route('/add_user', methods=["POST"])
def account():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    
    user = USER(first_name=first_name, last_name=last_name,email=email)
    db.session.add(user)
    db.session.commit()
    return render_template('about.html')

def upload_file(file_name, BUCKET):
    object_name = file_name
    s3 = boto3.resource('s3', aws_access_key_id="AKIAWHZ7WWMI246QZBN5",
         aws_secret_access_key="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")
    response = s3.meta.client.upload_file(file_name, BUCKET, object_name)
    return response

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        upload_file(f"uploads/{f.filename}", BUCKET)
        return render_template("liveview.html")

@app.route('/view_video/<string:name>')
def view_video(name):
    key = f"https://d1skcoh8jzfxme.cloudfront.net/uploads/{name}"
    return render_template('liveview.html', key=key)

@app.route('/liveview', methods=['GET'])
def live():
    return render_template('liveview.html')






'''
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace;boundary=frame')
'''

@app.route('/login', methods=['GET'])
def login():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)