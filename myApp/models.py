from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Save(models.Model):
    save_user = models.ForeignKey(User, on_delete = models.CASCADE)
    save_date = models.DateTimeField('date published', null = True, default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.save_user, self.save_date) 