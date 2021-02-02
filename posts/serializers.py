from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    # showing author name instead of id (deafult is User.id)
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )
        model = Post

    ## to change field values (testing purpose)
    # def to_representation(self, instance):
    #     rep = super(PostSerializer, self).to_representation(instance)
    #     print(rep)
    #     rep["title"] = instance.body
    #     return rep