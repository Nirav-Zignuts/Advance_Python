Simple Django Blog Application
This is a simple Django-based blog application where users can create, view, edit, and delete blog posts. The application includes basic functionalities such as user authentication and CRUD (Create, Read, Update, Delete) operations for blog posts.


Installation Guide

Requirements
To run this project, you will need to have the following things installed:


Python 3.9
Django 
SQLite (default database used in this project)




Installation
1. first clone the repository
go to terminal and do following
Copy 
git clone https://github.com/Nirav-Zignuts/Advance_Python.git
cd django-blog
2. Set up a virtual environment

Copy below command 
python3 -m venv venv
source venv/bin/activate  
3. Install dependencies
Install the required Python packages :

Copy
pip3 install -r requirements.txt
4. Set up the database
Run the following command to create the  database tables:
Copy
python manage.py migrate

5. Run the using below command server
Now, you can run the Django development server:
Copy
python3 manage.py runserver
Your application will be served at http://127.0.0.1:8000/.


Features
Basic User Authentication System includes -> registration , login , logout , change password , forgot password  with email sent.
An authenticated User can Create, view , update, and delete (soft delete) blog posts
Basic navigation (home page, login, register)


