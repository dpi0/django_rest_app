from rest_framework import serializers
from post_api.models import Post
from django.forms import ValidationError

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField()
#     publish_date = serializers.DateTimeField()

#     def create(self, data):
#         return Post.objects.create(**data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.publish_date = validated_data.get(
#             "publish_date", instance.publish_date
#         )
#         instance.save()
#         return instance

#     def delete(self, instance):
#         instance.delete()
#         return instance


class PostSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def validate_title(self, value):
        if len(value) < 10:
            # raise serializers.ValidationError("Title is too short")
            raise ValidationError("Title is too short")
        return value

    # def validate_publish_date(self, value):
    #     if value:
    #         raise ValidationError("Publish date is invalid")
    #     return value

    def validate(self, data):
        if len(data["content"]) < 10:
            raise ValidationError("Content is too short")
        return data

    def get_description(self, obj):
        return (
            "This is post id:"
            + str(obj.id)
            + ""
            + " having the title: "
            + str(obj.title)
            + ""
            + "published on "
            + str(obj.publish_date)
        )
