from django.core.management.base import BaseCommand, CommandError
from FRNChurchStructure.models import Group

class Command(BaseCommand):
    help = 'createRegion: This command will create a new Region.\
    		This command will not continue if there are existing groups.\
    		To create a new Region, make sure the database doesnot have any groups'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Indicates the name of the Region to be created')

    def handle(self, *args, **options):	
    	if Group.objects.count() > 0:
    		print("Error: cannot create Region, delete all the existing groups and try again")
    		return

    	group = Group()
    	group.name = options['name']
    	group.save()
    	print( group.name, " Region created")




