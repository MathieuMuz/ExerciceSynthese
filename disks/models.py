from django.db import models


class Track(models.Model):
    Name = models.CharField(max_length=200)
    Composer = models.CharField(max_length=220)
    Milliseconds = models.CharField(max_length=200)
    Bytes = models.IntegerField()
    UnitPrice = models.DecimalField(decimal_places=2, max_digits=10)

    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "track"
        ordering = ['Composer', 'Name']

    def __str__(self):
        return self.Name


class Album(models.Model):
    Title = models.CharField(max_length=160)

    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "album"
        ordering = ['artist', 'Title']

    def __str__(self):
        return self.Title


class Artist(models.Model):
    Name = models.CharField(max_length=120)

    class Meta:
        verbose_name = "artist"
        ordering = ['Name']

    def __str__(self):
        return self.Name
