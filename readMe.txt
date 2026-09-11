QUICK SETUP
1. Install Python and pip

Install Python on your system. Make sure Python is added to the system PATH during installation.
Check the Python version:
python --version
Check the pip version:
python -m pip --version

2. Check installed packages

To see all Python packages installed in your current environment:
python -m pip list
On Windows, if python is not recognized, use py instead:
py -m pip list

3. Create a virtual environment

To create a virtual environment named venv:
python -m venv venv
This creates an isolated Python environment for your project.
If python is not recognized:
py -m venv venv

4. Activate the virtual environment

On Windows:
venv\Scripts\activate
If the virtual environment is activated successfully, you will see (venv) at the beginning of your terminal:
(venv) D:\FastAPI>

5. Install FastAPI and Uvicorn

With the virtual environment activated, install FastAPI and Uvicorn:
python -m pip install fastapi uvicorn
If python is not recognized:
py -m pip install fastapi uvicorn
You can verify the installed packages:
python -m pip list

6. Start the FastAPI server

Assuming your FastAPI application is in main.py and your FastAPI instance is named app:
from fastapi import FastAPI
app = FastAPI()
Start the server with:
python -m uvicorn main:app --reload
Or on Windows:
py -m uvicorn main:app --reload
The server will normally be available at:
http://127.0.0.1:8000
FastAPI's interactive API documentation is available at:
http://127.0.0.1:8000/docs

7. Deactivate the virtual environment

When you are finished working on the project:
deactivate
The (venv) indicator will disappear from your terminal.