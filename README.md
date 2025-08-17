# StructaGen
A backend system for generating telecom tower mast structural reports.

StructaGen

StructaGen is a backend project for generating structural analysis reports for telecom towers. It allows engineers to input tower data, antenna loading, and stress analysis results, and automatically generate professional reports in .docx format.

Features (Planned)

Manage tower and antenna data.

Calculate EPA (Effective Projected Area) and FPA (Full Projected Area).

Store stress analysis results.

Auto-generate structural reports with placeholders for images and charts.

Export reports in .docx format.

Tech Stack

Backend: Django, Django REST Framework

Database: SQLite (development), PostgreSQL (production)

Report Generation: Python-docx

Version Control: Git + GitHub

Project Setup

Clone the repo:

git clone https://github.com/Anumatsue/StructaGen.git
cd StructaGen


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows


Install dependencies:

pip install -r requirements.txt


Run migrations:

python manage.py migrate


Start the development server:

python manage.py runserver

Status

Project in early development phase (Capstone project @ ALX Africa).

Author

Paschal Ebitse