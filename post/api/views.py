from rest_framework.viewsets import ModelViewSet
from post.api.serializers import PostSerializer
from post.models import Post

class PostApiViewSet(ModelViewSet):
    # Esto define los datos que nos tiene que devolver
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    