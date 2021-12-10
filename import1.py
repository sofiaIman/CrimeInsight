import csv,sys,os
os.environ['DJANGO_SETTINGS_MODULE'] = 'practiceapp.settings'
import django
django.setup()
from app.models import sf_crimes
data = csv.reader(open("sf_analysis.csv"),delimiter=',')
for row in data:
	if row[0] != 'Area_Name':

		post = sf_crimes()
		post.Area_Name = row[0]
		post.Year = row[1]
		post.Total = row[2]
		post.Arson = row[3]
		post.Assault = row[4]
		post.Bad_Checks = row[5]
		post.Bribery = row[6]
		post.Bulgary = row[7]
		post.Disorderly_Conduct = row[8]
		post.Driving_Under_Influence = row[9]
		post.Drug = row[10]
		post.Drunkedness = row[11]
		post.Embezzlement = row[12]
		post.Extortion = row[13]
		post.Family_Offenses = row[14]
		post.Forgery = row[15]
		post.Fraud = row[16]
		post.Gambling = row[17]
		post.Kidnapping = row[18]
		post.Theft = row[19]
		post.Liquor_Laws = row[20]
		post.Loitering= row[21]
		post.Missing_Person = row[22]
		post.NonCriminal = row[23]
		post.Other_Offenses = row[24]
		post.Porn = row[25]
		post.Prostitution = row[26]
		post.Recovered_Vehicle = row[27]
		post.Robbery = row[28]
		post.Runaway = row[29]
		post.Secondary_Code = row[30]
		post.Sex_Offense = row[31]
		post.Stolen_Property = row[32]
		post.Suicide = row[33]
		post.Suspicious_Occ = row[34]
		post.Trea = row[35]
		post.Tresspass = row[36]
		post.Vandalism = row[37]
		post.Vehicle_Theft = row[38]
		post.Warrants = row[39]
		post.Weapon_Law = row[40]
		post.save()
