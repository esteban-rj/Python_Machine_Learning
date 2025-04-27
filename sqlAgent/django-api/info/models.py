from django.db import models

# Create your models here.
class Pokemon(models.Model):
    CATEGORY_CHOICES = [
        ('SEED', 'Seed'),
        ('LIZARD', 'Lizard'), 
        ('TURTLE', 'Turtle'),
        ('WATER', 'Water'),
        ('FIRE', 'Fire'),
        ('ELECTRIC', 'Electric'),
        ('ROCK', 'Rock'),
        ('POISON', 'Poison'),
        ('FLYING', 'Flying'),
        ('PSYCHIC', 'Psychic'),
        ('BUG', 'Bug'),
        ('RAT', 'Rat')
    ]

    GENRE_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    TYPE_CHOICES = [
        ('PLANT', 'Plant'),
        ('POISON', 'Poison'),
        ('FIRE', 'Fire'),
        ('WATER', 'Water'),
        ('ELECTRIC', 'Electric'),
        ('ROCK', 'Rock'),
        ('GHOST', 'Ghost'),
        ('ICE', 'Ice'),
        ('DRAGON', 'Dragon'),
        ('DARK', 'Dark'),
        ('FAIRY', 'Fairy'),
        ('STEEL', 'Steel'),
        ('FIGHTING', 'Fighting'),
        ('NORMAL', 'Normal'),
        ('GROUND', 'Ground'),
        ('PSYCHIC', 'Psychic'),
        ('BUG', 'Bug'),
        ('DARK', 'Dark'),
        ('EARTH', 'Earth'),
    ]

    height = models.FloatField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    name = models.CharField(max_length=255, primary_key=True)
    
    # Many-to-many fields for types and weaknesses
    types = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES
    )
    weaknesses = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES
    )

    def __str__(self):
        return f"Pokemon {self.name}"

