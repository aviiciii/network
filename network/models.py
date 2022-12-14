from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.ManyToManyField("User", blank=True, related_name="user_following")
    following = models.ManyToManyField("User", blank=True, related_name="user_followers")



class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name="liked_posts")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} posted at {self.timestamp}"

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %-d %Y, %-I:%M %p"),
            "user": self.user.username,
            "likes": [user.username for user in self.likes.all()]
        }

    def like_count (self):
        return self.likes.all().count()
