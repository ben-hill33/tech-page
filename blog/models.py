from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """ Publish date can be empty and doesnt have to have any characters """
        self.pub_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.approve_comments.filter(approved_comments=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
