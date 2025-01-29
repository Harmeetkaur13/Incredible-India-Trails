from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Destination,Review,Image

class ImageInline(admin.TabularInline):
    """
    Inline admin descriptor for Image model
    which acts a bit like a singleton.
    """
    model = Image
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin view for Category model.
    Displays id, name, and description in the list view.
    Allows searching by name and orders by name by default.
    """
    list_display = ("id", "name", "description")
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Destination)
class DestinationAdmin(SummernoteModelAdmin):
    """
    Admin view for Destination model.
    Displays id, name, category, added_by, is_approved, status, and created_at in the list view.
    Allows filtering by is_approved, status, and category.
    Enables search functionality for name, description, location, and added_by username.
    Orders by created_at in descending order by default.
    Allows inline editing of is_approved and status fields.
    Adds a date hierarchy for filtering by creation date.
    Allows selecting users via a search pop-up for added_by field.
    Customizes the queryset to show only approved destinations for non-superusers.
    """
    list_display = ("id", "name", "category", "added_by", "is_approved", "status", "created_at")
    list_filter = ("is_approved", "status", "category")
    search_fields = ("name", "description", "location", "added_by__username")
    ordering = ("-created_at",)
    list_editable = ("is_approved", "status")
    date_hierarchy = "created_at"
    raw_id_fields = ("added_by",)
    inlines = [ImageInline]
    
    def get_queryset(self, request):
        """
        Customize the queryset to show only approved destinations for non-superusers. Usefull when users have staff status.
        """
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(is_approved=True)
        return qs

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin interface definition for the Review model.
    This class customizes the Django admin interface for the Review model, providing
    various configurations for displaying, filtering, searching, and ordering reviews.
    Attributes:
        list_display (tuple): Specifies the fields to be displayed in the list view.
        list_filter (tuple): Specifies the fields to be used for filtering the list view.
        search_fields (tuple): Specifies the fields to be used for searching in the list view.
        ordering (tuple): Specifies the default ordering of the list view.
        list_editable (tuple): Specifies the fields that can be edited directly in the list view.
    Methods:
    rating_display(obj): Returns a string representation of the rating using stars.
    """
    list_display = ("destination", "user", "rating", "comment", "is_approved", "created_at")
    list_filter = ("is_approved", "rating", "destination")
    search_fields = ("destination__name", "user__username", "comment")
    ordering = ("-created_at",)
    list_editable = ("is_approved",)

    def rating_display(self, obj):
        return "★" * obj.rating + "☆" * (5 - obj.rating)
    rating_display.short_description = 'Rating'
    list_display = ("destination", "user", "rating_display", "comment", "is_approved", "created_at")