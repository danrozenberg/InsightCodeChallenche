import WordCounter
import MedianCounter

inputFolder = "../wc_input/"
outputFolder = "../wc_output/"

WordCounter.proccessFolder(inputFolder, outputFolder + "wc_result.txt")
MedianCounter.proccessFolder(inputFolder, outputFolder + "med_result.txt")
