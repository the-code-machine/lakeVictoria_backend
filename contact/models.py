from django.db import models

# --- Submitted Contact Message ---
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


# --- Company Contact Info ---
class CompanyContactInfo(models.Model):
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    address_line3 = models.CharField(max_length=255, blank=True)
    address_line4 = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20)
    general_email = models.EmailField()

    def __str__(self):
        return "Company Contact Info"

    def has_add_permission(self):
        return not CompanyContactInfo.objects.exists()


class BusinessDevelopmentContact(models.Model):
    company_info = models.ForeignKey(CompanyContactInfo, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.title})"
