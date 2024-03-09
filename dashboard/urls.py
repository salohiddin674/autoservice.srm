from django.urls import path
from . import views

urlpatterns = [
    path("create-employee",views.CreateEmployee.as_view()),
    path("update-employee/",views.UpdateEmployee.as_view()),
    path("delete-employee",views.DeleteEmployee.as_view()),

]