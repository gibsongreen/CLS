# CLS
**Please View the Raw option to view the system inheritance viewable model **

The Kitchen Inventory System was developed independently by Gibson Green. It is an inventory system to track
the food and drink items in the different containers in the kitchen. It also has a grocery list for the kitchen.
This project was made throughout the Fall Semester of 2021, as an integration school project for Programming II at
Florida Gulf Coast University. 

Version Control System
Utilization of Git and Github

Sprint History
1. Creat Database file and basic Frontend (HTML and CSS) with Flask
2. Create UI to manipulate and parse Database
3. Upload, Download, and Display files from S3
4. Integate DB and S3 interactions with Flask
5. Create and integrate React with DB and S3


Frontend
- React
- HTML
- CSS

Backend 
- Flask
- SQLAlchemy
- S3, CloudFront

![alt text](https://github.com/gibsongreen/CLS/blob/44cca0aee384e0bbe58cc70cda95d67b389d0bf4/webapp/static/UseCaseDiagram.png)


Data Stored:
- User Data
- User Personal Information Data
- First, Last Name
- Email address
- Intended use in accessing data


# Demonstration
 ![Alt text](gibsongreen/OOPorject/files/ezgif-7-58c6575f54.gif)
# Documentation
https://gibsongreen.github.io/OOProject/index.html
	

# Diagrams 

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


# Acknowledgments
- https://www.cmi.ac.in/~madhavan/courses/pl2009/lecturenotes/lecture-notes/node28.html#:~:text=Subtyping%20refers%20to%20compatibility%20of,refers%20to%20reuse%20of%20implementations
- https://www.geeksforgeeks.org/
- https://www.learncpp.com/

# History
- N/A

# Key Programming Concepts Utilized
LO1. Design and implement a class. 

LO4. Include a comment in which you compare and contrast the procedural/functional approach and the object-oriented approach

LO1a. At least one class in a header file with non-trivial methods implemented in a cpp file

LO1b. Overload a constructor 

LO1c. Utilize an initialization list

LO2. Use subclassing to design simple class hierarchies that allow code to be reused for distinct subclasses.

LO2a. Include comments describing the visibility inheritance model

LO3. Correctly reason about control flow in a program using dynamic dispatch. 

LO5. Explain the relationship between object-oriented inheritance (code-sharing and overriding) and subtyping (the idea of a subtype being usable in a context that expects the supertype).

LO6. Use object-oriented encapsulation mechanisms such as interfaces and private members.

LO7. Define and use iterators and other operations on aggregates, including operations that take functions as arguments. 

- Follow best practices for style and readability
- Follow best practices for documentation
		
