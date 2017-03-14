from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from blog.models import Post 
from blog.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if instance.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects.cache = {}

        return Response(serializer.data)    

    def destroy(self, request, *args, **kargs):
        instance = self.get_object()

        if instance.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

