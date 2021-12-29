from django.db import models

# Create your models here.

class Room(models.Model):
    
    #Type (individual, team etc)
    class QuizType(models.TextChoices):
        INDIVIDUALS = 'IN'
        TEAMS = 'TE'
        MYSTERY_TEAMS = 'MY'
    quiztype = models.CharField(max_length = 2, choices = QuizType.choices, default = QuizType.INDIVIDUALS)
    roomuid = models.CharField(max_length = 10, unique=True)
    public = models.BooleanField(default=True)
    password = models.CharField(max_length=30)
    questions = models.FileField(upload_to='/media/', default='/static/files/default.csv')
    #need to verify file-type (with python-magic?)


    def __str__(self):
        return self.roomuid