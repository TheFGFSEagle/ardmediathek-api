# -*- coding: utf-8 -*-

import math
import requests
import requests_cache

from . import urls, utils
from .program import Program

requests_cache_backend = requests_cache.backends.filesystem.FileCache("~/.cache/ardmediathek-api/", )
requests_cache.install_cache("ardmediathek", backend=requests_cache_backend)

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

def get_program(id):
	return Program(utils.get_json(urls.make_grouping_url(id)))

