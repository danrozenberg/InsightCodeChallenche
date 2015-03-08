import  string

def clearPunctuation(text):
	"""Apostrophes are not changed, currently we do not deal with them
	We leave extra spaces because string.split() deals with them for us."""
	"""TODO: deal with apostrophes better"""
	for char in string.punctuation:
		if char <> "'":
			text = text.replace(char, " ")
	return text

def clearText(text):
	text = clearPunctuation(text)
	text = text.lower()
	return text