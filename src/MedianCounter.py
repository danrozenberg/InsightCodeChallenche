import DataManager
import bisect


def proccessFolder(inputFolderPath, outPutFilePath):
	medians = getOnlineMedians(inputFolderPath)
	writeMediansToFile(medians, outPutFilePath)

def getOnlineMedians(inputFolderPath):
	"""returns a list with the ongoing median"""
	medians = []
	streamedValues = []
	manager = DataManager.DataManager()
	for line in manager.streamFolder(inputFolderPath):

		#skip empty lines
		if line == "": continue
		newValue = len(line.split())
		median = updateMedians(newValue, streamedValues)
		medians.append(median)

	return medians

def updateMedians(newValue, oldValues)
	"""Updates the oldValues list and returns the new median.
	we are using a bisecting algorithm to keep the history array sorted.
	This part should be O(log(n)), because it uses binary search.
	unfortunately, insertion should be O(n), and thus does not scale so nicely.
	Better methods exist, but they are significanlty more elaborated.
	TODO: implement a faster online median algorithm"""

	bisect.insort(oldValues, newValue)
	return getMedian(oldValues)

def getMedian(valuesList):
	"""returns the median of a given list"""
	listSize = len(valuesList)

	#odd number of elements:
	if listSize % 2 == 1:
		#remember we are using 0 based lists
		midPoint = ((listSize + 1) / 2) - 1
		median = valuesList[midPoint]
	else:
		#remember we are using 0 based lists
		leftPoint = (listSize / 2) - 1
		rightPoint = (leftPoint + 1)
		median = float(valuesList[leftPoint] + valuesList[rightPoint]) / 2

	return median

def writeMediansToFile(medians, outPutFilePath):
	targetFile = file(outPutFilePath,'w')
	for median in sorted(medians):
		targetFile.write(str(median) + "\n")