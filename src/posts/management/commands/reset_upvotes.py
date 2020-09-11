"""
Custom django-admin command
"""

from django.core.management.base import BaseCommand

from posts.models import Post


class Command(BaseCommand):
    help = "Reset field 'upvotes_amount' in posts"

    def handle(self, *args, **kwargs):
        for post in Post.objects.all():
            post.upvotes_amount = 0
            post.save()
