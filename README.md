FastAPI Backend
This project is a FastAPI-based backend for retrieving metadata about 3D models. It provides a simple API to fetch model-related information.

Features
Developed using FastAPI for high performance.

Supports CORS for seamless frontend integration.

Offers metadata retrieval for 3D models.

Includes interactive API documentation with Swagger UI.

Installation Guide
Follow these steps to set up and run the backend locally:

1. Clone the Repository
First, clone the repository to your local machine:

bash
git clone https://github.com/bisher-muhammed/fastApi-backend.git
cd fastApi-backend
2. Create and Activate a Virtual Environment
Set up a virtual environment for the project:

bash
python -m venv venv
Activate the virtual environment:

On Windows:

bash
venv\Scripts\activate
3. Install Dependencies
Install all the required dependencies using:

bash
pip install -r requirements.txt
Running the Application
Navigate to the project directory and start the FastAPI server:

bash
python -m uvicorn main:app --host 0.0.0.0 --port 5000 --reload
The server will be running at: http://127.0.0.1:5000

API Documentation
FastAPI provides interactive API documentation with Swagger UI. Visit the documentation at: http://127.0.0.1:5000/docs

Endpoints
1. Retrieve 3D Model Metadata
URL: /python-model-info

Method: GET

Full URL: http://127.0.0.1:5000/python-model-info



