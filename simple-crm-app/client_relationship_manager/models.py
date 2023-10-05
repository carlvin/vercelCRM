from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
# from ckeditor.fields import RichTextField

# Create your models here.

class User(AbstractUser):
    is_organisor = models.BooleanField(_("Organisor"),default=True)
    is_agent = models.BooleanField(_("Agent"),default=False)

class UserProfile(models.Model):
    user = models.OneToOneField("User", verbose_name=_("User Profile"), on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.user.username}'

class Agent(models.Model):
    user=models.OneToOneField("User", verbose_name=_("Agent"), on_delete=models.CASCADE)
    organisation = models.ForeignKey('UserProfile', related_name='agent_organisation', on_delete=models.CASCADE)
    date_created = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    created_by = models.CharField(_("Added by"), max_length=150)
    
    def __str__(self) -> str:
        return f'{self.user.email}'
    
    def get_absolute_url(self):
        return reverse_lazy("agents:detail-agent", kwargs={"pk": self.pk})

class Client(models.Model):
    name = models.CharField(max_length=240)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=240)
    date_created = models.DateTimeField(auto_now_add=True)
    organisation = models.ForeignKey('UserProfile', related_name='client_organisation', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_success_url(self):
        return reverse_lazy("")

    def get_absolute_url(self):
        return reverse_lazy("crm:detail-client", kwargs={"pk": self.pk})
    

class Device(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    serial=models.CharField(_("Serial No"), max_length=50)
    siteName=models.CharField(_("Site "), max_length=50)
    faultTitle=models.CharField(_("Fault Title"), max_length=50)
    faultDescription=models.TextField(_("Fault Description"))
    technician=models.CharField(_("Technician"), max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name} from: {self.siteName}'
    
    def get_success_url(self):
        return reverse_lazy("")
    
    def get_absolute_url(self):
        return reverse_lazy("crm:detail-returned-device", kwargs={"pk": self.pk})
    
    
# class Unotes(models.Model):
#     # name=RichTextField(config_name='awesome_ckeditor')
#     name = models.CharField(_("Name"), max_length=50)
#     description=RichTextField(config_name='awesome_ckeditor')

#     def get_success_url(self):
#         return reverse_lazy("")

#     def __str__(self) -> str:
#         return f'{self.name} '

def post_user_created_signal(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance) 
        
post_save.connect(post_user_created_signal,sender=User)

