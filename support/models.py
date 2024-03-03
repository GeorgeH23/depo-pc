from django.db import models


class Contact(models.Model):

    # Choices for the reason of contac
    CONTACT_REASONS = [
        ('', 'Reason of Contact'),
        ('ORDER', 'Order'),
        ('SUGGESTIONS', 'Suggestions'),
        ('OTHER', 'Other'),

    ]

    # Fields for the Contact model
    contact_reason = models.CharField(max_length=24, choices=CONTACT_REASONS)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(max_length=1000)
    date_submmited = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_submmited']

    def __str__(self) -> str:
        return f'Contact {self.name} and message created'
