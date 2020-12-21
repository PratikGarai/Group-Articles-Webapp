from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

import misaka

from groups.models import Group

User = get_user_model()

class Post(models.Model):

    user = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("post:single", kwargs={"username": self.self.user.username,
                                              "pk": self.pk})
    
    class Meta:
        unique_together = ("user", "message")
        ordering = ["-created_at"]