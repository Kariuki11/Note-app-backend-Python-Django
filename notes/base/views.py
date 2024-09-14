from django.shortcuts import render
from notes.base.models import Note
from notes.base.serializers import NoteSerializer

# Create your views here.

def notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)