from django.shortcuts import render
from rest_framework.generics import(
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from have.serializers import PostSerializers
from have.models import Post
from rest_framework.authentication import SessionAuthentication

from smoke.permissions import IsOwnerOrReadyOnly


class PostListAPIView(CreateModelMixin, ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [SessionAuthentication]
    serializer_class = PostSerializers

    def get_queryset(self):
        r = self.request
        print(r.user)
        qs = Post.objects.all()
        return qs


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class PostCreateAPIView(CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetailAPIView(RetrieveAPIView):
    permission_classes = [IsOwnerOrReadyOnly]
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostUpdateAPIView(UpdateAPIView):
    permission_classes = [IsOwnerOrReadyOnly]
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDeleteAPIView(DestroyAPIView):
    permission_classes = [IsOwnerOrReadyOnly]
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializers
