from django.core.management.base import BaseCommand, CommandError

from django.db import transaction

from myapp.models import MyModel


class Command(BaseCommand):
    args = '<my_id my_id ...>'
    help = 'Get or create instace of mymodel with my_id'

    def handle(self, *args, **options):
        for my_id in args:
            instance, created = self.get_or_create(my_id)
            self.stdout.write('%s %s' % (instance.id, created))
            instance.delete()
            MyModel.objects.all()

    def get_or_create(self, my_id):
        created = False
        try:
            instance = MyModel.objects.get(my_id=my_id)
        except MyModel.DoesNotExist:
            with transaction.commit_on_success():
                try:
                    instance = MyModel.objects.create(my_id=my_id)
                    created = True
                except MyModel.DoesNotExist:
                    instance = MyModel.objects.get(my_id=my_id)
        return instance, created

