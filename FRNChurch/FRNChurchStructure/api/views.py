from rest_framework import viewsets
from rest_framework import generics
from FRNChurchStructure.models import Group
from .serializers import GroupSerializer, ChildrenGroupSerializer

class ChildrenGroupView(generics.ListAPIView):
	serializer_class = ChildrenGroupSerializer

	def get_queryset(self, *args, **kwargs):
		parent_id = self.kwargs['parent_id']
		return Group.objects.filter(parentGroup_id=parent_id)

class GroupView(viewsets.ReadOnlyModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

