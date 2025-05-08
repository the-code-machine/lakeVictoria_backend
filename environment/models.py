# models.py
from django.db import models

class EnvironmentalPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_description = models.TextField()
    image = models.ImageField(upload_to='environment/')

    def __str__(self):
        return "Environmental Page"

class EnvironmentalInitiative(models.Model):
    page = models.ForeignKey(EnvironmentalPage, on_delete=models.CASCADE, related_name='initiatives')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='environment/initiatives/')
    stats = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class CarbonFootprintPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_description = models.TextField()
    image = models.ImageField(upload_to='environment/carbon/')
    volume_shipped = models.PositiveIntegerField()

    def __str__(self):
        return "Carbon Footprint Page"

class OilManagementPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='environment/oil/management/')
    volume_shipped = models.PositiveIntegerField(blank=True, null=True) 

    def __str__(self):
        return "Oil Management Page"

class OilSystem(models.Model):
    page = models.ForeignKey(OilManagementPage, on_delete=models.CASCADE, related_name='systems')
    title = models.CharField(max_length=255)
    description = models.TextField()
    efficiency = models.CharField(max_length=255)
    image = models.ImageField(upload_to='environment/oil/systems/')

    def __str__(self):
        return self.title

class OilProcessStep(models.Model):
    page = models.ForeignKey(OilManagementPage, on_delete=models.CASCADE, related_name='process_steps')
    step = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['step']

    def __str__(self):
        return f"Step {self.step}: {self.title}"
