from rest_framework import serializers

from baykeshop.api.badmin.serializers import UserSerializer
from baykeshop.common.serializers import ModelSerializer, Serializer
from baykeshop.apps.comment.models import BaykeShopComment


class BaykeShopCommentSerializer(ModelSerializer):
    """ 评论 """
    owner = UserSerializer(many=False, read_only=True)
    
    class Meta:
        model = BaykeShopComment
        fields = "__all__"
        read_only_fields = ("reply", )
        

class BaykeShopCommentReplySerializer(ModelSerializer):
    """ 回复 """
    owner = UserSerializer(many=False, read_only=True)
    reply = serializers.CharField(max_length=200, min_length=5, required=True)
    
    class Meta:
        model = BaykeShopComment
        fields = "__all__"
        read_only_fields = ("content", "comment_choices")