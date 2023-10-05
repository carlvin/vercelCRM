from django import forms
from .models import Item
# from ckeditor.widgets import CKEditorWidget

class CreateItemForm(forms.ModelForm):
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        model = Item
        
        fields = ("name","model","quantity","price","description")
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'quantity': forms.TextInput(attrs={'class': 'form-input'}),
            'price': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
            # 'description': CKEditorWidget(config_name='awesome_ckeditor'),  # Use CKEditorWidget from ckeditor.widgets

        }
        
        