# CLS

Cloud Storage System is a web database server that enables users to view, upload, and download video files and related metadata of Lightning Events. 
This version of CLS will contain videos captured by Gibson Green, relating to the Physics publication "Lightning Activities in Different Meteorological
Conditions." Videos have been modified with VideoEditing Software written by Gibson Green, and these are the videos displayed, typically, at a reduced
FPS rate, to gain a better understanding of these high speed events. These videos are to be used for educational use only. 

# Mockup
https://www.figma.com/file/7GGntTgTTAjbQwLr1MAEcD/Cloud-Storage?node-id=0%3A1

![alt text](https://github.com/gibsongreen/CLS/blob/a54594b331b327a04c7dae3b3d85845b221bb87a/webapp/static/Image.jpeg)

Data Stored:
User Data
- User Personal Information Data
- First, Last Name
- Email address

Video Data
- Name
- Event Type
- Duration
- Frames per Second
- Original FPS
- Date
- Time
- Size of File
- Resolution


# Demonstration


# Documentation

	

# Diagrams 
![alt text](https://github.com/gibsongreen/CLS/blob/44cca0aee384e0bbe58cc70cda95d67b389d0bf4/webapp/static/UseCaseDiagram.png)

	
# Getting Started
Clone the repository, within the webapp folder, run the server.py file to get started locally.

# Built With
Frontend
- React (Not integrated yet)
- HTML
- CSS

Backend 
- Flask
- SQLAlchemy, Marshmallow
- S3, CloudFront

# Contributing

# Authors
- Gibson Green
- Kaden Carr


# Acknowledgments

# History
Version Control System
Local VCS
- Git
Repository Hosting
- Github

Sprint Overview History (View Issues)
1. Agile Planning (9/1-9/13)
- AWS Architectual Diagram (Kaden), Database Schema Diagram (Gibson), Figma Mockup (V1. Gibson, V2. Kaden), Use Cases (Gibson), Use Case Diagram (Gibson)
2. Creat Database file and basic Frontend (HTML and CSS) with Flask (9/13-9/20)
- SQL Alchemy(Gibson) and Flask (Kaden) developed seperately, then integrated 
3. Create UI to manipulate and parse Database (Gibson) (9/20-9/27)
- After initial integration, records can be added, modified, and deleted
4. Upload, Download, and Display files from S3 (Gibson) (10/21-10/28)
- From Flask, ability to interact and manipulate with S3
5. Integate DB and S3 interactions with Flask (Gibson) (10/28-10/31)
- SQLAlchemy DB (Flask local) and S3 integrated together 
6. Create and integrate React with DB and S3 (Kaden) (11/1-TBD)

# Key Programming Concepts Utilized
- Team Communication utilizing Slack, 1-2 in-person/virtual meetings per week
- Agile & Sprint Methodologies utilized
- Best practices for style, readability, documentation from docs.python standard
https://docs.python-guide.org/writing/style/
