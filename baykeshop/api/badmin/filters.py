from django_filters import rest_framework

from baykeshop.apps.badmin.models import BaykeDepartment, BaykeUser, BaykeDictValue


class BaykeDepartmentFilterSet(rest_framework.FilterSet):
    
    class Meta:
        model = BaykeDepartment
        fields = ('parent', 'is_enable')
        

class BaykeUserFilterSet(rest_framework.FilterSet):
    
    class Meta:
        model = BaykeUser
        fields = ('dept', 'user_type')
        

class BaykeDictValueFilterSet(rest_framework.FilterSet):
    
    class Meta:
        model = BaykeDictValue
        fields = ('dic__code', )
        
