from django.urls import path
from . import views

urlpatterns = [
    path("get-user",views.get_user),
    path("get-employee",views.get_employee),
    path("get-cassa",views.get_cassa),
    path("get-order",views.get_order),
    path("get-payment",views.get_payment),
    path("get-report",views.get_report),
]