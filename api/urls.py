from django.urls import path
from .views import CategoryListCreateView, CategoryRetrieveUpdateView, \
                   VendorListCreateView, VendorRetrieveUpdateView, \
                   RetailerListCreateView, RetailerRetrieveUpdateView, \
                   BriefingListCreateView, BriefingRetrieveUpdateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('category/<int:pk>/', CategoryRetrieveUpdateView.as_view(), name='category-retrieve-update'),
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendor/<int:pk>/', VendorRetrieveUpdateView.as_view(), name='vendor-retrieve-update'),
    path('retailers/', RetailerListCreateView.as_view(), name='retailer-list-create'),
    path('retailer/<int:pk>/', RetailerRetrieveUpdateView.as_view(), name='retailer-retrieve-update'),
    path('briefings/', BriefingListCreateView.as_view(), name='briefing-list-create'),
    path('briefing/<int:pk>/', BriefingRetrieveUpdateView.as_view(), name='briefing-retrieve-update'),
]
