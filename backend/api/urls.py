from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

from django.contrib import admin
from django.urls import path, include

from api.shipments import views


app_name = "shipments_app"

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet, basename="companies")
router.register(r'shipments', views.ShipmentViewSet, basename="shipments")


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Shipments API",
        default_version='1.0',
        description="REST API documentation",
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    path('api/', include(router.urls), name="api"),
]
