# -*- coding: utf-8 -*-

import math
from urllib.parse import urlparse

import requests

from . import urls, utils
from .program import Program
from .broadcast import Broadcast
from . import exceptions

def get_programs():
	programs_info = utils.get_json(urls.PROGRAMS_A_TO_Z)
	programs = []
	for letter_info in programs_info["widgets"]:
		current_page = 0
		total_pages = math.ceil(letter_info["pagination"]["totalElements"] / 100)
		while current_page < total_pages:
			programs += utils.get_json(urls.make_editorial_url(
				letter_info["links"]["self"]["urlId"], current_page, 100
			))["teasers"]
			
			current_page += 1
	
	new_programs = []
	for program in programs:
		if program["type"] != "show":
			#print(program["type"], program["shortTitle"])
			continue
		new_program = utils.get_json(program["links"]["target"]["href"])
		if len(new_program["widgets"]) == 0:
			#print(program["shortTitle"], program["links"])
			continue
		new_programs.append(Program(new_program))
	
	return new_programs

def get_program_api_url(id):
	return urls.make_grouping_url(id)

def get_program(id):
	try:
		json = utils.get_json(get_program_api_url(id))
	except requests.exceptions.HTTPError as e:
		if e.response.status_code == 400:
			raise exceptions.InvalidProgramIDException(id=id)
		else:
			raise e
	
	return Program(json)

def get_broadcast_api_url(id):
	return urls.make_item_url(id)

def get_broadcast(id):
	try:
		json = utils.get_json(get_broadcast_api_url(id))
	except requests.exceptions.HTTPError as e:
		if e.response.status_code == 400:
			raise exceptions.InvalidBroadcastIDException(id=id)
		else:
			raise e
	return Broadcast(json["widgets"][0])

def get_id_from_url(url):
	url_parts = urlparse(url)
	path_parts = list(filter(None, url_parts.path.split("/")))
	if path_parts[0] == "video":
		return "broadcast", path_parts[4]
	else:
		return "program", path_parts[2]

def get_quality_name(quality):
	if quality < 0 or quality > 4:
		return "UNKNOWN"
	quality_names = ["HVGA", "VGA", "DVGA", "HD", "FHD"]
	return quality_names[quality]

