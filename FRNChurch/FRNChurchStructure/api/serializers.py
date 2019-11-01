from rest_framework import serializers
from FRNChurchStructure.models import Group

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'name', 'type', 'parentGroup')

class ChildrenGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'name', 'type')