from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
from .models import Category,Destination

# Create your views here.
class AllDestinations(generic.ListView):
    template_name = "destination/Homepage.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = Destination.objects.all()
        search_query = self.request.GET.get('search', '')
        category_id = self.request.GET.get('category', '')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(category__name__icontains=search_query) |
                Q(location__icontains=search_query) |
                Q(added_by__username__icontains=search_query)
            )
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

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
