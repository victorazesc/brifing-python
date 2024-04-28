from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Vendor, Retailer, Briefing
from .serializers import CategorySerializer, VendorSerializer, RetailerSerializer, BriefingSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class RetailerListCreateView(generics.ListCreateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer

class RetailerRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer

class BriefingListCreateView(generics.ListCreateAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer

class BriefingRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer
