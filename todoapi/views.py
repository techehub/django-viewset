from django.shortcuts import render
from . models import Task
from .serializer import ToDoSerializer
from  rest_framework import viewsets
# Create your views here.

class ToDoView (viewsets.ModelViewSet):
    serializer_class = ToDoSerializer  # add this
    queryset = Task.objects.all()
