import WordCounter
import MedianCounter

"""This module runs the challenge, and is supposed to be run by the run.sh script at the root of the project
TODO: make this runnable even if we call it from somewhere else...must fix relative paths."""
inputFolder = "./wc_input/"
outputFolder = "./wc_output/"

WordCounter.proccessFolder(inputFolder, outputFolder + "wc_result.txt")
MedianCounter.proccessFolder(inputFolder, outputFolder + "med_result.txt")
