from rest_framework import viewsets, permissions

from .serializers import CompanySerializer, ShipmentSerializer
from .models import Company, Shipment


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class ShipmentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()
