from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['quiztype', 'public', 'password', 'questions']
        labels = {"questions":("Questions: (.csv file in format \" question, answer, question, answer\" etc)")}