from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.


class EventModel(models.Model):
    """
    Event model with fields for title, teaser, creator, image, description,
    date, time, approved status
    """
    title = models.CharField(max_length=250)
    teaser = models.CharField(max_length=300)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='events'
    )
    event_image_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    ticket_price = models.FloatField(default=0)
    event_date = models.DateField()
    event_time = models.TimeField()
    city = models.CharField(max_length=50)
    venue = models.CharField(max_length=100, null=False, blank=False, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


    class Meta:
        ordering = ['event_date']
        # The code below ensures that events can't take place at the same date and time at the same city.
        unique_together = [['event_date', 'event_time', 'venue']]


    def __str__(self):
        return f"Event name: {self.title} held in {self.city} on {self.event_date}"

    
    def get_image(self):
        return self.event_image_url


class BookEventModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    num_of_tickets = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 11)])
    date_booked = models.DateTimeField(auto_now_add=True)