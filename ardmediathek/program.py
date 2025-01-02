#-*- coding:utf-8 -*-

import math

from . import urls, utils
from .broadcast import Broadcast
from .image import Image
from .station import Station

class Program:
	def __init__(self, data):
		self.description = data["synopsis"]
		self.image = Image(data["image"])
		self.station = Station(data["publicationService"])
		self.title = data["title"]
		if len(data["widgets"]) > 0:
			self.id = data["widgets"][0]["links"]["self"]["id"]
			self.num_broadcasts = data["widgets"][0]["pagination"]["totalElements"]
		else:
			self.id = None
			self.num_broadcasts = 0
	
	def get_broadcasts(self):
		broadcasts = []
		current_page = 0
		total_pages = math.ceil(self.num_broadcasts / 100)
		while current_page < total_pages:
			broadcasts += utils.get_json(urls.make_asset_url(
				self.id, current_page, 100
			))["teasers"]
			
			current_page += 1
		
		new_broadcasts = []
		for broadcast in broadcasts:
			print(broadcast["links"]["target"]["href"])
			new_broadcast = Broadcast(utils.get_json(broadcast["links"]["target"]["href"])["widgets"][0])
			new_broadcasts.append(new_broadcast)
		
		return new_broadcasts

