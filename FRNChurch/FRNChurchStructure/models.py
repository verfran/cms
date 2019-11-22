from django.db import models

# Create your models here.
class Group(models.Model):
	name = models.CharField(max_length=80)
	type = models.CharField(max_length=25, blank = True, null = True)
	parentGroup = models.ForeignKey('self', on_delete=models.SET_NULL, blank = True, null = True)
	#menLeader = models.ForeignKey('FRNChurchStructure.Christian',
	#	on_delete=models.SET_NULL, null = True)
	#womenLeader = models.ForeignKey('FRNChurchStructure.Christian',
	#	on_delete=models.SET_NULL, null = True, related_name = 'femaleLeader')

	def __str__(self):
		return self.name

class Contact(models.Model):
	phoneNumber = models.CharField(max_length=15,blank=True, null=True)
	email = models.EmailField(max_length=50,blank=True, null=True)

	def __str__(self):
		if None != self.phoneNumber:
			return self.phoneNumber
		else:
			return self.email

class Person(models.Model):
	firstName = models.CharField(max_length=30)
	secondName = models.CharField(max_length=30, null = True, blank=True)

	GENDER_CHOICE = (
		('M', 'Male'),
		('F', 'Female'),
		)
	gender = models.CharField(max_length=1,choices = GENDER_CHOICE, default = 'M')
	dateOfBirth = models.DateField(null=True, blank=True)
	notes = models.TextField(blank=True)
	contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null = True, blank=True)

	MARITALSTATUS_CHOICE = (
		('S', 'Single'),
		('M', 'Married'),
		('D', 'Divorced'),
		('W', 'Widowed'),
		)
	maritalStatus = models.CharField(max_length=1, choices=MARITALSTATUS_CHOICE, default = 'S')

	def __str__(self):
		name = self.firstName
		if self.secondName:
			name = name + " " + self.secondName
		return name

class Christian(Person):
	dateOfBaptism = models.DateField(null=True, blank=True)
	familyGroup = models.ForeignKey(Group, on_delete=models.SET_NULL, null = True)
 
