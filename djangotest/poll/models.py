import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    q_text = models.CharField(max_length=200)
    q_date = models.DateTimeField('Published date')

    def __str__(self):
        return self.q_text

    def published_recently(self):
        return self.q_date >= timezone.now() - datetime.timedelta(days=1)

    published_recently.admin_order_field = 'q_date'
    published_recently.boolean = True
    published_recently.short_description = 'Published Recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    c_text = models.CharField(max_length=200)
    c_vote = models.IntegerField(default=0)

    def __str__(self):
        return self.c_text

