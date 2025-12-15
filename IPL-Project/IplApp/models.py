from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Franchise(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    founded_year = models.IntegerField()
    no_of_trophies = models.IntegerField()
    logo = models.ImageField(upload_to='franchise_logos/', blank=True, null=True)
    city = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)

    class Meta:
        db_table = 'franchises'

    def __str__(self):
        return f"{self.name} ({self.short_name})"

class Player(models.Model):
    ROLE_CHOICES = [
        ('Batsman', 'Batsman'),
        ('Bowler', 'Bowler'),
        ('All-Rounder', 'All-Rounder'),
        ('Wicket-Keeper', 'Wicket-Keeper'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    nationality = models.CharField(max_length=50)
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='player_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.role})"

class Stadium(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    home_team = models.ForeignKey(Franchise, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"