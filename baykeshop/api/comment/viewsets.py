from baykeshop.common import viewsets, permission
from baykeshop.apps.comment.models import BaykeShopComment
from .serializers import BaykeShopCommentSerializer


class BaykeShopCommentViewSet(viewsets.ModelViewSet):
    """ 评论接口 """
    queryset = BaykeShopComment.objects.all()
    serializer_class = BaykeShopCommentSerializer
    permission_classes = [permission.BaykePermission]


