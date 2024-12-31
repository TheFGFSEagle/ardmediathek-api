#!/usr/bin/env python
#-*- coding:utf-8 -*-

from .image import Image

class Station:
	def __init__(self, data):
		self.logo = Image(data["logo"])
		self.name = data["name"]
		self.type = data["publisherType"]

