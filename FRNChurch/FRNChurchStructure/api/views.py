from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Q
from FRNChurchStructure.models import Group, Christian
from .serializers import GroupSerializer, GroupGroupsSerializer, GroupPathSerializer, ChristianSerializer, GroupChristiansSerializer

class GroupDashboardView(APIView):
	def get(self, request, *args, **kwargs):
		return Response({"firstkey":"value"})

class GroupView(viewsets.ReadOnlyModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class GroupGroupsView(generics.ListAPIView):
	serializer_class = GroupGroupsSerializer

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
		fgs = self.getFamilyGroups(group_id)

		if (len(fgs) == 0):
			return None

		query = Q()
		for fg in fgs:
			if query == Q():
				query = Q(familyGroup=fg)
			else:
				query = query | Q(familyGroup=fg)

		return Christian.objects.filter(query)

	def getFamilyGroups(self, id):
		gp = None
		try:
			gp = Group.objects.get(pk=id)
		except Group.DoesNotExist:
			return []

		if gp.type == 'Family Group':
			return [gp]
		return self.getChildrenFamilyGroups(gp)

	def getChildrenFamilyGroups(self, gp):
		cldGrps = Group.objects.filter(parentGroup=gp)
		if len(cldGrps) > 0:
			if cldGrps[0].type == "Family Group":
				return cldGrps
		fgs = []
		for gp in cldGrps:
			fgs.extend(self.getChildrenFamilyGroups(gp))
		return fgs

