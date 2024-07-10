from django.db import models

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
