from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .models import Customers

class CustomersViewSet(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'customers/index.html'
    
    """ A view to return the index page """
    def get(self, request):
        queryset = Customers.objects.all()
        return Response({'customers': queryset})
    
    def get_queryset(self):
        customers = Customers.objects.all()
        return customers