# from django.shortcuts import render
from post_api.models import Post

# from django.http import JsonResponse
from post_api.serializer import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["GET"])
def get_post(request):
    post = Post.objects.all()
    post_serialized = PostSerializer(post, many=True)
    return Response(post_serialized.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_post_by_id(request, id):
    try:
        post = Post.objects.get(id=id)
        post_serialized = PostSerializer(post)
        return Response(post_serialized.data)
    except Post.DoesNotExist:
        return Response("Post Not Found", status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def create_post(request):
    post_serialized = PostSerializer(data=request.data)
    if not post_serialized.is_valid():
        return Response(post_serialized.errors)
    post_serialized.save()
    return Response(post_serialized.data, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def update_post(request, id):
    post = Post.objects.get(id=id)
    post_serialized = PostSerializer(post, data=request.data)
    if not post_serialized.is_valid():
        return Response(post_serialized.errors)
    post_serialized.save()
    return Response(
        post_serialized.data, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["DELETE"])
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return Response(
        "Post Deleted Successfully", status=status.HTTP_204_NO_CONTENT
    )
