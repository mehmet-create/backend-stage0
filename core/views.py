from django.shortcuts import render
from django.http import JsonResponse
import requests
from datetime import datetime, timezone

# Create your views here.

def me(request):
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        data = response.json()
        cat_fact = data.get("fact", "Cats are mysterious creatures!")
    except Exception:
        cat_fact = "Unable to fetch cat fact right now."

    timestamp = datetime.now(timezone.utc).isoformat()

    data = {
        "status": "success",
        "user": {
            "email": "your.email@example.com",
            "name": "Your Full Name",
            "stack": "Python/Django"
        },
        "timestamp": timestamp,
        "fact": cat_fact
    }
    return JsonResponse(data)