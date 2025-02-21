from django.db import models

# Create your models here.
from django.db import models

class Submission(models.Model):
    CATEGORY_CHOICES = [
        ('ACADEMIC', 'Academic Research'),
        ('BUSINESS', 'Business Report'),
        ('TECHNICAL', 'Technical Documentation'),
        ('CREATIVE', 'Creative Writing'),
    ]

    content = models.CharField(max_length=200)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='ACADEMIC'
    )
    is_reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content} - {self.get_category_display()}"

    class Meta:
        ordering = ['-created_at']

