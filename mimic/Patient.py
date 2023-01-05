class Patient():
    	
	def init(self, ID, gender, language, marital_status, race, anchor_age, anchor_year, date_of_death, anchor_year_group,admission_dict , xray_study_dict):
		# It is a unique identifier which specifies an individual patient
		self.ID : str = ID
		# It is the genotypical sex of the patient
		self.gender : str = gender
		# 
		self.language : str = language
		# 
		self.marital_status : str = marital_status
		# 
		self.race : str = race
		# It is the patient's age in the anchor_year.
		# If a patient's anchor_age is over 89 in the anchor_year then their anchor_age is set to 91, regardless of how old they actually were.
		self.anchor_age : int = anchor_age
		# It is a shifted year for the patient
		self.anchor_year : int = anchor_year
		# 
		self.date_of_death : str = date_of_death
		# It is a range of years - the patient's anchor_year occurred during this range."
		self.anchor_year_group : str = anchor_year_group
		# a dictionary indicating the multiple admissions of the patient to the hospital
		self.admission_dict : dict = admission_dict
		# 
		self.xray_study_dict : dict = xray_study_dict


 # Getters and Setters --------------------------------------------
	def getID(self) -> str:
		return self.ID

	def setGender(self, gender : str):
		self.gender = gender

	def getGender(self) -> str:
		return self.gender

	def setLanguage(self, language : str):
		self.language = language

	def getLanguage(self) -> str:
		return self.language

	def setMarital_status(self, marital_status : str):
		self.marital_status = marital_status

	def getMarital_status(self) -> str:
		return self.marital_status

	def setRace(self, ethnicity : str):
		self.race = ethnicity

	def getRace(self) -> str:
		return self.race

	def setAnchor_age(self, anchor_age : int):
		self.anchor_age = anchor_age

	def getAnchor_age(self) -> int:
		return self.anchor_age

	def setAnchor_year(self, anchor_year : int):
		self.anchor_year = anchor_year

	def getAnchor_year(self) -> int:
		return self.anchor_year

	def setDate_of_death(self, date_of_death : str):
		self.date_of_death = date_of_death

	def getDate_of_death(self) -> str:
		return self.date_of_death

	def setAnchor_year_group(self, anchor_year_group : str):
		self.anchor_year_group = anchor_year_group

	def getAnchor_year_group(self) -> str:
		return self.anchor_year_group

	def setAdmission_dict(self, admission_dict : dict):
		self.admission_dict = admission_dict

	def getAdmission_dict(self) -> dict:
		return self.admission_dict

	def setXray_study_dict(self, xray_study_dict : dict):
		self.xray_study_dict = xray_study_dict

	def getXray_study_dict(self) -> dict:
		return self.xray_study_dict


