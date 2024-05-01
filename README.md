Vendor management system with performace matrix using Django and DjangoREST Framework.This system will handle vendor profiles, track purchase orders and 
calculate vendor performance metrics.

**Prerequisites**
Python (Version 3), Django, Django REST framework

**Dependencies**
pip install django
pip install djangorestframework

**Project Structure**
* VendorMgmt: Django project directory & Django project folder
* Vendor:Django app containing API views, serializers and models for Vendor
* PurchaseOrder: Django app containing API views, serializers and models for PurchaseOrder
* HistoricalPerformance: Django app containing API views, serializers and models for HistoricalPerformance
* VendorPerformanceEvaluation: Django app containing API views, serializers and models for VendorPerformanceEvaluation
* manage.py: Django management script
* requirements.txt: Project dependencies
* README.md: Project documentation

**Installation**
  1. Clone the repository (git clone https://github.com/snownisha/Vendor-Management-System-with-Performance-Metrics.git)
  2. cd VendorMgmt
  3. python manage.py makemigrations
  4. python manage.py migrate
  5. To create super user (python manage.py createsuperuser)
  6. python manage.py runserver

**To access django admin panel**
To access the database (http://127.0.0.1:8000/admin/) 

**To test API endpoints:**
Used Curl to test the API endpoints

**Eg:**
1) curl http://localhost:8000/api/vendors/
2) curl -X GET http://localhost:8000/api/purchase_orders/
3) curl -X POST -d "username=your_superuser_username&password=your_superuser_password" http://localhost:8000/api-token-auth/
