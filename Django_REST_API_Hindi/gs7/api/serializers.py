from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # This will ensure that name doesn't get updated

    # way 1
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

        # Way 2
        # read_only_fields = ['name']

        # Way 3
        extra_kwargs = {'name': {'read_only': True}}
