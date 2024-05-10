Vendor management system with performace matrix

Vendor management system with performace matrix was created using Django and DjangoREST Framework.This system will handle vendor profiles, track purchase orders and calculate vendor performance metrics.

Prerequisites Python (Version 3), Django, Django REST framework

Dependencies pip install django pip install djangorestframework

Project Structure

VendorMgmt: Django project directory & Django project folder
Vendor:Django app containing API views, serializers and models for Vendor
PurchaseOrder: Django app containing API views, serializers and models for PurchaseOrder
HistoricalPerformance: Django app containing API views, serializers and models for HistoricalPerformance
VendorPerformanceEvaluation: Django app containing API views, serializers and models for VendorPerformanceEvaluation
manage.py: Django management script
requirements.txt: Project dependencies
README.md: Project documentation
Installation

Clone the repository (git clone https://github.com/snownisha/Vendor-Management-System-with-Performance-Metrics.git)
cd VendorMgmt
python manage.py makemigrations
python manage.py migrate
To create super user (python manage.py createsuperuser)
python manage.py runserver
To access django admin panel To access the database (http://127.0.0.1:8000/admin/)

To test API endpoints: Used Curl to test the API endpoints

Eg:

curl http://localhost:8000/api/vendors/
curl -X GET http://localhost:8000/api/purchase_orders/
curl -X POST -d "username=your_superuser_username&password=your_superuser_password" http://localhost:8000/api-token-auth/
