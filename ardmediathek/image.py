#-*- coding:utf-8 -*-

import copy
import io
import os
import requests
import tempfile
from PIL import Image

class Image:
	def __init__(self, data):
		self.description = data["alt"]
		self.producer = data["producerName"]
		self.title = data["title"]
		self.url = data["src"]
	
	def get(self):
		with tempfile.SpooledTemporaryFile(max_size=1e9) as buf:
			r = requests.get(self.url, stream=True)
			if r.status_code == 200:
				for chunk in r.iter_content(chunk_size=1024):
					buf.write(chunk)
				buf.seek(0)
				return Image.open(io.BytesIO(buffer.read()))
	
	def json(self):
		d = copy.copy(self.__dict__)
		return d


