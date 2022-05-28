from django import forms
from .models import blogpost

class PostForm(forms.ModelForm):
    class Meta:
        model=blogpost
        fields = '__all__'