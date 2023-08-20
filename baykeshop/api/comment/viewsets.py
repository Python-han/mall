from rest_framework.decorators import action

from baykeshop.common import mixins, viewsets, pagination
from baykeshop.apps.comment.models import BaykeShopComment
from .serializers import BaykeShopCommentSerializer, BaykeShopCommentReplySerializer


class BaykeShopCommentViewSet(mixins.ListModelMixin, 
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin, 
                              mixins.BatchDestroyModelMixin, 
                              viewsets.GenericViewSet):
    """ 评论接口 """
    queryset = BaykeShopComment.objects.all()
    serializer_class = BaykeShopCommentSerializer
    pagination_class = pagination.PageNumberPagination    

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response
    
    @action(methods=['delete'], detail=False)
    def batch_destroy(self, request, *args, **kwargs):
        return super().batch_destroy(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action in ['partial_update', 'update']:
            return BaykeShopCommentReplySerializer
        return super().get_serializer_class()
