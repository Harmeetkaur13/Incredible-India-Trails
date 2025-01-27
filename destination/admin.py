from django.contrib import admin
from .models import Category, Destination

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
class DestinationAdmin(admin.ModelAdmin):
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

    def get_queryset(self, request):
        """
        Customize the queryset to show only approved destinations for non-superusers. Usefull when users have staff status.
        """
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(is_approved=True)
        return qs
