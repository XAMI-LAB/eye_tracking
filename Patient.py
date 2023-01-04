#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Admission
import XrayStudy
from typing import List

class Patient(object):
	def add_admission(self, new_admission : Admission) -> None:
		"""adds an admission record to the patient admission list"""
		pass

	def remove_admission(self, admission : Admission) -> None:
		pass

	def add_xay_study(self, new_xray_study : XrayStudy) -> None:
		pass

	def remove_xray_study(self, xray_study : XrayStudy) -> None:
		pass

	def getID(self) -> str:
		return self.__iD

	def setGender(self, gender : str):
		self.__gender = gender

	def getGender(self) -> str:
		return self.__gender

	def setLanguage(self, language : str):
		self.__language = language

	def getLanguage(self) -> str:
		return self.__language

	def setMarital_status(self, marital_status : str):
		self.__marital_status = marital_status

	def getMarital_status(self) -> str:
		return self.__marital_status

	def setEthnicity(self, ethnicity : str):
		self.__ethnicity = ethnicity

	def getEthnicity(self) -> str:
		return self.__ethnicity

	def setAnchor_age(self, anchor_age : int):
		self.__anchor_age = anchor_age

	def getAnchor_age(self) -> int:
		return self.__anchor_age

	def setAnchor_year(self, anchor_year : int):
		self.__anchor_year = anchor_year

	def getAnchor_year(self) -> int:
		return self.__anchor_year

	def setDate_of_death(self, date_of_death : str):
		self.__date_of_death = date_of_death

	def getDate_of_death(self) -> str:
		return self.__date_of_death

	def setAnchor_year_group(self, anchor_year_group : str):
		self.__anchor_year_group = anchor_year_group

	def getAnchor_year_group(self) -> str:
		return self.__anchor_year_group

	def setAdmission_dict(self, admission_dict : dict):
		self.__admission_dict = admission_dict

	def getAdmission_dict(self) -> dict:
		return self.__admission_dict

	def setXray_study_dict(self, xray_study_dict : dict):
		self.__xray_study_dict = xray_study_dict

	def getXray_study_dict(self) -> dict:
		return self.__xray_study_dict

	def __init__(self):
		self.__iD : str = None
		"""It is a unique identifier which specifies an individual patient"""
		self.__gender : str = None
		"""It is the genotypical sex of the patient"""
		self.__language : str = None
		self.__marital_status : str = None
		self.__ethnicity : str = None
		self.__anchor_age : int = None
		"""It is the patient’s age in the anchor_year.
		If a patient’s anchor_age is over 89 in the anchor_year then their anchor_age is set to 91, regardless of how old they actually were."""
		self.__anchor_year : int = None
		"""It is a shifted year for the patient"""
		self.__date_of_death : str = None
		self.__anchor_year_group : str = None
		"""It is a range of years - the patient’s anchor_year occurred during this range."""
		self.__admission_dict : dict = None
		"""a dictionary indicating the multiple admissions of the patient to the hospital"""
		self.__xray_study_dict : dict = None
		self.unnamed_XrayStudy_ = []
		"""# @AssociationMultiplicity 1..*
		# @AssociationKind Composition"""
		self.unnamed_Admission_ = []
		"""# @AssociationMultiplicity 1..*
		# @AssociationKind Composition"""

