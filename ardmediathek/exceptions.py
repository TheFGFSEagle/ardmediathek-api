#-*- coding:utf-8 -*-

class BaseException(Exception):
	pass

class InvalidIDException(BaseException):
	def __init__(self, *args, **kwargs):
		self.id = kwargs.pop("id", None)
		super().__init__(*args, **kwargs)

class InvalidBroadcastIDException(InvalidIDException):
	def __repr__(self):
		return f"Invalid broadcast ID: {self.id}"

class InvalidProgramIDException(InvalidIDException):
	def __repr__(self):
		return f"Invalid program ID: {self.id}"

