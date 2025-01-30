from django.shortcuts import render
from django.views import generic
from .models import Destination

# Create your views here.
class AllDestinations(generic.ListView):
    queryset = Destination.objects.all()
    template_name = "destination/Homepage.html"
    paginate_by = 6

