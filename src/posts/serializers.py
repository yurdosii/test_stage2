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
            'title',
            'link',
            'creation_date',
            'upvotes_amount',
            'author_name'
        ]


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for model Comment
    """
    class Meta:
        model = Comment
        fields = [
            'post',
            'author_name',
            'content',
            'creation_date'
        ]
