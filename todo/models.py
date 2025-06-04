from django.db import models

PRIORITY_CHOICES = [
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
]

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title