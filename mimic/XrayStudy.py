#!/usr/bin/python
# -*- coding: UTF-8 -*-
from mimic.Xray import Xray
from mimic.Patient import Patient
from typing import List

class XrayStudy(object):
	def add_xray(self, new_xray : Xray) -> None:
		pass

	def remove_xray(self, xray : Xray) -> None:
		pass

	def getID(self) -> str:
		return self.__iD

	def setXray_lst(self, xray_lst : Xray):
		self.__xray_lst = xray_lst

	def getXray_lst(self) -> Xray:
		return self.__xray_lst

	def __init__(self):
		self.__iD : str = None
		self.__xray_lst : Xray = []
		self.takes : Patient = None
		"""# @AssociationMultiplicity 1"""
		self.unnamed_Xray_ = []
		"""# @AssociationMultiplicity 1..*
		# @AssociationKind Composition"""

