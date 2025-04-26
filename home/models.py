from django.db import models

# Hero Section
class HeroSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    button_one_text = models.CharField(max_length=100)
    button_one_link = models.URLField()
    button_two_text = models.CharField(max_length=100, blank=True, null=True)
    button_two_link = models.URLField(blank=True, null=True)
    background_image = models.ImageField(upload_to='hero/')
    featured_image = models.ImageField(upload_to='hero/featured/')
    years_experience = models.CharField(max_length=10)
    countries_served = models.CharField(max_length=10)
    support_hours = models.CharField(max_length=10)

    def __str__(self):
        return self.title

# Our Services Section
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=100)  # e.g., FaWarehouse
    feature_one = models.CharField(max_length=255, blank=True, null=True)
    feature_two = models.CharField(max_length=255, blank=True, null=True)
    feature_three = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

# Why Choose Us Section
class WhyChooseUsReason(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=100)  # e.g., FaLock

    def __str__(self):
        return self.title

# Infrastructure Section
class InfrastructureFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=100)  # e.g., FaMapMarkerAlt

    def __str__(self):
        return self.title

class InfrastructureSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    main_image = models.ImageField(upload_to='infrastructure/')

    def __str__(self):
        return self.title

# Clients and Partners Section
class ClientPartner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name
