"""
Posts API viewsets
"""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # endpoint for upvote
    @action(detail=True, methods=['GET'])
    def upvote_post(self, request, pk=None):
        """
        Endpoint that enables upvoting the post
        Upvoting the post - field 'upvotes_amount' will be increased by one
        """
        post = self.get_object()
        post.upvotes_amount += 1
        post.save()
        return Response({'status': 'post is upvoted'})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
