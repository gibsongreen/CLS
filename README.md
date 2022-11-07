# CLS

Cloud Storage System is a web database server that enables users to view, upload, and download video files and related metadata of Lightning Events. 
This version of CLS will contain videos captured by Gibson Green, relating to the Physics publication "Lightning Activities in Different Meteorological
Conditions." Videos have been modified with VideoEditing Software written by Gibson Green, and these are the videos displayed, typically, at a reduced
FPS rate, to gain a better understanding of these high speed events. These videos are to be used for educational use only. 

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

# Author
- Gibson Green
- Kaden Carr


# Acknowledgments

# History
Version Control System
- Utilization of Git and Github

Sprint Overview History
1. Creat Database file and basic Frontend (HTML and CSS) with Flask
- SQL Alchemy(Gibson) and Flask (Kaden) developed seperately, then integrated 
2. Create UI to manipulate and parse Database (Gibson)
- After initial integration, records can be added, modified, and deleted
3. Upload, Download, and Display files from S3 (Gibson)
- From Flask, ability to interact and manipulate with S3
4. Integate DB and S3 interactions with Flask (Gibson)
- SQLAlchemy DB (Flask local) and S3 integrated together
5. Create and integrate React with DB and S3 (Kaden) (TBD)

# Key Programming Concepts Utilized
- Best practices for style and readability utilized
- Best practices for documentation utilized
		
