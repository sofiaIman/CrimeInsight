from django.forms import ModelForm
from app.models import sf_crimes

from app.models import sanfran
from django import forms  



class caw(ModelForm):
	class Meta:
		model = sf_crimes
		fields = ['Area_Name','Year','Total','Arson','Assault','Bad_Checks','Bribery','Bulgary','Disorderly_Conduct','Drug','Drunkedness','Embezzlement','Extortion','Family_Offenses','Forgery','Fraud','Gambling','Kidnapping','Theft','Liquor_Laws','Loitering','Missing_Person','NonCriminal','Other_Offenses','Porn','Prostitution','Recovered_Vehicle','Robbery','Runaway','Secondary_Code','Trea','Tresspass','Vandalism','Vehicle_Theft','Warrants','Weapon_Law']




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

class sf(ModelForm):
	Day = forms.ChoiceField(choices=DAYS, required=True )
	location = forms.ChoiceField(choices=LOCATIONS, required=True )

	class Meta:
		model = sanfran
		fields = ['Day','location']