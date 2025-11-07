import json
import base64

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print("Пришли данные от SIM800:", data)
        return JsonResponse({"status": "ok", "message": "Данные приняты"})

    elif request.method == 'GET':
        return JsonResponse({"command": True})
