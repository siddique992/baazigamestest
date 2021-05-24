import os
from django.test.client import MULTIPART_CONTENT
from django.test import TestCase
from .models import Song
from django.utils import timezone
from django.core.files import File
from .api.serializers import SongSerializer

class AudioFilesViewTest(TestCase):
    def setUp(self):
        filepath1 = '/run/media/afzalfarooque/New Volume/videos/song/02 - Tu Jaane Na.mp3'
        with open(filepath1, 'rb') as fi:
             file1 = File(fi, name=os.path.basename(fi.name))
             self.first_audio = Song.objects.create(file=file1)
        filepath2 = '/run/media/afzalfarooque/New Volume/videos/song/old/Pakeezah-Chalte Chalte Yunhi Koi.mp3'
        with open(filepath2, 'rb') as fi:
             file2 = File(fi, name=os.path.basename(fi.name))
             self.first_audio = Song.objects.create(file=file2)

    def test_song_view_get_all(self):
        response = self.client.get('/song/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(Song.objects.all()))

    def test_song_view_get(self):
        pk = 1
        response = self.client.get(f'/song/{pk}/')
        try:
           obj = Song.objects.get(pk=pk)
           self.assertEqual(response.status_code, 200)
           self.assertEqual(response.data, SongSerializer(obj).data)
        except Song.DoesNotExist:
           self.assertEqual(response.status_code, 400)

    def test_song_view_post(self):
        with open('/run/media/afzalfarooque/New Volume/videos/song/02 - Tu Jaane Na.mp3', 'rb') as fp:
            response = self.client.post('/song/',
            {
            'name': '02 - Tu Jaane Na.mp3',
            'file': fp
            })

        self.assertEqual(response.status_code, 200)


    def test_song_view_update(self):
        pk = 1
        with open('/run/media/afzalfarooque/New Volume/videos/song/02 - Tu Jaane Na.mp3', 'rb') as fp:
            response = self.client.put(f'/song/{pk}/',
            {
            'name': '02 - Tu Jaane Na.mp3',
            'file': fp
            },content_type=MULTIPART_CONTENT)
        try:
           obj = Song.objects.get(pk=pk)
           self.assertEqual(response.status_code, 200)
        except Song.DoesNotExist:
           self.assertEqual(response.status_code, 400)
