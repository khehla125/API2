from django.urls import path
from .views import log_data, latest_reading, hourly_readings, daily_readings, device1_readings

urlpatterns = [
    path('datalogger/', log_data),
    path('datalogger/latest/', latest_reading),
    path('datalogger/hourly/', hourly_readings),
    path('datalogger/daily/', daily_readings),
    path('datalogger/device1/', device1_readings),
]
