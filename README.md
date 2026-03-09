# DCC ShutterSeek

A Django web application to search and display images using the Unsplash API. Users can enter keywords and get relevant pictures directly from Unsplash.

# Features

1. Simple and clean interface for image search
2. unsplash API integration for fetching

## How to Use

- Search for any keyword in the search box to find images.
- To manage users, groups, or content, visit http://127.0.0.1:8000/admin/ and login with your superuser account.
 
## Installation & Setup

1. Clone this repository:
   git clone https://github.com/Sanjana-33/django-shutterseek.git

2. Install dependencies:
   pip install -r requirements.txt

3. Run database migrations:
   python manage.py migrate

4. (Optional) Create a superuser for admin panel:
   python manage.py createsuperuser

5. Start the server:
   python manage.py runserver

6. Open http://127.0.0.1:8000/ in your browser
