from django.urls import re_path, path
from .views import PostApiView, PostUpdateRetriveViw

urlpatterns = [
    path("", PostApiView.as_view(), name="post"),
    path("<int:id>", PostUpdateRetriveViw.as_view(), name="retrive_post"),
]
