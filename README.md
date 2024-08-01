The project is creation of an address book application using FastAPI that performs the following tasks:

1) Create, update, and delete addresses:

    a. Addresses should contain coordinates.
    b. Addresses should be saved in an SQLite database.
    c. Addresses should be validated.
2) Retrieve addresses within a given distance and location coordinates.

3) No GUI is required so the built-in FastAPI’s Swagger Doc is sufficient.

To run the project please follow below steps:
    1. Install dependencies using pip install -r requirements.txt.
    2. Run the application with uvicorn main:app --reload.
    3. Access the API documentation at http://127.0.0.1:8000/docs.
