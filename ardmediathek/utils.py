#-*- coding:utf-8 -*-

import requests

def get_json(url):
	r = requests.get(url)
	assert r.ok, f"Could not download API JSON from {url}: error {r.status_code}"
	
	return r.json()

