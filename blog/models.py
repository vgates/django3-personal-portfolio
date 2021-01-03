from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date = models.DateField()

    # to display the title in admin page else would see as objects
    def __str__(self):
        return self.title
