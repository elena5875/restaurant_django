#models.py

from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

class Reservation(models.Model):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    CANCELED = 'canceled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (CANCELED, 'Canceled'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"

class Review(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    review_text = models.TextField()
    is_approved = models.BooleanField(default=False)
    is_posted = models.BooleanField(default=False)  # Add this field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment on {self.review.name}'

