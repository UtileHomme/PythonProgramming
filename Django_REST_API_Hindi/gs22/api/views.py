from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions\
    ,DjangoModelPermissionsOrAnonReadOnly
from .custom_permissions import MyPermission

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # Admin, superuser and normal users with details in user table will be able to access
    # permission_classes = [IsAuthenticated]

    #Only Admins can access the API -> is_staff should be true
    # permission_classes = [IsAdminUser]

    # Only retrieve is allowed for unauthenticated users
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # This allows us to give a particular some permissions
    # eg - for a particular user we can configure permissions for post, put , delete in the admin console
    # permission_classes = [DjangoModelPermissions]

    # This allows us to give a particular some permissions
    # eg - for a particular user we can configure permissions for post, put , delete in the admin console
    # But this will allow unauthenticated users to also retrieve data
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

#     Custom permission
    permission_classes = [MyPermission]



