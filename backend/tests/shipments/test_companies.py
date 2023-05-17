from rest_framework import status
from rest_framework.test import APITestCase
from api.shipments.models import Company


class CompanyAPITestCase(APITestCase):

    def setUp(self) -> None:
        data = {"name": "PolApps", "country": "PL"}
        self.company = Company.objects.create(**data)

        self.content_type = "application/json"
        self.url = "/api/companies/"

    def test_create_company(self):
        """
        Ensure we can create new company.
        """

        data = '{"name": "DabApps", "country": "AF"}'
        response = self.client.post(path=self.url, data=data, content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 2)
        self.assertEqual(Company.objects.last().name, "DabApps")

    def test_get_list_of_companies(self):
        """
        Ensure we can get list of companies.
        """
        response = self.client.get(path=self.url, content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.first().name, "PolApps")

    def test_get_company_by_id(self):
        """
        Ensure we can retrieve a company.
        """
        response = self.client.get(f"{self.url}{self.company.id}/", content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.first().name, "PolApps")

    def test_update_company(self):
        """
        Ensure we can update a company.
        """
        data = '{"name": "PolAppsChanged", "country": "AF"}'
        response = self.client.put(f"{self.url}{self.company.id}/", data=data, content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.first().name, "PolAppsChanged")

    def test_delete_company(self):
        """
        Ensure we can delete a company.
        """
        response = self.client.delete(f"{self.url}{self.company.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Company.objects.count(), 0)

    def tearDown(self) -> None:
        Company.objects.all().delete()
