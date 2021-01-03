from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    # to display the title in admin page else would see as objects
    def __str__(self):
        return self.title
