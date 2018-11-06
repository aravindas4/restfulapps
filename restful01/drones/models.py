from django.db import models


class DroneCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        db_table = 'drone_category'
        verbose_name_plural = "DroneCategories"

    def __str__(self):
        return self.name


class Drone(models.Model):
    name = models.CharField(max_length=250)
    drone_category = models.ForeignKey(
        DroneCategory,
        related_name='drones',
        on_delete=models.CASCADE
    )
    manufacturing_date = models.DateTimeField()
    has_it_completed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        db_table = "drone"

    def __str__(self):
        return self.name


class Pilot(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    name = models.CharField(max_length=150, blank=False, default='')
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    races_count = models.PositiveIntegerField(default=0)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        db_table = 'pilots'

    def __str__(self):
        return self.name


class Competition(models.Model):
    pilot = models.ForeignKey(
        Pilot,
        related_name="competitions",
        on_delete=models.SET_NULL,
        null=True
    )
    drone = models.ForeignKey(
        Drone,
        related_name="competated_in",
        on_delete=models.SET_NULL,
        null=True
    )
    distance_in_feet = models.PositiveIntegerField(default=0)
    distance_achievement_date = models.DateField()

    class Meta:
        ordering = ('-distance_in_feet',)
        db_table = "competition"
