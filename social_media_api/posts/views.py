from rest_framework import status,  viewsets, permissions
from .models import Post, Comment, Like, Notification
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType



class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only allow owners of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so GET, HEAD, or OPTIONS are safe.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get all users the current user follows
        following_users = request.user.following.all()

        # Get posts by followed users, ordered by newest first
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize and return
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Safely get the post or return 404
        post = generics.get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # Optionally create a notification for the post owner
            if post.owner != request.user:
                Notification.objects.create(
                    sender=request.user,
                    recipient=post.owner,
                    post=post,
                    notification_type="like"
                )
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Already liked"}, status=status.HTTP_200_OK)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Safely get the post or return 404
        post = generics.get_object_or_404(Post, pk=pk)

        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"message": "You haven’t liked this post"}, status=status.HTTP_400_BAD_REQUEST)