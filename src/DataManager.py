import os

class DataManager():

	def fileStreamer(self, filePath):
		"""This is a simple python generator"""
		for line in open(filePath):
			yield line

	def streamFolder(self, folderPath):
		"""given a folder path, start streaming file by file"""
		dirContents =  os.listdir(folderPath)
		for filePath in dirContents:
			if filePath.endswith(".txt"):
				yield self.fileStreamer(folderPath + filePath)
