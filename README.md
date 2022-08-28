# Attendance


## Introduction

- this project is used to track the attendance of the employees of the company.
- As a new employee, I can register to the system & start using its functionality.
- Only signed-in employees can log their attendance.
- As an employee, I can log my new attendance and list the previous attendance records.
- Each employee lists attendance records related to himself only.
- Employee can’t log attendance for another employee.
- Each attendance record shall have check-in & check-out times.
- Attendance validations:
    - Check-out can't be before check-in.
    - you can’t log your check-out before logging the check-in first.
    - check-out time must be always bigger than check-in time.
    - User can't create attendance record for the same interval.

## How to Install the Project

- Download the project from [GitHub]
- Create virtual environment and install the dependencies
- Run this command in terminal to create the virtual environment with the dependencies: `python3 -m venv venv`
    ```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

- Run this commands in terminal to migrate the models to the database: 
    ```
    python manage.py makemigraions
    python manage.py db migrate
    ```
- Run this command in terminal ro create admin user account: `python3 manage.py createsuperuser`
- Run this command in terminal to run the server: `python3 manage.py runserver`
- Open the browser and got to the url: `http://localhost:8000/register` to register the employees.
- Open the browser and got to the url: `http://localhost:8000/login` to login to the system.
- Open the browser and go to http://localhost:8000/attendance/check_in and check_in the attendance of the employee
- Open the browser and go to http://localhost:8000/attendance/check_out and check_out the attendance of the employee
- Open the browser and go to http://localhost:8000/attendance/dashboard to to see the attendances of the yours.
- Open the browser and go to http://localhost:8000/admin/ to see the admin dashboard and sign in with the superuser account.
- Open the postman application or browser and go to http://localhost:8000/api/attendances/ to see the api endpoint which uses to list and create the attendances.
- Open the postman application or browser and go to http://localhost:8000/api/attendances/<int:pk>/ to see the api endpoint which uses to get the attendance by id.
- Open the postman application or browser and go to http://localhost:8000/api/attendances/<int:pk>/update/ to see the api endpoint which uses to update the attendance by id.
- Open the postman application or browser and go to http://localhost:8000/api/attendances/<int:pk>/delete/ to see the api endpoint which uses to delete the attendance by id.


## Prerequisite

1. asgiref==3.5.2
1. backports.zoneinfo==0.2.1
1. Django==4.0.5
1. djangorestframework==3.13.1
1. pytz==2022.1
1. sqlparse==0.4.2
1. tzdata==2022.1

## Author

- (ahmedlotfe132@gmail.com)
