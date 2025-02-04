from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.db.models import Q
from .models import Category,Destination, Review
from .forms import ReviewForm
from django.contrib import messages

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
    reviews = destination.reviews_destination.all().order_by("-created_at")
    review_count = destination.reviews_destination.filter(is_approved=True).count()
    Review_form = ReviewForm()
    if request.method == "POST":
        Review_form = ReviewForm(data=request.POST)
        if Review_form.is_valid():
            Review = Review_form.save(commit=False)
            Review.user = request.user
            Review.destination = destination
            Review.rating = request.POST.get('rating')
            Review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your review is submitted and awaiting for the approval.'
            )
            return redirect("view_destination", name=destination.name)
   

    return render(
        request,
        "destination/view_destination.html",
        {"destination": destination,
        "reviews": reviews,
        "review_count": review_count,
        "Review_form": Review_form,
        },
    )

def review_edit(request, name, review_id):
    """
    View to edit a review
    """
    queryset = Destination.objects.filter(status=1)
    destination = get_object_or_404(queryset, name=name)
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, instance=review)
        if review_form.is_valid() and review.user == request.user:
            review = review_form.save(commit=False)
            review.destination = destination
            review.rating = request.POST.get('rating')
            if review.rating is None:
                messages.add_message(
                    request, messages.ERROR,
                    'Please select a rating before submitting your review.'
                )
                return redirect("view_destination", name=destination.name)
            review.is_approved = False  # Mark as not approved after editing
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    
    return redirect("view_destination", name=destination.name)

def review_delete(request, name, review_id):
    """
    View to delete a review
    """
    queryset = Destination.objects.filter(status=1)
    destination = get_object_or_404(queryset, name=name)
    review = get_object_or_404(Review, pk=review_id)

    if review.user == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return redirect("view_destination", name=destination.name)