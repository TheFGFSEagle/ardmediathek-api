# -*- coding: utf-8 -*-

import unittest

import ardmediathek

class TestARDMediathek(unittest.TestCase):
	def test_get_programs(self):
		print("Getting programs ...")
		programs = ardmediathek.get_programs()
		print("done")
		self.assertGreater(len(programs), 2000)
		self.assertNotEqual(programs[0].title, "")
		self.assertNotEqual(programs[0].description, "")
		print("Getting broadcasts of first program ...")
		broadcasts = programs[0].get_broadcasts()
		print("done")
		
		print("Getting program by id ...")
		program = ardmediathek.get_program("Y3JpZDovL25kci5kZS80NQ")
		print("done")
		self.assertEqual(program.title, "Expeditionen ins Tierreich")
		print("Getting broadcasts of program ...")
		broadcasts = program.get_broadcasts()
		print("done")
		self.assertGreater(len(broadcasts), 0)
		
		print("Getting broadcast by valid ID ...")
		self.assertTrue(ardmediathek.get_broadcast("Y3JpZDovL25kci5kZS80NV8yMDA4LTA0LTA2LTAzLTUx").title)
		print("done")
		print("Getting broadcast by invalid ID ...")
		with self.assertRaises(AssertionError):
			ardmediathek.get_broadcast("Y3JpZDovL25kci5kZS80NV8yMDA4LTA0LTA2LTAzLTUx000")
		print("done")

if __name__ == "__main__":
	unittest.main()

