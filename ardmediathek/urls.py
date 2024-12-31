#-*- coding:utf-8 -*-

API_BASE = "https://api.ardmediathek.de/page-gateway/"
PROGRAMS_A_TO_Z = API_BASE + "pages/ard/editorial/experiment-a-z?embedded=false"
EDITORIAL = API_BASE + "widgets/ard/editorials/{id}?pageNumber={page}&pageSize={page_size}&embedded=true"
GROUPING = API_BASE + "pages/dreisat/grouping/{id}?embedded=true"
ASSET = API_BASE + "widgets/dreisat/asset/{id}?pageNumber={page}&pageSize={page_size}&embedded=true&seasoned=false&seasonNumber=&withAudiodescription=false&withOriginalWithSubtitle=false&withOriginalversion=false&single=false"

def make_editorial_url(id, page, page_size):
	return EDITORIAL.format(id=id, page=page, page_size=page_size)

def make_grouping_url(id):
	return GROUPING.format(id=id)

def make_asset_url(id, page, page_size):
	return ASSET.format(id=id, page=page, page_size=page_size)

