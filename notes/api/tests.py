from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Note


class NotesTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "test",
            "test@test.com",
            "test",
        )

        self.note_data = {
            "subject": "My first Note",
            "text": "this is my first note"
        }

        self.note_one = Note.objects.create(subject="Test subject 01", text="Test text 01")
        self.note_two = Note.objects.create(subject="Test subject 02", text="Test text 02")

    def add_user_token_authorization(self):
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {str(refresh.access_token)}"
        )

    def test_notes_unauthorized_request(self):
        url = reverse("notes-list")
        response = self.client.get(f"{url}")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_notes(self):
        url = reverse("notes-list")
        self.add_user_token_authorization()
        response = self.client.get(url)
        self.assertEqual(len(response.json()), 2)

    def test_create_notes(self):
        url = reverse("notes-list")
        self.add_user_token_authorization()
        response = self.client.post(url, self.note_data)

        saved_note = Note.objects.get(subject='My first Note')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(saved_note.text, self.note_data['text'])
        self.assertEqual(saved_note.subject, self.note_data['subject'])

    def test_update_notes(self):
        url = reverse("notes-detail", kwargs={'pk':self.note_one.id})
        self.add_user_token_authorization()
        response = self.client.patch(url, {'subject':'updated'})

        saved_note = Note.objects.get(id=self.note_one.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(saved_note.subject, 'updated')
        self.assertEqual(saved_note.text, self.note_one.text)

    def test_note_detail(self):
        url = reverse("notes-detail", kwargs={'pk':self.note_one.id})
        self.add_user_token_authorization()
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.note_one.text, data['text'])
        self.assertEqual(self.note_one.subject, data['subject'])

    def test_destroy(self):
        url = reverse("notes-detail", kwargs={'pk':self.note_one.id})
        self.add_user_token_authorization()
        response = self.client.delete(url)
        notes_queryset = Note.objects.filter(pk=self.note_one.id)
        
        self.assertEqual(len(notes_queryset), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
