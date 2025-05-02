from django.db import models

# Hero Section
class HeroSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    background_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    featured_image = models.ImageField(upload_to='hero/featured/', blank=True, null=True)
    years_experience = models.CharField(max_length=10, blank=True, null=True)
    countries_served = models.CharField(max_length=10, blank=True, null=True)
    support_hours = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.title


# Services – allows multiple entries
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    feature_one = models.CharField(max_length=255, blank=True, null=True)
    feature_two = models.CharField(max_length=255, blank=True, null=True)
    feature_three = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


# Why Choose Us Section
class WhyChooseUsReason(models.Model):
    title = models.CharField(max_length=100)

    feature_one_title = models.CharField(max_length=100, blank=True, null=True)
    feature_one_description = models.TextField(blank=True, null=True)

    feature_two_title = models.CharField(max_length=100, blank=True, null=True)
    feature_two_description = models.TextField(blank=True, null=True)

    feature_three_title = models.CharField(max_length=100, blank=True, null=True)
    feature_three_description = models.TextField(blank=True, null=True)

    feature_four_title = models.CharField(max_length=100, blank=True, null=True)
    feature_four_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


# Infrastructure Section
class InfrastructureSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    main_image = models.ImageField(upload_to='infrastructure/', blank=True, null=True)

    feature_one_title = models.CharField(max_length=100, blank=True, null=True)
    feature_one_description = models.TextField(blank=True, null=True)

    feature_two_title = models.CharField(max_length=100, blank=True, null=True)
    feature_two_description = models.TextField(blank=True, null=True)

    feature_three_title = models.CharField(max_length=100, blank=True, null=True)
    feature_three_description = models.TextField(blank=True, null=True)

    feature_four_title = models.CharField(max_length=100, blank=True, null=True)
    feature_four_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


# Clients Section
class ClientPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class ClientLogo(models.Model):
    page = models.ForeignKey(
        ClientPage,
        on_delete=models.CASCADE,
        related_name='logos'
    )
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='client_logos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.page.title})"
