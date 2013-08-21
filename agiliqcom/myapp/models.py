from django.db import models

# Create your models here.


class MyModel(models.Model):
    my_id = models.IntegerField(unique=True)

    def __unicode__(self):
        return self.my_id
