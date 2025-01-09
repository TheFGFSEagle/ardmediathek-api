#-*- coding:utf-8 -*-

import requests_cache

__requests_cache_backend = requests_cache.backends.filesystem.FileCache("~/.cache/ardmediathek-api/")

def get_json(url):
	with requests_cache.session.CachedSession(backend=__requests_cache_backend) as session:
		r = session.get(url)
		r.raise_for_status()
	
	return r.json()

