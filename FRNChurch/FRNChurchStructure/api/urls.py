from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Group', views.GroupView)

urlpatterns = [
	path('', include(router.urls)),
	path('ChildrenGroup/<int:parent_id>', views.ChildrenGroupView.as_view()),
]

