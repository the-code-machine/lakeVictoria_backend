from django.db import models

# --- ABOUT ---
class AboutMain(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class AboutSection(models.Model):
    SECTION_CHOICES = [
        ("our_identity", "Our Identity"),
        ("our_principles", "Our Principles"),
        ("our_strength", "Our Strength"),
    ]
    page = models.ForeignKey(AboutMain, on_delete=models.CASCADE, related_name="sections",null=True)
    category = models.CharField(max_length=50, choices=SECTION_CHOICES)
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to="about/", blank=True, null=True)

    def __str__(self):
        return f"{self.get_category_display()} - {self.title}"

class AboutCompanyMain(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class AboutCompanySection(models.Model):
    SECTION_CHOICES = [
        ('overview', 'Overview'),
        ('history', 'History'),
        ('leadership', 'Leadership'),
    ]
    page = models.ForeignKey(AboutCompanyMain, on_delete=models.CASCADE, related_name="sections",null=True)
    category = models.CharField(max_length=20, choices=SECTION_CHOICES)
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='about/company/', blank=True, null=True)

    def __str__(self):
        return f"{self.get_category_display()} - {self.title}"


# --- ENVIRONMENT ---
class EnvironmentalPage(models.Model):
    hero_title = models.CharField(max_length=255)
    hero_description = models.TextField()
    intro = models.TextField()

    def __str__(self):
        return "Environmental Stewardship Page"

class EnvironmentalBlock(models.Model):
    BLOCK_CHOICES = [
        ("commitment", "Environmental Commitment"),
        ("initiatives", "Sustainability Initiatives"),
    ]
    page = models.ForeignKey(EnvironmentalPage, on_delete=models.CASCADE, related_name="blocks")
    block_type = models.CharField(max_length=20, choices=BLOCK_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='environment/', blank=True, null=True)

    def __str__(self):
        return f"{self.get_block_type_display()} - {self.title}"

class EnvironmentalBlockPoint(models.Model):
    block = models.ForeignKey(EnvironmentalBlock, on_delete=models.CASCADE, related_name="points")
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class EnvironmentalPillar(models.Model):
    page = models.ForeignKey(EnvironmentalPage, on_delete=models.CASCADE, related_name="pillars")
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# --- MILESTONES ---
class MilestonePage(models.Model):
    hero_title = models.CharField(max_length=255)
    hero_description = models.TextField()
    intro = models.TextField()

    def __str__(self):
        return "Milestones Page"

class FoundingStory(models.Model):
    page = models.OneToOneField(MilestonePage, on_delete=models.CASCADE, related_name="founding_story")
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='milestones/founding/', blank=True, null=True)

    def __str__(self):
        return self.title

class FoundingPoint(models.Model):
    story = models.ForeignKey(FoundingStory, on_delete=models.CASCADE, related_name='points')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class MilestoneEvent(models.Model):
    page = models.ForeignKey(MilestonePage, on_delete=models.CASCADE, related_name="timeline")
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.year} - {self.title}"

class MilestoneAchievement(models.Model):
    page = models.ForeignKey(MilestonePage, on_delete=models.CASCADE, related_name="achievements")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


# --- VISION & MISSION ---
class VisionMissionPage(models.Model):
    hero_title = models.CharField(max_length=255)
    hero_description = models.TextField()
    intro = models.TextField()

    def __str__(self):
        return "Vision & Mission Page"

class VisionMissionBlock(models.Model):
    BLOCK_CHOICES = [
        ('vision', 'Vision'),
        ('mission', 'Mission'),
    ]
    page = models.ForeignKey(VisionMissionPage, on_delete=models.CASCADE, related_name='blocks')
    block_type = models.CharField(max_length=10, choices=BLOCK_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='vision-mission/', blank=True, null=True)

    def __str__(self):
        return f"{self.get_block_type_display()} - {self.title}"

class VisionMissionPoint(models.Model):
    block = models.ForeignKey(VisionMissionBlock, on_delete=models.CASCADE, related_name='points')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class CompanyValue(models.Model):
    page = models.ForeignKey(VisionMissionPage, on_delete=models.CASCADE, related_name='values')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# --- INVESTMENTS ---
# --- INVESTMENTS (Refactored like Environment) ---
class InvestmentPage(models.Model):
    hero_title = models.CharField(max_length=255)
    hero_description = models.TextField()
    intro = models.TextField()

    def __str__(self):
        return "Investment Page"

class InvestmentBlock(models.Model):
    BLOCK_CHOICES = [
        ('fleet', 'Fleet Modernization Program'),
        ('infrastructure', 'Infrastructure Development'),
    ]
    page = models.ForeignKey(InvestmentPage, on_delete=models.CASCADE, related_name='blocks')
    block_type = models.CharField(max_length=20, choices=BLOCK_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='investments/', blank=True, null=True)

    def __str__(self):
        return f"{self.get_block_type_display()} - {self.title}"

class InvestmentBlockPoint(models.Model):
    block = models.ForeignKey(InvestmentBlock, on_delete=models.CASCADE, related_name="points")
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


# --- SAFETY ---
class SafetyPolicyPage(models.Model):
    hero_title = models.CharField(max_length=255)
    hero_description = models.TextField()
    intro = models.TextField()

    def __str__(self):
        return "Safety & Policies Page"

class SafetyPolicyItem(models.Model):
    page = models.ForeignKey(SafetyPolicyPage, on_delete=models.CASCADE, related_name='policies')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='safety/', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


# --- TEAM ---
class ManagementTeamPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    page = models.ForeignKey(ManagementTeamPage, on_delete=models.CASCADE, related_name='members')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.title
