import io

from django.shortcuts import render
import json, io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)

        # Converts JSON into Python data
        python_data = JSONParser().parse(stream)

        # Converting python data into complex data
        serializer = StudentSerializer(data = python_data)

        if serializer.is_valid():
            serializer.save()
            result = {'msg': 'Data Created'}
            jsonData = JSONRenderer().render(result)
            return HttpResponse(jsonData, content_type='application/json')

        jsonData = JSONRenderer().render(serializer.errors)
        return HttpResponse(jsonData, content_type='application/json')
