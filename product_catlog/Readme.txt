Simple Product API
This is a simple REST API  for managing products. It allows users to create, retrieve, update, and delete product data.



Installation
1. Clone the repository
Copy
git clone https://github.com/Nirav-Zignuts/Advance_Python.git
cd django-product-api
2. Set up a virtual environment
Create and activate  virtual environment for the project:
Copy
python3 -m venv venv_product
source venv_product/bin/activate  

3.
Install all the dependencies:
Copy and paste below command into terminal
pip3 install -r requirements.txt

4. Set up the database
Run the below command to create  database tables:
Copy
python3 manage.py migrate

7. Run the development server
Now, you can run the Django development server:

Copy
python manage.py runserver
Your API will be served at http://127.0.0.1:8000/.

Features
Create, read, update, and delete products
List all products
Retrieve product details by ID
Update product information 
Update partital product information 
Delete products from the database 


API Endpoints
1. GET http://127.0.0.1:8000/product_catlog/
Description: Retrieve a list of all products.
Response: JSON array of product objects.

2. GET http://127.0.0.1:8000/product_catlog/{id}/
Description: Retrieve a single product by its ID.
Response: JSON object with product details.

3. POST http://127.0.0.1:8000/product_catlog/
Description: Create a new product.
Request Body: JSON  containing product details.

4. PUT http://127.0.0.1:8000/product_catlog/{id}/
Description: Update a product data by its ID.
Request Body: JSON object with update product details.

5. PATCH http://127.0.0.1:8000/product_catlog/{id}/
Description: Update a partial product data  by its ID.
Request Body: JSON object with update product details.

5. DELETE http://127.0.0.1:8000/product_catlog/{id}/
Description: Delete a product by its ID.(soft delete)
Response: response with a message .



Test Cases
there is a folder named tests in product_drf folder which contains all the test cases for application
Unit testing :
folder contain all 3 unit testing
1 . Model Testing
2 . Serializer Testing
3 . Views Testing

To run all the test cases execute following command in terminal:
python3 manage.py test
 it will show you all number of the test cases executes along with test cases which fails  
