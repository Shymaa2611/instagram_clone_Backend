from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('post',views.postviewSets,basename='post')
router.register('comment',views.commentviewSets,basename='comment')
router.register('profile',views.profileviwsets,basename='profile')
urlpatterns=[

]
urlpatterns+=router.urls