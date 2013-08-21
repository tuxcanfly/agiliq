from django.core.management.base import BaseCommand, CommandError
from myapp.models import MyModel

class Command(BaseCommand):
    args = '<my_id my_id ...>'
    help = 'Get or create instace of mymodel with my_id'

    def handle(self, *args, **options):
        for my_id in args:
            instance, created  = MyModel.objects.get_or_create(my_id=my_id)
            self.stdout.write('%s %s' % (instance.id, created))
            instance.delete()
            MyModel.objects.all()
