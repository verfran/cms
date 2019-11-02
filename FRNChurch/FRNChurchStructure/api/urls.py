from django.urls import path, include
from .views import GroupView, GroupChildrenView, GroupPathView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Group', GroupView)

urlpatterns = [
	path('', include(router.urls)),
	path('GroupChildren/<int:parent_id>', GroupChildrenView.as_view()),
	path('GroupPath/<int:id>', GroupPathView.as_view()),
]

