import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField


STATUS_CHOICES = (
    ("CREATED", "created"),
    ("RECEIVED", "information received"),
    ("IN QUEUE", "in queue"),
    ("IN TRANSIT", "in transit"),
    ("PICKUP", "available for pickup"),
    ("DELIVERED", "delivered"),
    ("CANCELED", "canceled"),
)

AVAILABILITY_CHOICES = (
    ("AVAILABLE", "available"),
    ("NOT AVAILABLE", "not available"),
)


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True)
    country = CountryField(default="UK", null=False, unique=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name


class Shipment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, blank=True)
    quantity = models.IntegerField(default=1, validators=[MaxValueValidator(1000), MinValueValidator(1)])
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companies')
    delivery_country = CountryField(default="PL", null=False, unique=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default="AVAILABLE")
    delivery_status = models.CharField(max_length=40, choices=STATUS_CHOICES, default="CREATED")

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title
