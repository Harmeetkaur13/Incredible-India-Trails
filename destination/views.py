from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .forms import ContactForm, DestinationForm, ImageFormSet, ReviewForm
from .models import Category, Destination, Review


# Create your views here.
class AllDestinations(generic.ListView):
    template_name = "destination/Homepage.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = Destination.objects.filter(is_approved=True)
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
        context['search_query'] = self.request.GET.get('search', '')
        context['category_id'] = self.request.GET.get('category', '')
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
    rc = destination.reviews_destination.filter(is_approved=True).count()
    review_count = rc
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
        {
            "destination": destination,
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
            review.is_approved = False  # Mark as not approved after editing
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating review!')

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
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own reviews!')

    return redirect("view_destination", name=destination.name)


def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            destination = form.save(commit=False)
            destination.added_by = request.user
            destination.save()
            for form in formset:
                if form.cleaned_data.get('image'):
                    image = form.save(commit=False)
                    image.destination = destination
                    image.save()
            if request.user.is_superuser:
                messages.add_message(
                    request, messages.SUCCESS,
                    'Dear Admin, The destination was added successfully.'
                )
            else:
                messages.add_message(
                    request, messages.SUCCESS,
                    'Your destination has been submitted and is awaiting approval.'
                )
            return redirect('home')
    else:
        form = DestinationForm()
        formset = ImageFormSet()

    return render(request, 'destination/add_destination.html',
                           {'form': form, 'formset': formset})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            if request.user.is_authenticated:
                contact.user = request.user
            contact.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your message has been sent successfully. We will get back to '
                'you soon if required after reviewing your message.'
            )
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'destination/contact.html', {'form': form})
