#-*- coding:utf-8 -*-

import copy

from . import utils, urls
from .image import Image
from .station import Station
from .stream import Stream

class Broadcast:
	def __init__(self, data):
		self.description = data["synopsis"]
		self.duration = data["mediaCollection"]["embedded"]["_duration"]
		self.emission_date_time = data["broadcastedOn"]
		self.geoblocked = data["geoblocked"]
		self.id = data["id"]
		self.image = Image(data["image"])
		self.program_id = data["show"]["id"]
		self.program = None
		self.station = Station(data["publicationService"])
		self.streams = []
		self.subtitle_url = data["mediaCollection"]["embedded"].get("_subtitleUrl")
		self.title = data["title"]
		
		for stream_info in data["mediaCollection"]["embedded"]["_mediaArray"][0]["_mediaStreamArray"]:
			if stream_info["_quality"] == "auto":
				continue
			self.streams.append(Stream(stream_info))
	
	def json(self):
		d = copy.copy(self.__dict__)
		d["image"] = self.image.json()
		if self.program:
			d["program"] = self.program.json()
		d["station"] = self.station.json()
		d["streams"] = []
		for stream in self.streams:
			d["streams"].append(stream.json())
		
		return d


