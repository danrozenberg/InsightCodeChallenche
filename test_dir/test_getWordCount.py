from unittest import TestCase
from src import WordCounter


class TestGetWordCount(TestCase):

	def test_getWordCount(self):
		"""Does email example. Folder has only 1 file"""
		createdDictionary = WordCounter.getWordCount("./ExampleFolder/")
		expected = {"a":1, "big":1, "call":1, "every":2, "everyone":1, "get":1,
					"holler":1, "make":2, "meeting":1, "out":2, "shout":2, "so":1, "who":2}

		for word1, word2 in zip(sorted(expected), sorted(createdDictionary)):
			self.assertEquals(word1, word2, "Different words")
			self.assertEquals(expected[word1], createdDictionary[word2], "Different counts")

		"""Does a folder with more files"""
		createdDictionary = WordCounter.getWordCount("./FolderToStream/")
		expected = {"good":1, "morning":1, "sunshine":1, "testing":1, "is":2, "fun":1,
					"the":1, "third":1, "file":1, "it":1, "a":1, "little":1,
					"different":1, "but":1, "it's":1, "still":1, "small":1}

		for word1, word2 in zip(sorted(expected), sorted(createdDictionary)):
			self.assertEquals(word1, word2, "Different words")
			self.assertEquals(expected[word1], createdDictionary[word2], "Different counts")
