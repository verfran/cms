from django.db.models import Q
from rest_framework import serializers
from FRNChurchStructure.models import Group, Christian

class ParentGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'name', 'type')

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'name', 'type')

class ChristianSerializer(serializers.ModelSerializer):
	name = serializers.SerializerMethodField()

	class Meta:
		model = Christian
		fields = ('id', 'name', 'gender')

	def get_name(self, xtian):
		name = xtian.firstName
		if xtian.secondName:
			name = name + " " + xtian.secondName
		return name

class DashboardSerializer(serializers.Serializer):
	groupInfo = serializers.SerializerMethodField()
	parentGroup = GroupSerializer()
	groupGroups = serializers.SerializerMethodField()
	members = serializers.SerializerMethodField()
	men = serializers.SerializerMethodField()
	women = serializers.SerializerMethodField()

	def get_members(self, group):
		queryset = Christian.objects.filter(self.familyGroupquery)
		return ChristianSerializer(queryset, many=True).data

	def get_men(self, group):
		queryset = Christian.objects.filter(self.familyGroupquery, gender='M')
		return ChristianSerializer(queryset, many=True).data

	def get_women(self, group):
		queryset = Christian.objects.filter(self.familyGroupquery, gender='F')
		return ChristianSerializer(queryset, many=True).data

	def get_groupGroups(self, group):
		queryset = Group.objects.filter(parentGroup=group)
		return GroupSerializer(queryset, many=True).data

	def get_groupInfo(self, group):
		retval = {
			"id": group.id,
			"name": group.name,
			"type": group.type,
			"memberCount": self.memberCount(group),
			"menCount": self.menCount(group),
			"womenCount": self.womenCount(group),
		}
		return retval

	def memberCount(self, group):
		self.familyGroupquery = self.getFGquery(group)
		return Christian.objects.filter(self.familyGroupquery).count()

	def getFGquery(self, gp):
		fgs = self.getFamilyGroups(gp)

		if (len(fgs) == 0):
			return 0

		query = Q()
		for fg in fgs:
			if query == Q():
				query = Q(familyGroup=fg)
			else:
				query = query | Q(familyGroup=fg)
		return query

	def getFamilyGroups(self, gp):
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

	def menCount(self, group):
		return Christian.objects.filter(self.familyGroupquery, gender='M').count()

	def womenCount(self, group):
		return Christian.objects.filter(self.familyGroupquery, gender='F').count()


class GroupChristiansSerializer(serializers.ModelSerializer):
	class Meta:
		model = Christian
		fields = ('id', 'firstName', 'secondName', 'gender')
