from django.shortcuts import render
from rest_framework import viewsets
from RK2_app.models import OperatingSystem, Computer
from RK2_app.serializers import OperatingSystemSerializer, ComputerSerializer

def index(request):
    return render(request, 'index.html')


class OperatingSystemViewSet(viewsets.ModelViewSet):
    queryset = OperatingSystem.objects.all().order_by("model")
    serializer_class = OperatingSystemSerializer


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all().order_by("model")
    serializer_class = ComputerSerializer


def report(request):
    return render(request, 'report.html', {'data':{'computer':Computer.objects.select_related('os')}})

