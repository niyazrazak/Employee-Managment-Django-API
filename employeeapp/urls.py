from django.urls import re_path as url
from employeeapp import views

urlpatterns = [
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),
]