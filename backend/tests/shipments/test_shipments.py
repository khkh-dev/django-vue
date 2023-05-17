import json

from rest_framework import status
from rest_framework.test import APITestCase
from api.shipments.models import Company, Shipment


class ShipmentAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.company = Company.objects.create(name="HRY", country="BY")
        data = {
            "title": "Microwave",
            "description": "lorem ipsum",
            "company_owner": self.company,
            "company_sender": self.company,
            "country_sender": "BY",
            "country_recipient": "BY",
            "availability": "AVAILABLE",
            "delivery_status": 0,
        }
        self.shipment = Shipment.objects.create(**data)

        self.content_type = "application/json"
        self.url = "/api/shipments/"

    def test_create_shipment(self):
        """
        Ensure we can create new shipment..
        """
        data = json.dumps({
            "title": "Microwave M10",
            "description": "lorem ipsum",
            "company_owner": f"{self.company.id}",
            "company_sender": f"{self.company.id}",
            "country_sender": "BY",
            "country_recipient": "BS",
            "availability": "AVAILABLE",
            "delivery_status": 0
        })
        response = self.client.post(path=self.url, data=data, content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shipment.objects.count(), 2)
        self.assertEqual(Shipment.objects.last().title, "Microwave M10")

    def test_get_list_of_shipments(self):
        """
        Ensure we can get list of shipments.
        """
        response = self.client.get(path=self.url, content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Shipment.objects.count(), 1)
        self.assertEqual(Shipment.objects.first().title, "Microwave")

    def test_get_shipment_by_id(self):
        """
        Ensure we can retrieve a shipment.
        """
        response = self.client.get(f"{self.url}{self.shipment.id}/", content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Shipment.objects.count(), 1)
        self.assertEqual(Shipment.objects.first().title, "Microwave")

    def test_update_shipment(self):
        """
        Ensure we can update a shipment.
        """
        data = json.dumps({
            "title": "Microwave M10 Changed",
            "description": "lorem ipsum",
            "company_owner": f"{self.company.id}",
            "company_sender": f"{self.company.id}",
            "country_sender": "BY",
            "country_recipient": "BS",
            "availability": "AVAILABLE",
            "delivery_status": 0
        })
        response = self.client.put(f"{self.url}{self.shipment.id}/", data=data, content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Shipment.objects.count(), 1)
        self.assertEqual(Shipment.objects.first().title, "Microwave M10 Changed")

    def test_delete_shipment(self):
        """
        Ensure we can delete a shipment.
        """
        response = self.client.delete(f"{self.url}{self.shipment.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Shipment.objects.count(), 0)

    def tearDown(self) -> None:
        Shipment.objects.all().delete()
