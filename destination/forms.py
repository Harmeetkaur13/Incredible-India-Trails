from .models import Review
from django import forms
from django.core.exceptions import ValidationError
from .models import Destination,Image


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment',)
class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'category', 'description', 'location']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

ImageFormSet = forms.inlineformset_factory(Destination, Image, form=ImageForm, extra=3, can_delete=False)        

