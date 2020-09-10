from rest_framework_extensions.routers import ExtendedDefaultRouter

from .views import CommentViewSet, PostViewSet

router = ExtendedDefaultRouter()
router.register(
    'posts',
    PostViewSet,
    basename='post'
).register(
    'comments',
    CommentViewSet,
    basename='posts-comment',
    parents_query_lookups=['post']  # Comments.object.filter(post={value})
)

urlpatterns = router.urls  # API endpoints
