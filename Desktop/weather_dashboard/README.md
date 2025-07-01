# Personal Weather Dashboard

A Django REST Framework based personal weather dashboard that allows users to register, login, update their location, and get real-time weather updates using OpenWeatherMap API.

---

## Features

- User registration and JWT-based authentication  
- Update location via city/country or latitude/longitude  
- Fetch current weather data for saved location  
- Simple and clean frontend for login, register, and dashboard  

---

## Setup Instructions

### 1. Clone the repository
    git clone <your-repo-url>
    cd <your-repo-folder>


2. Create and activate a virtual environment

    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate


3. Install dependencies

    pip install -r requirements.txt

4. Setup environment variables
    Create a .env file in the project root with the following keys:

    .env
    SECRET_KEY=your_django_secret_key
    WEATHER_API_KEY=your_openweathermap_api_key
5. Run migrations
    python manage.py migrate
6. Run the development server

    python manage.py runserver


Open your browser and visit http://127.0.0.1:8000/ to access the home page.

How to Test?
    Register a new user:
    Go to http://127.0.0.1:8000/api/users/register-page/ and create an account.

    Login:
    Go to http://127.0.0.1:8000/api/users/login-page/ and login with your credentials.

    Dashboard:
    After login, you will be redirected to the dashboard where you can view weather data and update your location.

    Update Location:
    Use the form to set your city/country or latitude/longitude. Weather data will refresh accordingly.

Requirements
All required packages are listed in requirements.txt. Example content:

    Django>=4.0
    djangorestframework
    djangorestframework-simplejwt
    requests
    python-dotenv
Install them via:
    pip install -r requirements.txt


Notes
***Make sure your .env file is never committed to the repository.***

***You must obtain your own API key from OpenWeatherMap.***

***The frontend is simple HTML/CSS/JS and uses JWT stored in localStorage.***