from django.urls import path
from .views import (
    ItemCreateView,ItemListView,ItemDetailView
)

app_name = 'inventory'

urlpatterns = [
    path('',ItemListView.as_view(),name='item-list'),
    path('item_create/',ItemCreateView.as_view(),name='create-item'),
    path('item_detail/',ItemDetailView.as_view(),name='item-detail'),
]
