from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('customers', views.CustomersViewSet, basename='customers')

urlpatterns = [
    path('', views.CustomersViewSet.as_view(), name='customers'),
]

urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)