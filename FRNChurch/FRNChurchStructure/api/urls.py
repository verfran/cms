from django.urls import path, include
from .views import GroupView, GroupGroupsView, GroupPathView, ChristianView, GroupChristiansView, GroupDashboardView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Group', GroupView)
router.register('Christian', ChristianView)

urlpatterns = [
	path('', include(router.urls)),
	path('GroupGroups/<int:parent_id>/', GroupGroupsView.as_view()),
	path('GroupPath/<int:id>/', GroupPathView.as_view()),
	path('GroupChristians/<int:group_id>/', GroupChristiansView.as_view()),
	path('GroupDashboard/<int:id>/', GroupDashboardView.as_view()),
]

