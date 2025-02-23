# Data Submission System

A Django-based data submission system that helps users manage their data submissions.

## Features

- Track data submissions with categorization
- View data submissions history with filtering options
- Export data submissions to CSV
- Search data submissions
- Create new data submissions

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup Instructions

1. Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run database migrations:

```bash
python manage.py migrate
```

4. (Optional) Seed the database with sample data:

```bash
python manage.py seed_submissions
```

5. Start the development server:

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

- `submissions/` - Main application directory
  - `models.py` - Database models for Submission
  - `views.py` - View functions for handling requests
  - `forms.py` - Form definitions for data validation
  - `management/commands/` - Custom management commands
  - `templates/` - HTML templates
  - `migrations/` - Database migrations

## AI Usage Report

#HTMX
--For the frontend, since I had no experience with HTMX, I first used a simple template with basic CRUD functionality. After completing it, I tried converting it to HTMX using Cursor Composer and solved issues. Later, I noticed some changes in my backend code due to HTMX integration, so I worked on understanding and adjusting my backend accordingly.But ,starting to realize the usage of htmx which is to update the contents dynamically by eding sections htmx request.

#Fake Data
--As I had no experience with mock data generation in Python, I used Cursor Composer to generate fake data. Then, I analyzed the code, understood it, and made some modifications.

#Pagination
--I used htmx for pagination, and I let the AI do the complex query params for the htmx request.and i just care the data sent from the backend to the frontend.

#Filtering
--I used htmx for filtering, and I let the AI do the complex query params for the htmx request.and i just care the data sent from the backend to the frontend.

#Search
--I used htmx for search, and I let the AI do the complex query params for the htmx request.and i just care the data sent from the backend to the frontend and noticed htmx is powerful  for dynamic content update.





