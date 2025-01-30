from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Category,Destination

# Create your views here.
class AllDestinations(generic.ListView):
    queryset = Destination.objects.all()
    template_name = "destination/Homepage.html"
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

def destination_detail(request, name):
    """
    Display an individual :model:`destination.Destination`.

    **Context**

    ``post``
        An instance of :model:`destination.Destination`.

    **Template:**

    :template:`destination/view_destination.html`
    """

    queryset = Destination.objects.filter(status=1)
    destination = get_object_or_404(queryset, name=name)

    return render(
        request,
        "destination/view_destination.html",
        {"destination": destination},
    )
def filter_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    destinations = Destination.objects.filter(category=category)
    return render(request, "filter_by_category.html", {
        "category": category,
        "destinations": destinations
    })