from django.db import models

class MediaEventsPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_description = models.TextField()

    def __str__(self):
        return self.title

class MediaSection(models.Model):
    page = models.ForeignKey(MediaEventsPage, related_name='sections', on_delete=models.CASCADE)
    section_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media_events/sections/')

    def __str__(self):
        return self.title

class MediaArticle(models.Model):
    title = models.CharField(max_length=255)
    publication = models.CharField(max_length=255)
    date = models.DateField()
    summary = models.TextField()
    image = models.ImageField(upload_to='media_events/articles/')

    def __str__(self):
        return self.title

class Event(models.Model):
    event_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    thumbnail_image = models.ImageField(upload_to='media_events/events/thumbs/')

    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    src = models.ImageField(upload_to='media_events/events/gallery/')
    caption = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.event.title} - {self.caption}"
