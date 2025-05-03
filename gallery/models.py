from django.db import models

class GalleryPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_description = models.TextField()
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)

    def __str__(self):
        return "Gallery Page"

class GalleryItem(models.Model):
    page = models.ForeignKey(GalleryPage, on_delete=models.CASCADE, related_name='items')
    src = models.FileField(upload_to='gallery/items/')
    caption = models.CharField(max_length=255)
    date = models.DateField()
    type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])

    def __str__(self):
        return self.caption
