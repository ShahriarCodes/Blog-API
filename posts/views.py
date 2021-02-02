from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer

# Create your views here.


class PostList(generics.ListCreateAPIView):
    ## not required if project level permission set to IsAuthenticated inside setting.py
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    ## not required if project level permission set to IsAuthenticated inside setting.py
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer