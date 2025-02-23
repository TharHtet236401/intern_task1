# Data Submission System

A Django-based data submission system with real-time updates using HTMX. This project demonstrates modern web development practices by combining Django's robust backend with HTMX's dynamic frontend capabilities.

## Features

- ✨ Real-time content updates without full page reloads
- 🔍 Dynamic search with instant results
- 📊 Category and status filtering
- 📄 Pagination with state preservation
- ✅ Review status updates

## Tech Stack

- Python 3.x
- Django 5.1.6
- HTMX
- SQLite
- Faker (for demo data)

## Quick Start

1. Clone the repository
```bash
git clone https://github.com/TharHtet236401/intern_task1.git
cd intern_task1
```

2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. (Optional) Load sample data
```bash
python manage.py seed_submissions
```

6. Start development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Project Structure

```
data-submission-system/
├── submissions/                 # Main application
│   ├── management/             # Custom management commands
│   │   └── commands/          
│   │       └── seed_submissions.py
│   ├── templates/             # HTML templates
│   │   └── submissions/
│   │       └── partials/     # HTMX partial templates
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── urls.py              # URL routing
│   └── forms.py             # Form definitions
├── templates/               # Base templates
├── requirements.txt        # Project dependencies
├── manage.py              # Django management script
└── README.md             # Project documentation
```

## Development Insights

### HTMX Integration
The project leverages HTMX for dynamic content updates, demonstrating:
- Partial page updates for search and filtering
- Dynamic status updates without page reload
- Pagination with state preservation
- Form submissions with instant feedback

### Data Management
- Efficient database queries with Django ORM
- Custom management command for seeding test data

## AI Usage Report

-HTMX
--For the frontend, since I had no experience with HTMX, I first used a simple template with basic CRUD functionality. After completing it, I tried converting it to HTMX using Cursor Composer and solved issues. Later, I noticed some changes in my backend code due to HTMX integration, so I worked on understanding and adjusting my backend accordingly.But ,starting to realize the usage of htmx which is to update the contents dynamically by eding sections htmx request.

-Fake Data
--As I had no experience with mock data generation in Python, I used Cursor Composer to generate fake data. Then, I analyzed the code, understood it, and made some modifications.

-Pagination
--I used htmx for pagination, and I let the AI do the complex query params for the htmx request.and i just care the data sent from the backend to the frontend.

-Filtering
--I used htmx for filtering, and I let the AI do the complex query params for the htmx request.and i just care the data sent from the backend to the frontend.

-Search
--I used htmx for search, and I let the AI do the complex query params for the htmx request.and i just care the data sent from the backend to the frontend and noticed htmx is powerful  for dynamic content update.

-Server time to local time
--I used the AI Composer with command to change the server time to local time and justify the understanding of the code.

-Request 
--Although I try to modulate the css and js with separate files, but I had some issues with the htmx request also due to time constraint for me to do it.I will make sure to understand the usage of static files and modulate the css and js with separate files before interview.





