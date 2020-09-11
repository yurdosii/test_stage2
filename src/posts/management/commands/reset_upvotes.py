"""
Custom django-admin command
"""

from django.core.management.base import BaseCommand

from posts.models import Post  # type: ignore


class Command(BaseCommand):
    """
    Custom django-admin command
    Can be called with 'python manage.py reset_upvotes'
    Command resets upvotes_amount in posts
    Command will be used inside the job that will run once a day
    """

    help = "Reset field 'upvotes_amount' in posts"

    def handle(self, *args, **kwargs) -> None:
        """
        Command handler
        """
        for post in Post.objects.all():
            post.upvotes_amount = 0
            post.save()
