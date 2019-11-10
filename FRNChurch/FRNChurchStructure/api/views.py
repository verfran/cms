from rest_framework import viewsets
from rest_framework import generics
from django.db.models import Q
from FRNChurchStructure.models import Group, Christian
from .serializers import GroupSerializer, GroupChildrenSerializer, GroupPathSerializer, ChristianSerializer, GroupChristiansSerializer

class GroupView(viewsets.ReadOnlyModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class GroupGroupsView(generics.ListAPIView):
	serializer_class = GroupChildrenSerializer

	def get_queryset(self, *args, **kwargs):
		parent_id = self.kwargs['parent_id']
		return Group.objects.filter(parentGroup_id=parent_id)

class GroupPathView(generics.ListAPIView):
	serializer_class = GroupPathSerializer

	def getParent(self, id):
		gp = None
		try:
			gp = Group.objects.get(pk=id)
		except Group.DoesNotExist:
			return None

		if gp.parentGroup == None:
			return None
		pgp = Group.objects.get(pk=gp.parentGroup.id)
		if pgp == None:
			return None
		return pgp.id

	def get_queryset(self, *args, **kwargs):
		id = self.kwargs['id']
		parentIds = []

		parentid = self.getParent(id)
		while parentid != None:
			parentIds.append(parentid)
			parentid = self.getParent(parentid)

		query = Q()
		for pid in parentIds:
			if query == Q():
				query = Q(id=pid)
			else:
				query = query | Q(id=pid)

		if query == Q():
			return None

		return Group.objects.filter(query)


class ChristianView(viewsets.ReadOnlyModelViewSet):
	queryset = Christian.objects.all()
	serializer_class = ChristianSerializer

class GroupChristiansView(generics.ListAPIView):
	serializer_class = GroupChristiansSerializer

	def get_queryset(self, *args, **kwargs):
		group_id = self.kwargs['group_id']
		return Christian.objects.filter(familyGroup_id=group_id)
