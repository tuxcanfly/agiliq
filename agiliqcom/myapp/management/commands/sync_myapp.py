from django.core.management.base import BaseCommand, CommandError
from myapp.models import MyModel

from threading import Lock

MYMODEL_LOCK = Lock()

class Command(BaseCommand):
    args = '<my_id my_id ...>'
    help = 'Get or create instace of mymodel with my_id'

    def handle(self, *args, **options):
        for my_id in args:
            created = False
            try:
                instance = MyModel.objects.get(my_id=my_id)
            except MyModel.DoesNotExist:
                with MYMODEL_LOCK:
                    try:
                        instance = MyModel.objects.create(my_id=my_id)
                        created = True
                    except MyModel.DoesNotExist:
                        instance = MyModel.objects.get(my_id=my_id)
            self.stdout.write('%s %s' % (instance.id, created))
            instance.delete()
            MyModel.objects.all()
