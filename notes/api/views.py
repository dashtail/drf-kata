from functools import partial
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


class NotesViewSet(viewsets.ViewSet):
    """
    A viewset for viewing and editing notes instances. 
    """

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404

    def list(self, request):
        queryset = Note.objects.all()
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk=None):
        note = self.get_object(pk=pk)
        serializer = NoteSerializer(note)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        note = self.get_object(pk=pk)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        note = self.get_object(pk=pk)
        note.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
