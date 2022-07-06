from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    # Admin, superuser and normal users with details in user table will be able to access
    # permission_classes = [IsAuthenticated]

    #Only Admins can access the API -> is_staff should be true
    permission_classes = [IsAdminUser]


