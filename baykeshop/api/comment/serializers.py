from rest_framework import serializers

from baykeshop.common.serializers import ModelSerializer
from baykeshop.apps.comment.models import BaykeShopComment


class BaykeShopCommentSerializer(ModelSerializer):
    """ 评论 """    
    class Meta:
        model = BaykeShopComment
        fields = "__all__"
    