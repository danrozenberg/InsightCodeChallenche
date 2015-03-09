from unittest import TestCase
from src import MedianCounter



class TestGetOnlineMedians(TestCase):
	def test_getOnlineMedians(self):
		"""Does email example. Folder has only 1 file"""
		medians  =  MedianCounter.getOnlineMedians("./ExampleFolder/")
		expected = [5,4.5,4.0,4.5]

		for m1, m2 in zip(medians, expected):
			self.assertEquals(m1, m2, "Different medians")
