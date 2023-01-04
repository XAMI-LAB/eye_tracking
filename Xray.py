#!/usr/bin/python
# -*- coding: UTF-8 -*-
import XrayStudy
from typing import List

class Xray(object):
	def show_xay(self, iD : str) -> None:
		pass

	def show_report(self, iD : str) -> None:
		pass

	def setReport(self, report : str):
		self.__report = report

	def getReport(self) -> str:
		return self.__report

	def setPath(self, path : str):
		self.__path = path

	def getPath(self) -> str:
		return self.__path

	def __init__(self):
		self.__iD : str = None
		"""The Xray ID corresponds to the DICOM filename"""
		self.__report : str = None
		self.__path : str = None
		self.contains : XrayStudy = None
		"""# @AssociationMultiplicity 1"""
		self.unnamed_Radiologist_ = []
		"""# @AssociationMultiplicity 0..*"""

