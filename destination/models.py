from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Category(models.Model):
    """
    Stores a single category entry related to :model:`auth.User`.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Destination(models.Model):
    """
    Stores a single destination entry related to :model:`auth.User`.
    """
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="destinations_category")
    description = models.TextField()
    location = models.CharField(max_length=200)  
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="all_destinations")
    is_approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically approve destinations added by a superuser
        if self.added_by.is_superuser:
            self.is_approved = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} | written by {self.added_by}"

