#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class Constants(object):
	"""Extends from Pythons Enum class"""
	def __init__(self):
		self.__dATASET_PATH : str = None
		self.__cOLS : dict = None
		"""COLS = { "butter": [ '#fce94f',
		'#edd400',
		'#c4a000'],
		"orange": [ '#fcaf3e',
		'#f57900',
		'#ce5c00'],
		"chocolate": [ '#e9b96e',
		'#c17d11',
		'#8f5902'],
		"chameleon": [ '#8ae234',
		'#73d216',
		'#4e9a06'],
		"skyblue": [ '#729fcf',
		'#3465a4',
		'#204a87'],
		"plum": [ '#ad7fa8',
		'#75507b',
		'#5c3566'],
		"scarletred":[ '#ef2929',
		'#cc0000',
		'#a40000'],
		"aluminium": [ '#eeeeec',
		'#d3d7cf',
		'#babdb6',
		'#888a85',
		'#555753',
		'#2e3436'],
		}"""
		self.__fONT : dict = None
		"""FONT = { 'family': 'Ubuntu',
		'size': 12}
		matplotlib.rc('font', **FONT)"""

