"""
News API models
"""

from django.db import models


class Post(models.Model):
    """
    Post model class
    """

    title = models.CharField(
        verbose_name="post's title",
        max_length=150,
    )
    link = models.URLField(
        verbose_name="link to post",
    )
    creation_date = models.DateTimeField(
        verbose_name="date when post was created", auto_now_add=True
    )
    upvotes_amount = models.IntegerField(
        verbose_name="number of upvotes on post"
    )
    author_name = models.CharField(
        verbose_name="post author's name", max_length=150
    )

    def __str__(self) -> str:
        return f"Post #{self.id} by {self.author_name} - {self.title}"

    class Meta:
        db_table = "posts"


class Comment(models.Model):
    """
    Comment model class
    Model represents post's comment
    """

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="post, on which comment is written",
        related_name="comments",
    )
    author_name = models.CharField(
        verbose_name="comment author's name", max_length=150
    )
    content = models.TextField(verbose_name="comment content")
    creation_date = models.DateTimeField(
        verbose_name="date when comment was added", auto_now_add=True
    )

    def __str__(self) -> str:
        return f"Comment #{self.id} by {self.author_name} on {self.post.title}"

    class Meta:
        db_table = "comments"
