from django.shortcuts import render
from rest_framework_mongoengine import viewsets as meviewsets
from project.myserver.serializers import *
from project.myserver.models import *


class StudentViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Student.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST' or method == 'DELETE':
            return StudentWriteSerializer
        else:
            return StudentReadSerializer


class MajorViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Major.objects.all()
    serializer_class = MajorSerializer

class StudentByMajorViewSet(meviewsets.ModelViewSet):
    serializer_class = StudentReadSerializer
    def get_queryset(self):
        mid = self.kwargs['major_id']
        queryset =Student.objects.filter(Major=mid)
        return queryset





