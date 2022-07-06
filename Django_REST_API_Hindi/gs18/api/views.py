from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

