from django.urls import path
from .import views

urlpatterns = [
    path('notes/', views.notes, name='notes'),
    path('notes/<slug:slug>/', views.note_detail, name='note-detail'),
]

# ENDPOINTS.
# GET_ALL_NOTES_and_CREATE_NEW_NOTE = "http://127.0.0.1:8004/notes/"
# GET_SPECIDIED_NOTE = "http://127.0.0.1:8004/notes/note-slug"
