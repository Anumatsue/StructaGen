StructaGen API

StructaGen is a Django REST Framework (DRF) project designed for structural reporting of telecom towers.
The API allows engineers to input tower and antenna parameters, automatically calculate stresses, and generate structured reports.

🚀 Features

🔑 JWT Authentication (secure login/logout with access & refresh tokens)

🏗️ Tower Management (CRUD endpoints for tower models)

📡 Antenna Management with auto-calculated EPA & FPA values

📊 Stress & Deflection Results linked to tower models

📝 Reports automatically generated upon data submission

🌐 RESTful API tested with Postman & DRF Browsable API

📦 Tech Stack

Backend: Django, Django REST Framework

Database: SQLite (development), can be switched to PostgreSQL/MySQL in production

Authentication: JWT (SimpleJWT)

Deployment: PythonAnywhere

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/Anumatsue/structagen.git
cd structagen


Create a virtual environment

python -m venv .env
source .env/bin/activate   # Linux/Mac
.env\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py makemigrations
python manage.py migrate


Create a superuser

python manage.py createsuperuser


Run development server

python manage.py runserver

🔑 Authentication (JWT)

Obtain tokens:

POST /api/auth/login/
{
  "username": "your_username",
  "password": "your_password"
}


Response:

{
  "access": "your-access-token",
  "refresh": "your-refresh-token"
}


Use Authorization: Bearer <access_token> in Postman or frontend requests.

📡 API Endpoints (examples)
Towers

GET /api/towers/ – List towers

POST /api/towers/ – Create tower

GET /api/towers/{id}/ – Retrieve tower

Antennas

POST /api/antennas/ – Add antenna (EPA/FPA auto-calculated)

Stress Results

POST /api/stress-results/ – Stress ratio, deflection
Reports

GET /api/reports/ – List all generated reports

🌍 Deployment (PythonAnywhere)

Push code to GitHub

Create a PythonAnywhere account

Pull project from GitHub into PythonAnywhere console

Create and activate virtualenv, install dependencies

Run:

python manage.py migrate
python manage.py collectstatic


Configure WSGI file to point to Django project

Map /static/ to STATIC_ROOT in PythonAnywhere static files settings

Reload web app 🎉

🧹 Notes

Migrations: Keep only clean migration files before final deployment (delete redundant ones if project was restarted multiple times).

collectstatic: Needed for CSS/JS/images in production.

Database: SQLite works on PythonAnywhere, but PostgreSQL is recommended for scalability.

👨‍💻 Author

Paschal Ebitse – Backend Software Engineer (ALX Africa Capstone Project)

Project in early development phase (Capstone project @ ALX Africa).

Author

Paschal Ebitse
