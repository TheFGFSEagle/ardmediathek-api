#-*- coding:utf-8 -*-

import copy

class Stream:
	def __init__(self, data):
		self.width = data["_width"]
		self.height = data["_height"]
		self.url = data["_stream"]
		self.quality = data["_quality"]
	
	def json(self):
		d = copy.copy(self.__dict__)
		return d

