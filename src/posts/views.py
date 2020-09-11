"""
News API viewsets
"""

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Post model CRUD viewset
    Also provides endpoint 'upvote_post'
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # endpoint for upvote
    @action(detail=True, methods=["GET"])
    def upvote_post(self, *args, **kwargs) -> Response:
        """
        Endpoint that enables upvoting the post
        Upvoting the post - field 'upvotes_amount' will be increased by one
        """
        post = self.get_object()
        post.upvotes_amount += 1
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Comment model CRUD viewset
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer: CommentSerializer) -> None:
        """
        This method use URL kwargs to set field 'post' of model 'Comment'
        when new 'Comment' instance is being added.
        As 'post' is read-only field, the only way to get it is from URL.
        """
        post_id = int(self.kwargs["parent_lookup_post"])
        serializer.save(post_id=post_id)
