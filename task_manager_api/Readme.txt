Task Manager API
This API allows user to manage task with built using JWT authentication .  REST API  for managing Tasks allows users to create, retrieve, update, and delete Task.



Installation
1. Clone the repository
Copy
git clone https://github.com/yourusername/django-product-api.git
cd django-product-api
2. Set up a virtual environment
Create and activate  virtual environment for the project:
Copy
python3 -m venv venv_task
source venv_task/bin/activate  

3.
Install all the dependencies:
Copy and paste below command into terminal
pip3 install -r requirements.txt

4. Set up the database
Run the below command to create  database tables:
Copy
python manage.py migrate

7. Run the development server
Now, you can run the Django development server:

Copy
python manage.py runserver
Your API will be served at http://127.0.0.1:8000/.

Features
User module:
  -->  user registration , retrieving all the users, retrieving single user , update existing user data.
  -->  user gets token for accessing api endpoints once user successfully registered.
Task module:
 --> user can Create, retrive, update, and delete tasks
 --> user can List all tasks
 --> user can Retrieve task details by ID


API Endpoints
|-------------------------Token Endpoints--------------------------|

1. POST http://127.0.0.1:8000/token/
Description: Request for the Access token {access token valid for 15 min }  {refresh token valid for 1day } 
Response body: JSON array of data include fields : username and password
Sample Response :{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MjM3ODQ0NSwiaWF0IjoxNzQyMjkyMDQ1LCJqdGkiOiI3NzQ4MDViMmY5NDc0MmI5YmI1NDI5MzczYzJmYjM1YyIsInVzZXJfaWQiOjR9.MjGvl3RGYhZQQwOf0hFo7Mw-DexXlVJ6CpIGFHHK2W0",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMjkyOTQ1LCJpYXQiOjE3NDIyOTIwNDUsImp0aSI6ImQwZDI0NGI0NTIwMzQ4OGJiZmU4NTA5ZTRhYjZhYWUxIiwidXNlcl9pZCI6NH0.uS37BL3S93p_b3zO1ZE9LyhkwpWkKZimmU08KoU_3uY"
}


2. POST http://127.0.0.1:8000/token/token_refresh/
Description: Request for the refresh existing token 
Response body: JSON array of data include field : refresh : <refresh>
Sample Response:{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMjkyOTQ1LCJpYXQiOjE3NDIyOTIwNDUsImp0aSI6ImQwZDI0NGI0NTIwMzQ4OGJiZmU4NTA5ZTRhYjZhYWUxIiwidXNlcl9pZCI6NH0.uS37BL3S93p_b3zO1ZE9LyhkwpWkKZimmU08KoU_3uY"
}

3. POST  http://127.0.0.1:8000/token_verify/
Description: Request for the verfying existing token 
Response body: JSON array of data include field : token :<token>
Sample Response:
Valid Token: If the token is valid, the response will be an empty body.
Invalid Token: If the token is invalid or expired, the response will  an error message.


|------------------------User Endpoints-------------------|

1. GET http://127.0.0.1:8000/UserAPI/    ### Note Append header -:Authorization :bearer <token>
Description: Retrieve a list of all USERS.
Response: JSON array of Users objects.

2. GET http://127.0.0.1:8000/UserAPI/{id}/ ### Note Append header -:Authorization :bearer <token>
Description: Retrieve a single User by its ID.
Response: JSON object with single user details.

3. POST http://127.0.0.1:8000/UserAPI/
Description: Create a new User.
Request Body: JSON  containing user data details.
include username,email,password,confirm password

Sample Response include user details with Authorizationtoken JWT

4. PUT http://127.0.0.1:8000/UserAPI/{id}/      ### Note Append header -:Authorization :bearer <token>
Description: Update a user data by its ID.
Request Body: JSON object with update user details.

5. PATCH http://127.0.0.1:8000/UserAPI/{id}/        ### Note Append header -:Authorization :bearer <token>
Description: Update a partial user data  by its ID.
Request Body: JSON object with update User details.

|------------------Task Endpoints------------------|

--> all the endpoints of task api secured with jwt token so make sure to insert valid token in header.
---> key = Authorization
---> value = bearer <token>

1. GET http://127.0.0.1:8000/TaskAPI/    
Description: Retrieve a list of all Tasks.
Response: JSON array of Tasks objects.

2. GET http://127.0.0.1:8000/TaskAPI/{id}   
Description: Retrieve a single  Task.
Response: JSON array of Task object.

3. POST http://127.0.0.1:8000/TaskAPI/   
Description: Create  a single  Task.
Response body : JSON array of Task data.
fields include : title,description,user

4. PUT http://127.0.0.1:8000/TaskAPI/{id}   
Description: Update a single  Task data.
Response: JSON array of Task object.

5. PATCH http://127.0.0.1:8000/TaskAPI/{id}   
Description: Update partial details of  single  Task .
Response: JSON array of Task object.

6. DELETE http://127.0.0.1:8000/TaskAPI/{id}   
Description: Delete  single  Task . Implemented soft delete .
Response: JSON success message .

