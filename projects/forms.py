from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'category', 'about', 'text', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5')
