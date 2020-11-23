from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=120)
    price = models.CharField(max_length=120)
    image_url = models.URLField()
    detail_url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kitablar'
        verbose_name_plural = "Kitablar"
        ordering = ['-id']