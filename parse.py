import json	

def Parse():
	with open('output.txt',"r+") as f:
		text = f.readline()

	neWwords = text.split(" ")
	removewords = []

	def MakeLower(word):
		return word.lower().strip(".,")

	words = list(map(MakeLower,neWwords))

	for i in range(len(words)): 
		if words[i] == "one":
			words[i] = "1"
		elif words[i] == "two":
			words[i] = "2"
		elif words[i] == "too":
			words[i] = "2"

	for i in range(len(words)):
		if words[i] == "first" and words[i+1] == "name":
			words[i : i + 1] = [''.join(words[i : i+2])]
			removewords.append(words[i+1])
		if words[i] == "last" and words[i+1] == "name":
			words[i : i + 1] = [''.join(words[i : i+2])]
			removewords.append(words[i+1])
		if words[i] == "id" and words[i+1] == "number":
			words[i : i + 1] = [''.join(words[i : i+2])]
			removewords.append(words[i+1])
		if words[i] == "main" and words[i+1] == "concern":
			words[i : i + 1] = [''.join(words[i : i+2])]
			removewords.append(words[i+1])
		if words[i] == "scenario" and words[i+1] == "detailed":
			words[i : i + 1] = [''.join(words[i : i+2])]
			removewords.append(words[i+1])
		if words[i] == "important" and words[i+1] == "metrics":
			words[i : i + 1] = [''.join(words[i : i+2])]
			removewords.append(words[i+1])
		if words[i] == "scenario" and words[i+1] == "detailed":
			words[i : i + 1] = [''.join(words[i : i+2])]
			removewords.append(words[i+1])
		if words[i] == "conscienceness" and words[i+1] == "level" and words[i+2] == "1":
			words[i : i + 1] = [''.join(words[i : i+3])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
		if words[i] == "conscienceness" and words[i+1] == "level" and words[i+2] == "2":
			words[i : i + 1] = [''.join(words[i : i+3])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
		if words[i] == "breaths" and words[i+1] == "per" and words[i+2] == "minute" and words[i+3] == "1":
			words[i : i + 1] = [''.join(words[i : i+4])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
			removewords.append(words[i+3])
		if words[i] == "breaths" and words[i+1] == "per" and words[i+2] == "minute" and words[i+3] == "2":
			words[i : i + 1] = [''.join(words[i : i+4])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
			removewords.append(words[i+3])
		if words[i] == "breathing" and words[i+1] == "status" and words[i+2] == "1":
			words[i : i + 1] = [''.join(words[i : i+3])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
		if words[i] == "breathing" and words[i+1] == "status" and words[i+2] == "2":
			words[i : i + 1] = [''.join(words[i : i+3])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
		if words[i] == "saturation" and words[i+1] == "1":
			words[i : i + 1] = [''.join(words[i : i+2])]
		if words[i] == "saturation" and words[i+1] == "2":
			words[i : i + 1] = [''.join(words[i : i+2])]
		if words[i] == "pulses" and words[i+1] == "per" and words[i+2] == "minute" and words[i+3] == "1":
			words[i : i + 1] = [''.join(words[i : i+4])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
			removewords.append(words[i+3])
		if words[i] == "pulses" and words[i+1] == "per" and words[i+2] == "minute" and words[i+3] == "2":
			words[i : i + 1] = [''.join(words[i : i+4])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
			removewords.append(words[i+3])
		if words[i] == "strength" and words[i+1] == "of" and words[i+2] == "pulse" and words[i+3] == "1":
			words[i : i + 1] = [''.join(words[i : i+4])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
			removewords.append(words[i+3])
		if words[i] == "strength" and words[i+1] == "of" and words[i+2] == "pulse" and words[i+3] == "2":
			words[i : i + 1] = [''.join(words[i : i+4])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
			removewords.append(words[i+3])
		if words[i] == "pulse" and words[i+1] == "regularity" and words[i+2] == "1":
			words[i : i + 1] = [''.join(words[i : i+3])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
		if words[i] == "pulse" and words[i+1] == "regularity" and words[i+2] == "2":
			words[i : i + 1] = [''.join(words[i : i+3])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
		if words[i] == "systolic" and words[i+1] == "blood" and words[i+2] == "pressure" and words[i+3] == "1":
			words[i : i + 1] = [''.join(words[i : i+4])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
			removewords.append(words[i+3])
		if words[i] == "systolic" and words[i+1] == "blood" and words[i+2] == "pressure" and words[i+3] == "2":
			words[i : i + 1] = [''.join(words[i : i+4])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
			removewords.append(words[i+3]) 
		if words[i] == "diastolic" and words[i+1] == "blood" and words[i+2] == "pressure" and words[i+3] == "1":
			words[i : i + 1] = [''.join(words[i : i+4])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
			removewords.append(words[i+3])
		if words[i] == "diastolic" and words[i+1] == "blood" and words[i+2] == "pressure" and words[i+3] == "2":
			words[i : i + 1] = [''.join(words[i : i+4])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
			removewords.append(words[i+3]) 
		if words[i] == "glucose" and words[i+1] == "test" and words[i+2] == "1":
			words[i : i + 1] = [''.join(words[i : i+3])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
		if words[i] == "glucose" and words[i+1] == "test" and words[i+2] == "2":
			words[i : i + 1] = [''.join(words[i : i+3])]
			removewords.append(words[i+1])
			removewords.append(words[i+2]) 
		if words[i] == "treatments" and words[i+1] == "given":
			words[i : i + 1] = [''.join(words[i : i+2])]
		if words[i] == "als" and words[i+1] == "level" and words[i+2] == "treatments":
			words[i : i + 1] = [''.join(words[i : i+3])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
		if words[i] == "als" and words[i+1] == "drug" and words[i+2] == "therapy":
			words[i : i + 1] = [''.join(words[i : i+3])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
		if words[i] == "method" and words[i+1] == "of" and words[i+2] == "evacuation":
			words[i : i + 1] = [''.join(words[i : i+3])]
			removewords.append(words[i+1])
			removewords.append(words[i+2])
		if words[i] == "evacuation" and words[i+1] == "destination":
			words[i : i + 1] = [''.join(words[i : i+2])]
		if words[i] == "current" and words[i+1] == "location":
			words[i : i + 1] = [''.join(words[i : i+2])]



	for word in removewords:
		words.remove(word)



	keywords = ['date', 'time', 'firstname', 'lastname', 'idnumber', 'age', 'sex', 'address', 'telephone', 'mainconcern', 'scenariodetailed', 'importantmetrics', 'consciencenesslevel1', 'consciencenesslevel2', 'breathsperminute1', 'breathsperminute2', 'breathingstatus1', 'breathingstatus2', 'saturation1', 'saturation2', 'pulsesperminute1', 'pulsesperminute2', 'strengthofpulse1', 'strengthofpulse2', 'pulseregularity1', 'pulseregularity2', 'systolicbloodpressure1', 'systolicbloodpressure2', 'diastolicbloodpressure1', 'diastolicbloodpressure2', 'glucosetest1', 'glucosetest2', 'allergies', 'temperaturepopr1', 'temperaturepopr2', 'treatmentsgiven', 'alsleveltreatments', 'alsdrugtherapy', 'methodofevacuation', 'evacuationdestination', 'reasonforreferral', 'patientnameanddriversnumber', 'doctorandliscencenumber', 'signature', 'namerefusalofhospitalization', 'idrefusalofhospitalization', 'signaturerefusalofhospitalization', 'currentlocation']


	Data =	{
		"Garbage":"",
		"date":" ",
		"time":" ",
		"firstname": "",
		"lastname":" ",
		"idnumber":" ",
		"age":" ",
		"sex":" ",
		"address":" ",
		"telephone":" ",
		"mainconcern":" ",
		"scenariodetailed":" ",
		"importantmetrics":" ",
		"consciencenesslevel1":" ",
		"consciencenesslevel2":" ",
		"breathsperminute1":" ",
		"breathsperminute2":" ",
		"breathingstatus1":" ",
		"breathingstatus2":" ",
		"saturation1":" ",
		"saturation2":" ",
		"pulsesserminute1":" ",
		"pulsesperminute2":" ",
		"strengthofpulse1":" ",
		"strengthofpulse2":" ",
		"pulseregularity1":" ",
		"pulseregularity2":" ",
		"systolicbloodpressure1":" ",
		"systolicbloodpressure2":" ",
		"diastolicbloodpressure1":" ",
		"diastolicbloodpressure2":" ",
		"glucosetest1":" ",
		"glucosetest2":" ",
		"allergies":" ",
		"temperaturepopr1":" ",
		"temperaturepopr2":" ",
		"treatmentsgiven":" ",
		"alsleveltreatments":" ",
		"alsdrugtherapy":" ",
		"methodofevacuation":" ",
		"evacuationdestination":" ",
		"reasonforreferral":"",
		"patientnameanddriversnumber":"",
		"attendingdoctorandliscencenumber":"",
		"signature":"",
		"namerefusalofhospitalization":"",
		"idrefusalofhospitalization":"",
		"signaturerefusalofhospitalization":"",
		"currentlocation":""
			}

	keyword = "Garbage"
	for word in words:
		index = 0
		if word.lower().strip(".,") in keywords:
			keyword = word.lower().strip(".,")
		else:
			Data[f'{keyword}'] += f" {word}"


	with open("data.json", "w") as outfile:
		json.dump(Data, outfile,indent=0)

	return Data


#Parse()














