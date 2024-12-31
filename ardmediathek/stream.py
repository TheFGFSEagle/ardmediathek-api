#-*- coding:utf-8 -*-

class Stream:
	def __init__(self, data):
		self.width = data["_width"]
		self.height = data["_height"]
		self.url = data["_stream"]
		self.quality = data["_quality"]

