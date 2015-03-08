from collections import defaultdict
import DataManager
import TextCleaner

def proccessFolder(inputFolderPath, outPutFilePath):
	"""creates a count dictionary from words, and then
	saves the result to file"""
	countFromWord = getWordCount(inputFolderPath)
	writeCountToFile(countFromWord, outPutFilePath)

def getWordCount(inputFolderPath):
	countFromWord = defaultdict(int)
	manager = DataManager.DataManager()
	for line in manager.streamFolder(inputFolderPath):

		#skip empty lines
		if line == "": continue

		#add each word to its count
		cleanLine = TextCleaner.clearText(line)
		for word in cleanLine.split():
			countFromWord[word] += 1

	return countFromWord

def writeCountToFile(countFromWord, outPutFilePath):
	targetFile = file(outPutFilePath,'w')
	for word in sorted(countFromWord):
		targetFile.write(word + "\t" + str(countFromWord[word]) + "\n")