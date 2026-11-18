EMPLOYEE MANAGEMENT API - PYCHARM PROJECT

OPEN IN PYCHARM
1. Extract employee_management_pycharm.zip.
2. In PyCharm choose File > Open and select the extracted employee_management_pycharm folder.
3. Create/select a Python virtual environment.
4. Open the PyCharm terminal and run:
      pip install -r requirements.txt
      python manage.py makemigrations
      python manage.py migrate
      python manage.py createsuperuser
      python manage.py runserver
5. Open http://127.0.0.1:8000/

API ENDPOINTS
POST   /api/register/       Register a normal user
POST   /api/login/          Obtain a token
GET    /api/employees/      List employees (authenticated)
POST   /api/employees/      Create employee (superuser only)
GET    /api/employees/1/    Retrieve employee (authenticated)
PUT    /api/employees/1/    Update employee (superuser only)
PATCH  /api/employees/1/    Partially update employee (superuser only)
DELETE /api/employees/1/    Delete employee (superuser only)

AUTHENTICATION
After login, use this header for protected endpoints:
Authorization: Token YOUR_TOKEN

IMAGE UPLOAD
Use multipart/form-data in Postman for employee create/update requests
that include an image. Field names: name, employee_id, department,
designation, salary, image.

NOTES
- Registration creates normal users, not superusers.
- Create a superuser using createsuperuser.
- Employee names are converted to uppercase by the pre_save signal.
