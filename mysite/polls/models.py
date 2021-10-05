from django.db import models

# Create your models here.


'''
Here, each model is represented by a class that subclasses django.db.models.Model. 
Each model has a number of class variables, each of which represents a database field in the model.
'''

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # inherit a model from another class
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Customer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    weight = models.IntegerField()