from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
# age model for storing multiple images for a destination
class Image(models.Model):
    """
    Model representing an image associated with a specific destination.
        destination (ForeignKey): Foreign key to the Destination model, representing the destination this image is associated with.
        image (CloudinaryField): Field to store the image using Cloudinary.
       
        __str__(): Returns a string representation of the image, including its ID and the name of the associated destination.
    Note:
        This model allows multiple images to be associated with a single destination.
    
    """
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE, related_name='images_destination')
    image = CloudinaryField('image')
    caption = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} for {self.destination.name}"
    
# Category model for categorizing destinations
class Category(models.Model):
    """
    Stores a single category entry related to :model:`auth.User`.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Destination model to store information about places
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
    class Meta:
        ordering = ["-created_at"]

# Review model to store reviews for destinations
RATING_CHOICES = [(i, f"{i} Star") for i in range(0, 6)]  # Rating choices from 1 to 5 stars

class Review(models.Model):
    """
    Stores a review for a destination by a user.
    Related to :model:`destination.Destination`.
    """
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="reviews_destination")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(choices=RATING_CHOICES, default=0, null=True)
    comment = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.destination.name}: '{self.comment}' by {self.user.username}"

    class Meta:
        ordering = ['-created_at']  # Show most recent reviews first
