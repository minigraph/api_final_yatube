from rest_framework import viewsets, pagination, filters
from posts.models import Post, Group, Follow
from . import serializers, permissions
from .serializers import CommentSerializer
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.OwnerOrReadOnly, )
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = (permissions.OwnerOrReadOnly, )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.OwnerOrReadOnly, )

    def __get_post(self):
        """Получить экземпляр Post по id из пути."""
        id = self.kwargs.get('post_id')
        return get_object_or_404(Post, id=id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.__get_post())

    def get_queryset(self):
        return self.__get_post().comments.all()


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', 'user__username', )

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
