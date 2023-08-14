from django.urls import path, include

from baykeshop.apps.badmin.views import index


urlpatterns = [
    path('badmin/', index, name='index'),
]