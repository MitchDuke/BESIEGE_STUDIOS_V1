from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='gallery/images/')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
