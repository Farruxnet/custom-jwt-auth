from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="DOCUMENTATION",
        description="REST API",
        default_version="1.0.0",
        terms_of_service="ScienTech Solution",
        contact=openapi.Contact(email="admin@gmail.com"),
        license=openapi.License(name="Private"),
    ),
    public=False,
    permission_classes=(AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('users.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),

]
