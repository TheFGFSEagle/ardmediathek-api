#!/usr/bin/env python
#-*- coding:utf-8 -*-

import copy

from .image import Image

class Station:
	def __init__(self, data):
		self.logo = Image(data["logo"])
		self.name = data["name"]
		self.type = data["publisherType"]
	
	def json(self):
		d = copy.copy(self.__dict__)
		d["logo"] = self.logo.json()
		return d

