from django.test import TestCase
from .models import Song, Podcast, AudioBook
from django.utils import timezone


class SongTestCase(TestCase):
    def setUp(self):
        Song.objects.create(file="lion", duration=320, upload_time=timezone.now())
        Song.objects.create(file="lion", duration=320, upload_time=timezone.now())

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
