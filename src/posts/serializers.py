"""
News API serializers
"""

from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for model 'Post'
    """

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for model 'Comment'
    """

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["post"]
