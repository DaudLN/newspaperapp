from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse, reverse_lazy
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.comment[:20]

    def get_absolute_url(self):
        return reverse("article_list")
