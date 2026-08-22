# ToDo List

A simple ToDo List web application built with Django.

## Features

- Create, update and delete tasks
- Mark tasks as completed and undo completion
- Optional task deadlines
- Create, update and delete tags
- Assign multiple tags to tasks
- Tasks sorted by completion status and creation date
- Responsive sidebar navigation

## Technologies

- Python
- Django
- Bootstrap 5
- SQLite
- Flake8

## Installation

Clone the repository and enter the project directory:

```bash

git clone <https://github.com/Qbaldo/ToDoList.git>
cd ToDoList

```

# Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate

# Install dependencies:

pip install -r requirements.txt

# Run migrations:

python manage.py migrate

# Start the development server:

python manage.py runserver

# The application will be available at:

http://127.0.0.1:8000/

# Run the automated tests with:

python manage.py test