from django.db import models
from django.utils.text import slugify
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    # image
    # author

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class User(models.Model):
    name = models.CharField(max_length=255)
    place = models.TextField()

    def __str__(self):
        return self.name
