from django.db import models

class ServiceMainPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_description = models.TextField()

    def __str__(self):
        return "Service Main Page"


class ServiceCategory(models.Model):
    page = models.ForeignKey(ServiceMainPage, on_delete=models.CASCADE, related_name="categories")
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="services/")

    def __str__(self):
        return self.title


class ServiceCategoryContent(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name="content_items")
    sub_title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.sub_title

class LogisticServicePage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_description = models.TextField()
    image = models.ImageField(upload_to='logistics/')

    def __str__(self):
        return "Logistic Service Page"


class LogisticService(models.Model):
    page = models.ForeignKey(LogisticServicePage, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='logistics/')

    def __str__(self):
        return self.title



class ServiceDetailPoint(models.Model):
    service = models.ForeignKey(LogisticService, on_delete=models.CASCADE, related_name='details')
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text

class ServiceAreaPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_description = models.TextField()
    image = models.ImageField(upload_to='service-area/')

    def __str__(self):
        return "Service Area Page"


# --- COVERAGE MAP ---
class CoverageMap(models.Model):
    page = models.OneToOneField(ServiceAreaPage, on_delete=models.CASCADE, related_name='coverage_map')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='service-area/')
    alt = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class CountryCoverage(models.Model):
    map = models.ForeignKey(CoverageMap, on_delete=models.CASCADE, related_name='countries')
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country


class CountryLocation(models.Model):
    country = models.ForeignKey(CountryCoverage, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# --- SERVICE AREA DETAILS ---
class ServiceAreaSection(models.Model):
    page = models.ForeignKey(ServiceAreaPage, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='service-area/')

    def __str__(self):
        return self.title


class ServiceAreaDetailPoint(models.Model):
    section = models.ForeignKey(ServiceAreaSection, on_delete=models.CASCADE, related_name='details')
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text

class StorageServicePage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_description = models.TextField()
    image = models.ImageField(upload_to='storage/', blank=True, null=True)

    def __str__(self):
        return "Storage & Handling Page"


class StorageService(models.Model):
    page = models.ForeignKey(StorageServicePage, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='storage/services/')

    def __str__(self):
        return self.title


class StorageServiceDetail(models.Model):
    service = models.ForeignKey(StorageService, on_delete=models.CASCADE, related_name='details')
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text