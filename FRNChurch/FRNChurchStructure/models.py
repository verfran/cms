from django.db import models

# Create your models here.
class Group(models.Model):
	name = models.CharField(max_length=80)
	type = models.CharField(max_length=25)
	parentGroup = models.ForeignKey('self', on_delete=models.SET_NULL, null = True)
	menLeader = models.ForeignKey('FRNChurchStructure.Christian',
		on_delete=models.SET_NULL, null = True)
	womenLeader = models.ForeignKey('FRNChurchStructure.Christian',
		on_delete=models.SET_NULL, null = True, related_name = 'femaleLeader')

	def __str__(self):
		return self.name

class Person(models.Model):
	firstName = models.CharField(max_length=30)
	secondName = models.CharField(max_length=30, null = True)

	GENDER_CHOICE = (
		('M', 'Male'),
		('F', 'Female'),
		)
	gender = models.CharField(max_length=1,choices = GENDER_CHOICE)

	dateOfBirth = models.DateField(null=True, blank=True)

	notes = models.TextField(blank=True)

	def __str__(self):
		return self.firstName + " " + self.secondName

class Christian(Person):
	dateOfBaptism = models.DateField(null=True, blank=True)
	familyGroup = models.ForeignKey(Group, on_delete=models.SET_NULL, null = True)
 
