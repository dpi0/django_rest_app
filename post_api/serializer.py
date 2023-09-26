from rest_framework import serializers
from post_api.models import Post


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    publish_date = serializers.DateTimeField()

    def create(self, data):
        return Post.objects.create(**data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.publish_date = validated_data.get(
            "publish_date", instance.publish_date
        )
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance
