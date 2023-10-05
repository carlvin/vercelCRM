from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.forms.models import BaseModelForm
from .forms import CreateItemForm
from django.views import generic
from django.http import HttpResponse
from .models import Item
from django.contrib import messages

# Create your views here.
class ItemListView(generic.ListView):
    template_name = "item_list.html"
    context_object_name = "items"
    
    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        queryset = Item.objects.filter(organisation=user.userprofile)
        return queryset
    
    
class ItemCreateView(generic.CreateView):
    template_name = "item_create.html"
    form_class = CreateItemForm
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form = form.save(commit=False)
        form.organisation = self.request.user.userprofile
        form.save()
        return super(ItemCreateView,self).form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request,"Item Created")
        return reverse_lazy("inventory:item-list")
    
class ItemDetailView(generic.DetailView):
    template_name = None
    context_object_name = "items"
    
    def get_queryset(self) -> QuerySet[Any]:
       user = self.request.user
       queryset = Item.objects.filter(organisation=user.userprofile)
       return queryset
    
    
     