from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    #
    path("api/posts/", include("posts.urls")),
]
