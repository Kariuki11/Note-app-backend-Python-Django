from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework import status

# Create your views here.

# This function allows searching notes based on a query parameter (search). 
# It filters notes based on whether the query is found in the title, body, or category of a note.
@api_view(['GET'])
def search_notes(request):
    query = request.query_params.get("search")
    
    # Filter notes based on the search query, checking if it is in the title, body, or category fields
    notes = Note.objects.filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(category__icontains=query))
    
    # Serialize the filtered notes and return them in the response
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# This function handles GET requests to list all notes and POST requests to create a new note.
@api_view(["GET", "POST"])
def notes(request):
    if request.method == "GET":
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    # Handle POST request: Create a new note
    elif request.method == "POST":
        serializer = NoteSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
# This function handles GET, PUT, and DELETE requests for a specific note identified by its slug.
@api_view(['GET', 'PUT', 'DELETE'])   
def note_detail(request, slug):
    try:
        note = Note.objects.get(slug=slug)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # If the data is not valid, return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Handle DELETE request: Delete the specified note
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




















# from django.shortcuts import render
# from .models import Note
# from .serializers import NoteSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.db.models import Q
# from rest_framework import status

# # Create your views here.

# @api_view(['GET'])
# def search_notes(request):
#     query = request.query_params.get("search")
#     notes = Note.objects.filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(category__icontains=query))
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(["GET", "POST"])
# def notes(request):
#     if request.method == "GET":
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)
    
#     elif request.method =="POST":
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
# @api_view(['GET', 'PUT', 'DELETE'])   
# def note_detail(request, slug):
#     try:
#         note = Note.objects.get(slug=slug)
#     except Note.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = NoteSerializer(note, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)