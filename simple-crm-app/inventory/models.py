from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from client_relationship_manager.models import UserProfile

# Create your models here.
class Item(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    model = models.CharField(_("Model"), max_length=50)
    serial = models.CharField(_("Serial"), max_length=50)
    description = models.TextField(_("Description"))
    quantity = models.PositiveIntegerField(_("Quantity"))
    price = models.DecimalField(_("Price"), max_digits=5, decimal_places=2)
    organisation = models.ForeignKey(UserProfile, related_name='item_organisation', on_delete=models.CASCADE)
    date_created = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    created_by = models.CharField(_("Added by"), max_length=150)
    
    # last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    # modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='modified_items')
    
    # def save(self, *args, **kwargs):
    #     # Set the modified_by field to the current user (if available)
    #     user = kwargs.pop('user', None)
    #     if user:
    #         self.modified_by = user
        
    #     super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse_lazy("inventory:item-detail", kwargs={"pk": self.pk})
    