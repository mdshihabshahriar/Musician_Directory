# Musicians Directory

## Overview

A web application built using Python, Django, HTML, and CSS that allows users to manage musicians and their albums efficiently.

## Features

### Musician Management
- Create, view, edit, and delete musician details.
- Fields include:
  - First Name
  - Last Name
  - Email
  - Phone Number
  - Instrument Type

### Album Management
- Add, view, edit, and delete album details.
- Fields include:
  - Album Name
  - Rating (1–5)
  - Release Date
- Each album is associated with a musician (one-to-many relationship).

### User-Friendly Interface
- Display musicians and albums in a tabular format.
- Edit musician data by clicking the musician's name.
- Edit album data using the Edit button in the actions column.

## Instructions
1. Click **Edit** under the Actions column to edit album data.
2. Click on the musician's name to edit musician data.
3. Data is saved to the backend and can be retrieved or modified easily.

## Technologies Used
- **Backend**: Python, Django
- **Frontend**: HTML, CSS
- **Database**: SQLite (default for Django)
- **Others**: Django Model Forms

## Usage

1. Add musicians and albums using the provided forms.
2. View, edit, or delete entries directly from the table.

---

## Future Enhancements

1. Add user authentication for better access control.
2. Implement search and filter functionality for musicians and albums.
3. Enable file uploads for musician or album images.

---

## Prerequisites

Before running this project, ensure you have the following installed on your system:

1. **Python** (version 3.8 or later)
2. **Django** (version 4.x or later)
3. **pip** (Python package installer)
4. **SQLite** (default Django database)
5. **A Code Editor or IDE**
