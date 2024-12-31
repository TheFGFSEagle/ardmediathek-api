#-*- coding:utf-8 -*-

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
		self.image = Image(data["image"])
		self.program = utils.get_json(urls.make_grouping_url(data["show"]["id"]))
		self.station = Station(data["publicationService"])
		self.streams = []
		self.subtitle_url = data["mediaCollection"]["embedded"].get("_subtitleUrl")
		self.title = data["title"]
		
		for stream_info in data["mediaCollection"]["embedded"]["_mediaArray"][0]["_mediaStreamArray"]:
			if stream_info["_quality"] == "auto":
				continue
			self.streams.append(Stream(stream_info))

