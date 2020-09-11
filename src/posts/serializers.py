"""
Posts API serializers
"""

from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for model Post
    """

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "link",
            "creation_date",
            "upvotes_amount",
            "author_name",
        ]


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for model Comment
    """

    class Meta:
        model = Comment
        fields = ["id", "post", "author_name", "content", "creation_date"]
        read_only_fields = ["post"]
