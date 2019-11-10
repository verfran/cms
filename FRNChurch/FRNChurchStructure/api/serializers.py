from rest_framework import serializers
from FRNChurchStructure.models import Group, Christian

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'name', 'type', 'parentGroup')

class GroupChildrenSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'name', 'type')

class GroupPathSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'name', 'type')

class ChristianSerializer(serializers.ModelSerializer):
	class Meta:
		model = Christian
		fields = ('id', 'firstName', 'secondName', 'gender')

class GroupChristiansSerializer(serializers.ModelSerializer):
	class Meta:
		model = Christian
		fields = ('id', 'firstName', 'secondName', 'gender', 'dateOfBirth','dateOfBaptism')
