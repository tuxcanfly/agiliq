from threading import Thread

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from myapp.models import MyModel


class MyThread(Thread):

    def __init__(self, my_id):
        super(MyThread, self).__init__(name=my_id)
        self.my_id = my_id

    def run(self):
        instance, created = MyModel.objects.get_or_create(my_id=self.my_id)
        print '%s %s' % (instance.id, created)
        instance.delete()
        return


class Command(BaseCommand):
    args = '<my_id my_id ...>'
    help = 'Get or create instace of mymodel with my_id'

    def handle(self, *args, **options):
        for my_id in args:
            thread = MyThread(my_id=my_id)
            thread.start()
            MyModel.objects.all()
