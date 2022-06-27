from rest_framework import serializers
from .models import Student


# Validators
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with R')

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

    # Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat is full')
        return value

    #  Object level validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')

        if name.lower() == 'rohit' and city.lower() != 'ranchi':
            raise serializers.ValidationError('City must be ranchi')

        return data

