# Student Records Management System

This is a Django web application for managing student records, allowing users to add, view, and delete student information.

## Features

- Add student records with name, age, and bio.
- View all student records in a table format.
- Delete student records.
- Admin panel for managing student records.

## Requirements

- Python 3.6 or higher
- MySQL server
- Django 5.1 or higher
- mysqlclient library

## Setup Instructions for Windows

### 1. Install MySQL

1. Download the MySQL Installer from the [official MySQL website](https://dev.mysql.com/downloads/mysql/).
2. Run the installer and select "MySQL Server".
3. Follow the installation wizard and set a root password. Note down this password.
4. Complete the installation.

### 2. Create a MySQL Database

#### 1. Open the MySQL Command Line Client and log in with the root user
   
#### 2. Create a new database:
    CREATE DATABASE student_records CHARACTER SET UTF8;

#### 3. Create a MySQL user and grant privileges:
    CREATE USER 'myprojectuser'@'localhost' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON student_records.* TO 'myprojectuser'@'localhost';
    FLUSH PRIVILEGES;

#### 4. Clone the Repository:
    git clone https://github.com/your-username/student-records.git
    cd student-records

#### 5.Create a Virtual Environment:
    python -m venv myenv
    myenv\Scripts\activate

#### 6.Install Dependencies
    pip install -r requirements.txt

#### 7.Update Database Configuration
    Open the student_project/settings.py file and update the DATABASES section::

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'student_records',  # Your database name
            'USER': 'myprojectuser',     # Your MySQL username
            'PASSWORD': 'password',       # Your MySQL password
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

#### 8. Run Migrations
    python manage.py makemigrations
    python manage.py migrate

#### 9. Create a Superuser
    python manage.py createsuperuser

#### 10. Run the Development Server
    python manage.py runserver


### Access the Application
#### Open your web browser and visit:

    Home Page: http://127.0.0.1:8000/
    Admin Panel: http://127.0.0.1:8000/admin/



