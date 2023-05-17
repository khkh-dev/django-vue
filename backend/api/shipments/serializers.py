from rest_framework import serializers
from .models import Company, Shipment


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'description',
            'country',
            'created_at',
            'updated_at',
        )


class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipment
        fields = (
            'id',
            'title',
            'description',
            'quantity',
            'company',
            'delivery_country',
            'availability',
            'delivery_status',
            'created_at',
            'updated_at',
        )

