from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import os


class Song(models.Model):
    file = models.FileField(upload_to='uploads',
                null=False,
                max_length=100
                )
    duration = models.PositiveIntegerField(null=False),
    upload_time = models.DateTimeField(null=False, default=timezone.now)

    def __unicode__(self):
        return self.file.name

    def name(self):
        return os.path.basename(self.file.name)

    def delete(self, *args, **kwargs):
        os.remove(self.file.path)
        self.file.delete(False)
        super(Song, self).delete(*args, **kwargs)


class Podcast(models.Model):
    file = models.FileField(upload_to='uploads',
                null=False,
                max_length=100
                )
    duration = models.PositiveIntegerField(null=False),
    upload_time = models.DateTimeField(null=False, default=timezone.now)
    host = models.CharField(max_length=100)
    participants = ArrayField(default=list, base_field=models.CharField(max_length=100),
            size=10)

    def __unicode__(self):
        return self.file.name

    def name(self):
        return os.path.basename(self.file.name)

    def delete(self, *args, **kwargs):
        os.remove(self.file.path)
        self.file.delete(False)
        super(Podcast, self).delete(*args, **kwargs)


class AudioBook(models.Model):
    file = models.FileField(upload_to='uploads',
                null=False,
                max_length=100
                )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(null=False),
    upload_time = models.DateTimeField(null=False, default=timezone.now)

    def __unicode__(self):
        return self.file.name

    def name(self):
        return os.path.basename(self.file.name)

    def delete(self, *args, **kwargs):
        os.remove(self.file.path)
        self.file.delete(False)
        super(AudioBook, self).delete(*args, **kwargs)
