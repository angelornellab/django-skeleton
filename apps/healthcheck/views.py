from django.http import JsonResponse
from datetime import datetime
from django.conf import settings


def healthcheck(request):
    return JsonResponse(
        {
            "service": "Healthcheck",
            "status": "Successful",
            "message": "Service is up and running",
            "manager_url": f"{settings.BASE_URL}/admin",
            "timestamp": str(datetime.now()),
        }
    )
