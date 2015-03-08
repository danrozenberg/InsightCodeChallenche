from unittest import TestCase
from src import DataManager

class TestStreamFolder(TestCase):

	def test_streamFolder(self):
		manager = DataManager.DataManager()
		wordList = []
		for line in manager.streamFolder("./FolderToStream/"):
			if line == "\n": continue
			for word in str.rstrip(line).split():
				wordList.append(word.lower())

		#the answer list:
		answerList = ["good", "morning", "sunshine.", "testing", "is", "fun!"
			,"the", "third", "file.", "it", "is", "a", "little", "different.", "but", "it's", "still", "small."]

		#the order doesn't matter for this test, so we sort
		wordList.sort()
		answerList.sort()

		self.assertEquals(wordList, answerList, "Lists are not equal")
