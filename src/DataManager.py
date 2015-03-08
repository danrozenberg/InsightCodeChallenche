import os

class DataManager():

	def fileStreamer(self, filePath):
		"""streams a file line by line"""
		for line in open(filePath):
			yield line

	def streamFolder(self, folderPath):
		"""given a folder path, start streaming file lines, file by file"""
		dirContents =  os.listdir(folderPath)
		for filePath in dirContents:
			if not filePath.endswith(".txt"):
				continue
			for line in self.fileStreamer(folderPath + filePath):
				yield line
