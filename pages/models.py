from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=60, blank=True)
    message = models.TextField(max_length=300, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
