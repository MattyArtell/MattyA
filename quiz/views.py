from django.shortcuts import render, redirect
from quiz.models import Room
from .forms import RoomForm
from django.core.exceptions import ValidationError
import random
import csv
import io

# Create your views here.

def genid():
     # Create a new unique 10 char room number
    roomid = ''
    while (len(roomid) < 10):
        chars = 'abcdefghijk1234567890'
        char = random.choice(chars)
        roomid += char
        if Room.objects.filter(roomuid = roomid).exists():
            roomid = ''
            continue
    return(roomid)

def parseqs(csvf):
    #Parse questions & answers from a csv file into a dictionary
    mydict = {}
    decoded_file = csvf.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    #print(io_string)
    for line in csv.reader(io_string):
        mydict[line[0]] = line[1]
    return mydict

def quiz(request):
    return render(request, 'quiz/home.html')

def create(request):
    if request.method == 'GET':
        return render(request, 'quiz/create.html', {'form':RoomForm()})
    else:
        try:
            roomform = RoomForm(request.POST, request.FILES)
            newroom = roomform.save(commit=False)
            roomid = genid()
            newroom.roomuid = roomid
            newroom.save()
            return redirect('../quiz/room/{}'.format(roomid)) # this is weird, without .. it does /quiz/quiz 
        except ValueError:
            return render(request, 'quiz/create.html', {'form':RoomForm(), 'error':'Files must be .csv of no more than 1MB'})
    #return render(request, 'quiz/create.html', {'myid':roomid})

def join(request):
    if request.method == 'GET':
        return render(request, 'quiz/join.html')
    else:
        uid = request.POST.get('roomid')
        passw = request.POST.get('roompass') 
        try:
            roomobj = Room.objects.get(roomuid = uid)
        except:
            return render(request, 'quiz/join.html', {'error':'Invalid room'})
        print(roomobj)
        if (roomobj.public == False):
            if (passw == roomobj.password):
                return redirect('../quiz/room/{}'.format(uid))
            else:
                return render(request, 'quiz/join.html', {'error':'Incorrect password'})
        else: 
            return redirect('../quiz/room/{}'.format(uid))    

def currentroom(request, uid=0):
    if Room.objects.filter(roomuid = uid).exists():
        roomobj = Room.objects.get(roomuid = uid)
        csvf = roomobj.questions
#        print(csvf)
        qdict = parseqs(csvf)
        print(qdict)
        return render(request, 'quiz/currentroom.html', {'id':uid, 'qdict':qdict})
    else:
        return render(request, 'quiz/home.html', {'error':'{} is not a valid room'.format(uid)})
    