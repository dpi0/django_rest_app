from post_api.models import Post
from post_api.serializer import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# from django.shortcuts import render
# from django.http import JsonResponse


class GetAllPost(APIView):
    def get(self, request):
        post = Post.objects.all()
        post_serialized = PostSerializer(post, many=True)
        return Response(post_serialized.data, status=status.HTTP_200_OK)


class GetPostById(APIView):
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
            post_serialized = PostSerializer(post)
            return Response(post_serialized.data)
        except Post.DoesNotExist:
            return Response(
                "Post Not Found", status=status.HTTP_404_NOT_FOUND
            )


class CreatePost(APIView):
    def post(self, request):
        post_serialized = PostSerializer(data=request.data)
        if not post_serialized.is_valid():
            return Response(post_serialized.errors)
        post_serialized.save()
        return Response(
            post_serialized.data, status=status.HTTP_201_CREATED
        )


class UpdatePost(APIView):
    def put(self, request, id):
        try:
            post = Post.objects.get(id=id)
            post_serialized = PostSerializer(post, data=request.data)
            if not post_serialized.is_valid():
                return Response(post_serialized.errors)
            post_serialized.save()
            return Response(
                post_serialized.data, status=status.HTTP_400_BAD_REQUEST
            )
        except Post.DoesNotExist:
            return Response(
                "Post Not Found", status=status.HTTP_404_NOT_FOUND
            )


class DeletePost(APIView):
    def delete(self, request, id):
        try:
            post = Post.objects.get(id=id)
            post.delete()
            return Response(
                "Post Deleted Successfully",
                status=status.HTTP_204_NO_CONTENT,
            )
        except Post.DoesNotExist:
            return Response(
                "Post Not Found", status=status.HTTP_404_NOT_FOUND
            )
