from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    class Meta:
        db_table = "post"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    title = models.CharField(verbose_name="Title", max_length=80, null=False)
    published = models.DateTimeField(verbose_name="Published", default=datetime.now)
    image = models.ImageField(verbose_name="Image", upload_to='media/', blank=True)
    summary = models.CharField(verbose_name="Summary", max_length=500)
    body = models.TextField(verbose_name="Body")

    def __str__(self):
        return self.title

    def brief_body(self):
        return self.body[:25]
