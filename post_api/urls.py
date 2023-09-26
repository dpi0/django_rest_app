from django.contrib import admin
from django.urls import path


from post_api.views import (
    GetAllPost,
    CreatePost,
    GetPostById,
    UpdatePost,
    DeletePost,
)


urlpatterns = [
    path("", GetAllPost.as_view()),
    path("create", CreatePost.as_view()),
    path("<int:id>", GetPostById.as_view()),
    path("update/<int:id>", UpdatePost.as_view()),
    path("delete/<int:id>", DeletePost.as_view()),
]
