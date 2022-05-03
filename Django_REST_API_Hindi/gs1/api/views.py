from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


# Create your views here.

# Function Based View
def student_detail(request, pk):
    # To get one single model object
    stu = Student.objects.get(id=pk)
    # print(stu)
    serializer = StudentSerializer(stu)
    # print(serializer, serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')

    # Set safe = False if the returned result is not a dictionary but below data is already dictionary
    return JsonResponse(serializer.data)


# Function based for query set for getting all Student data
def student_list(request):
    # To get one single model object
    stu = Student.objects.all()
    # print(stu)
    serializer = StudentSerializer(stu, many=True)
    # print(serializer, serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')

    # Set safe = False if the returned result is not a dictionary
    return JsonResponse(serializer.data, safe=False)
