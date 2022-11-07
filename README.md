# CLS
**Please View the Raw option to view the system inheritance viewable model **

The Kitchen Inventory System was developed independently by Gibson Green. It is an inventory system to track
the food and drink items in the different containers in the kitchen. It also has a grocery list for the kitchen.
This project was made throughout the Fall Semester of 2021, as an integration school project for Programming II at
Florida Gulf Coast University. 

Frontend
- React
- HTML
- CSS

Backend 
- Flask
- SQLAlchemy
- S3, CloudFront

Data Stored:
User Data
- User Personal Information Data
- First, Last Name
- Email address
- Intended use in accessing data


# Demonstration
 ![Alt text](gibsongreen/OOPorject/files/ezgif-7-58c6575f54.gif)
# Documentation
https://gibsongreen.github.io/OOProject/index.html
	

# Diagrams 
![alt text](https://github.com/gibsongreen/CLS/blob/44cca0aee384e0bbe58cc70cda95d67b389d0bf4/webapp/static/UseCaseDiagram.png)

System Model:

		Container is the grandparent class to								Item is the parent class			Kitchen class
		/			\										/	\
parent class Refridgerator	children classes pantry, canned good, spice drawer			child food class	child drink class
	/
child class Freezer

	- Container class contains name of container, the ability to add and remove items from the container
		the ability to print the inventory of the container, the ability to save the container object to 
		a text file, and the ability to read a text file and convert it into a container object
	- The refridgerator, pantry, canned goods and spice drawer inherit all fields and methods from container
	- the refridgerator adds methodology for temperature
	- the freezer inherits from the grandprarent class, container, and the parent class, refridgerator, with
		functionality changes

	- the item class gives basic functionality to be inherited by the food and drink child classes
	- items can be added and removed to containers
	
	- containers are stored in the kitchen class
		the kitchen class contains objects of the refridgerator, pantry, canned good, spice drawer,
		and freezer classes the kitchen allows access to the different objects to edits objects,
		save them to objects to file, and print inventory
		
	Text Files:
	- allow for returning user to access their kitchen data, or new users to set up their kitchen
	- default kitchen setup, enter as returning user to access default kitchen
	- otherwise, setup your kitchen as a new user, save your container files after updating objects
	
# Getting Started
Clone the repository, Final.cpp is the main function to operate the program

# Built With
- Microsoft Visual Studio 2019 
- Documentation Generated with Doxygen

# Contributing

# Author
- Gibson Green
- Kaden Carr


# Acknowledgments

# History
Version Control System
- Utilization of Git and Github

Sprint History
1. Creat Database file and basic Frontend (HTML and CSS) with Flask
2. Create UI to manipulate and parse Database
3. Upload, Download, and Display files from S3
4. Integate DB and S3 interactions with Flask
5. Create and integrate React with DB and S3

# Key Programming Concepts Utilized


- Follow best practices for style and readability
- Follow best practices for documentation
		
