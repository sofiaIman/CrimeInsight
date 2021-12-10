from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class sf_crimes(models.Model):
    Area_Name = models.CharField(max_length=140)
    Year = models.CharField(max_length=140)
    Total = models.CharField(max_length=140)
    Arson = models.CharField(max_length=10,null=True)
    Assault = models.CharField(max_length=10,null=True)
    Bad_Checks = models.CharField(max_length=10,null=True)
    Bribery = models.CharField(max_length=10,null=True)
    Bulgary = models.CharField(max_length=10,null=True)
    Disorderly_Conduct = models.CharField(max_length=10,null=True)
    Driving_Under_Influence = models.CharField(max_length=10,null=True)
    Drug = models.CharField(max_length=10,null=True)
    Drunkedness = models.CharField(max_length=10,null=True)
    Embezzlement = models.CharField(max_length=10,null=True)
    Extortion = models.CharField(max_length=10,null=True)
    Family_Offenses = models.CharField(max_length=10,null=True)
    Forgery = models.CharField(max_length=10,null=True)
    Fraud = models.CharField(max_length=10,null=True)
    Gambling = models.CharField(max_length=10,null=True)
    Kidnapping = models.CharField(max_length=10,null=True)
    Theft = models.CharField(max_length=10,null=True)
    Liquor_Laws = models.CharField(max_length=10,null=True)
    Loitering= models.CharField(max_length=10,null=True)
    Missing_Person = models.CharField(max_length=10,null=True)
    NonCriminal = models.CharField(max_length=10,null=True)
    Other_Offenses = models.CharField(max_length=10,null=True)
    Porn = models.CharField(max_length=10,null=True)
    Prostitution = models.CharField(max_length=10,null=True)
    Recovered_Vehicle = models.CharField(max_length=10,null=True)
    Robbery = models.CharField(max_length=10,null=True)
    Runaway = models.CharField(max_length=10,null=True)
    Secondary_Code = models.CharField(max_length=10,null=True)
    Sex_Offense = models.CharField(max_length=10,null=True)
    Stolen_Property = models.CharField(max_length=10,null=True)
    Suicide = models.CharField(max_length=10,null=True)
    Suspicious_Occ = models.CharField(max_length=10,null=True)
    Trea = models.CharField(max_length=10,null=True)
    Tresspass = models.CharField(max_length=10,null=True)
    Vandalism = models.CharField(max_length=10,null=True)
    Vehicle_Theft = models.CharField(max_length=10,null=True)
    Warrants = models.CharField(max_length=10,null=True)
    Weapon_Law = models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return self.Area_Name
    

DAYS = (  
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
     )


LOCATIONS = (  
    ('BAYVIEW', 'BAYVIEW'),
    ('CENTRAL', 'CENTRAL'),
    ('INGLESIDE', 'INGLESIDE'),
    ('MISSION', 'MISSION'),
    ('NORTHERN', 'NORTHERN'),
    ('PARK', 'PARK'),
    ('RICHMOND', 'RICHMOND'),
    ('SOUTHERN', 'SOUTHERN'),
    ('TARAVAL', 'TARAVAL'),
    ('TENDERLOIN', 'TENDERLOIN'),
      )

class sanfran(models.Model):  
            Day = models.CharField(max_length=10, choices=DAYS)
            Location = models.CharField(max_length=20, choices=LOCATIONS)


