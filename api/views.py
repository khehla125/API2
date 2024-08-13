from django.http import JsonResponse
from .models import DataLogger
import json
from django.utils import timezone
from django.db.models import Q
from datetime import timedelta
from django.shortcuts import get_object_or_404

def log_data(request):
    device = request.GET.get('device')
    temperature = request.GET.get('temperature')
    turbidity = request.GET.get('turbidity')
    conductivity = request.GET.get('cond')
    longitude = request.GET.get('lng')
    latitude = request.GET.get('lat')

    # Create a new DataLogger object and save it to the database
    data_logger = DataLogger.objects.create(
        device=device,
        temperature=temperature,
        turbidity=turbidity,
        conductivity=conductivity,
        longitude=longitude,
        latitude=latitude
    )

    # Prepare the data for JSON response
    data = {
        "device": data_logger.device,
        "temperature": data_logger.temperature,
        "turbidity": data_logger.turbidity,
        "conductivity": data_logger.conductivity,
        "longitude": data_logger.longitude,
        "latitude": data_logger.latitude,
        "timestamp": data_logger.timestamp,
    }

    # Return a JSON response
    return JsonResponse(data)
# View to get the latest reading
def latest_reading(request):
    latest = DataLogger.objects.latest('timestamp')
    data = {
        "device": latest.device,
        "temperature": latest.temperature,
        "turbidity": latest.turbidity,
        "conductivity": latest.conductivity,
        "longitude": latest.longitude,
        "latitude": latest.latitude,
        "timestamp": latest.timestamp,
    }
    return JsonResponse(data)

# View to get readings from the last hour
def hourly_readings(request):
    one_hour_ago = timezone.now() - timedelta(hours=1)
    readings = DataLogger.objects.filter(timestamp__gte=one_hour_ago)
    data = [{"device": r.device, "temperature": r.temperature, "turbidity": r.turbidity, "conductivity": r.conductivity, "longitude": r.longitude, "latitude": r.latitude, "timestamp": r.timestamp} for r in readings]
    return JsonResponse(data, safe=False)

# View to get today's readings
def daily_readings(request):
    today = timezone.now().date()
    readings = DataLogger.objects.filter(timestamp__date=today)
    data = [{"device": r.device, "temperature": r.temperature, "turbidity": r.turbidity, "conductivity": r.conductivity, "longitude": r.longitude, "latitude": r.latitude, "timestamp": r.timestamp} for r in readings]
    return JsonResponse(data, safe=False)

# View to get all readings for device1
def device1_readings(request):
    readings = DataLogger.objects.filter(device="device1")
    data = [{"device": r.device, "temperature": r.temperature, "turbidity": r.turbidity, "conductivity": r.conductivity, "longitude": r.longitude, "latitude": r.latitude, "timestamp": r.timestamp} for r in readings]
    return JsonResponse(data, safe=False)
