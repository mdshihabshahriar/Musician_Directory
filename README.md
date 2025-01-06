Musicians Directory
A web application built using Python, Django, HTML, and CSS that allows users to manage musicians and their albums efficiently.

Features
Musician Management:

Create, view, edit, and delete musician details.
Fields include:
First Name
Last Name
Email
Phone Number
Instrument Type
Album Management:

Add, view, edit, and delete album details.
Fields include:
Album Name
Rating (1–5)
Release Date
Each album is associated with a musician (one-to-many relationship).
User-Friendly Interface:

Display musicians and albums in a tabular format.
Edit musician data by clicking the musician's name.
Edit album data using the Edit button in the actions column.

Instructions
Click Edit under the Actions column to edit album data.
Click on the musician's name to edit musician data.
Data is saved to the backend and can be retrieved or modified easily.

Technologies Used
Backend: Python, Django
Frontend: HTML, CSS
Database: SQLite (default for Django)
Others: Django Model Forms

Installation
Clone the repository:

bash
git clone <repository-url>
cd musicians-directory
Install the dependencies:

bash
pip install -r requirements.txt
Apply migrations:

bash
python manage.py migrate
Run the development server:

bash
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000.

Usage
Add musicians and albums using the provided forms.
View, edit, or delete entries directly from the table.

Future Enhancements
Add user authentication for better access control.
Implement search and filter functionality for musicians and albums.
Enable file uploads for musician or album images.

Prerequisites
Before running this project, ensure you have the following installed on your system:

Python (version 3.8 or later)
Django (version 4.x or later)
pip (Python package installer)
SQLite (default Django database)
A Code Editor or IDE
