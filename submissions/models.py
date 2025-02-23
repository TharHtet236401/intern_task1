from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models

class Submission(models.Model):
    CATEGORY_CHOICES = [
        ('TEXT', 'Text'),
        ('IMAGE_URL', 'Image URL'),
    ]

    content = models.CharField(max_length=200)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='TEXT'
    )
    is_reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content} - {self.get_category_display()}"

    class Meta:
        ordering = ['-created_at']

