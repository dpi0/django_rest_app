from django.contrib import admin
from django.urls import path

from post_api.views import (
    get_post,
    create_post,
    get_post_by_id,
    update_post,
    delete_post,
)

urlpatterns = [
    path("", get_post),
    path("create", create_post),
    path("<int:id>", get_post_by_id),
    path("update/<int:id>", update_post),
    path("delete/<int:id>", delete_post),
]
