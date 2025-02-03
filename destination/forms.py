from .models import Review
from django import forms
from django.core.exceptions import ValidationError


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment',)

