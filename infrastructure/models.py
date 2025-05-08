from django.db import models

# -------- Terminal Automation --------

class AutomationPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_description = models.TextField()
    overview_title = models.CharField(max_length=255)
    overview_description = models.TextField()
    benefits_title = models.CharField(max_length=255)
    benefits = models.JSONField()
    overview_image = models.ImageField(upload_to='infrastructure/automation/')

    def __str__(self):
        return "Automation Page"

class AutomationSystem(models.Model):
    page = models.ForeignKey(AutomationPage, related_name='systems', on_delete=models.CASCADE)
    system_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    features = models.JSONField()
    image = models.ImageField(upload_to='infrastructure/automation/systems/')

    def __str__(self):
        return self.title

# -------- Fire Fighting --------

class FirePage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_text = models.TextField()
    overview_title = models.CharField(max_length=255)
    overview_text = models.TextField()
    list_title = models.CharField(max_length=255)
    overview_items = models.JSONField()
    overview_image = models.ImageField(upload_to='infrastructure/fire/')

    def __str__(self):
        return "Fire Fighting Page"

class FireSystem(models.Model):
    page = models.ForeignKey(FirePage, related_name='systems', on_delete=models.CASCADE)
    system_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    features = models.JSONField()
    image = models.ImageField(upload_to='infrastructure/fire/systems/')

    def __str__(self):
        return self.title

class AutoModeStep(models.Model):
    page = models.ForeignKey(FirePage, related_name='auto_mode_steps', on_delete=models.CASCADE)
    step = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['step']

    def __str__(self):
        return f"Step {self.step}: {self.title}"

class FireTraining(models.Model):
    page = models.OneToOneField(FirePage, related_name='training', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    items = models.JSONField()
    image = models.ImageField(upload_to='infrastructure/fire/training/')

    def __str__(self):
        return "Fire Training"

# -------- Power Backup --------

class PowerPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_text = models.TextField()
    critical_systems = models.JSONField()

    def __str__(self):
        return "Power Backup Page"

class PowerSystem(models.Model):
    page = models.ForeignKey(PowerPage, related_name='systems', on_delete=models.CASCADE)
    system_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.CharField(max_length=255)
    response_time = models.CharField(max_length=255)
    image = models.ImageField(upload_to='infrastructure/power/systems/')

    def __str__(self):
        return self.title

class PowerDistribution(models.Model):
    page = models.OneToOneField(PowerPage, related_name='distribution', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    text = models.TextField()
    features = models.JSONField()
    image = models.ImageField(upload_to='infrastructure/power/distribution/')

    def __str__(self):
        return "Power Distribution"

class PowerMaintenanceStep(models.Model):
    page = models.ForeignKey(PowerPage, related_name='maintenance_steps', on_delete=models.CASCADE)
    step = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['step']

    def __str__(self):
        return f"Step {self.step}: {self.title}"

# -------- Storage --------

class StoragePage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_prefix = models.CharField(max_length=255)
    intro_suffix = models.CharField(max_length=255)

    def __str__(self):
        return "Storage Page"

class StorageTank(models.Model):
    page = models.ForeignKey(StoragePage, related_name='tanks', on_delete=models.CASCADE)
    tank_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    features = models.JSONField()
    image = models.ImageField(upload_to='infrastructure/storage/tanks/')

    def __str__(self):
        return self.name

class StorageSafetyBlock(models.Model):
    page = models.ForeignKey(StoragePage, related_name='safety_blocks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title

# -------- Truck Loading --------

class TruckLoadingPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    config_note = models.CharField(max_length=255)
    average_rate = models.CharField(max_length=100)
    truck_count = models.CharField(max_length=100)
    intro_image = models.ImageField(upload_to='infrastructure/truck-loading/')

    def __str__(self):
        return "Truck Loading Page"

class LoadingBay(models.Model):
    page = models.ForeignKey(TruckLoadingPage, related_name='bays', on_delete=models.CASCADE)
    bay_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    loading_rate = models.CharField(max_length=100)
    features = models.JSONField()

    def __str__(self):
        return self.name

class LoadingProcessStep(models.Model):
    page = models.ForeignKey(TruckLoadingPage, related_name='process_steps', on_delete=models.CASCADE)
    step = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['step']

    def __str__(self):
        return f"Step {self.step}: {self.title}"

class TruckLoadingSafety(models.Model):
    page = models.OneToOneField(TruckLoadingPage, related_name='safety', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    safety_list = models.JSONField()
    efficiency_list = models.JSONField()

    def __str__(self):
        return "Truck Loading Safety"

# -------- Vessel Fleet --------

class VesselPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    intro_title = models.CharField(max_length=255)
    intro_text = models.TextField()
    overview_title = models.CharField(max_length=255)
    overview_text = models.TextField()
    overview_list = models.JSONField()
    overview_image = models.ImageField(upload_to='infrastructure/vessels/')

    def __str__(self):
        return "Vessel Fleet Page"

class VesselFeature(models.Model):
    page = models.ForeignKey(VesselPage, related_name='features', on_delete=models.CASCADE)
    feature_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class VesselSpec(models.Model):
    page = models.ForeignKey(VesselPage, related_name='specs', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=[("technical", "Technical"), ("safety", "Safety")])

    def __str__(self):
        return f"{self.label} ({self.type})"

class VesselCrew(models.Model):
    page = models.OneToOneField(VesselPage, related_name='crew', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()

    def __str__(self):
        return "Vessel Crew"

class VesselCrewStat(models.Model):
    crew = models.ForeignKey(VesselCrew, related_name='stats', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.label
