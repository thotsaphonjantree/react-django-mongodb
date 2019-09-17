from rest_framework_mongoengine import serializers
from project.myserver.models import *


class StudentWriteSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentReadSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1

class MajorSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Major
        fields = '__all__'
