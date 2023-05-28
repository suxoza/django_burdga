from rest_framework import generics, filters
from .serializers import Post, PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get("title_only"):
            return ["title"]
        return super().get_search_fields(view, request)


class PostApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        # filters.SearchFilter,
        CustomSearchFilter,
    ]
    filterset_fields = ["title", "price"]
    ordering_fields = ["title", "id"]
    search_fields = ["description", "title"]


class PostUpdateRetriveViw(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"
