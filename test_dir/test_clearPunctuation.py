from unittest import TestCase
from src import TextCleaner


class TestClearPunctuation(TestCase):

	def test_cleanText(self):
		original = "Good morning to you."
		expected = "good morning to you "
		self.assertEquals(expected, TextCleaner.clearText(original))

		original = "It's his car's tires!"
		expected = "it's his car's tires "
		self.assertEquals(expected, TextCleaner.clearText(original))

		original = "HEY!!! Give me this: a high, Five!"
		expected = "hey    give me this  a high  five "
		self.assertEquals(expected, TextCleaner.clearText(original))

