from music21 import *
from django.http import HttpResponse

fileList =['hen','littleplant', 'pigs','lambs', 'caterpillar', 'littleboy']
wordCount = [26, 26, 28, 40,43, 52]
def parse_lyrics(input):
	input = str(input)
	lyrics = []
	word = ""
	for c in input:
		if c is '-' or (c is ' ' and word.strip() is not ''):
			lyrics.append(word)
			word = ""
		elif c is not ' ':
			word += c
	#append last word
	if word.strip is not '':
		lyrics.append(word)
	return lyrics

def place_lyrics(input):

	newTitle = 'Testing'
	lyrics = parse_lyrics(input)

	#find the matching song
	filename = fileList[-1]
	for i, song in enumerate(fileList):
		if len(lyrics) < wordCount[i]:
			filename = song
			break


	file = converter.parse('static/music/' + filename +'.xml')
	voice = file.parts[0]

	i = 0
	for n in voice.flat.notes:
		if len(lyrics) > i:
			n.lyric = lyrics[i]
			i += 1
		else:
			n.lyric = ""

	#replace the title
	originalTitle = file.metadata.movementName
	fileStr = musicxml.m21ToString.fromMusic21Object(file)
	fileStr = fileStr.replace(originalTitle, newTitle)

	fileStr = fileStr.replace('part-name>MusicXML Part', 'part-name print-object="no">MusicXML Part')

	newFile = open('static/music/result.xml', 'w')
	newFile.write(fileStr)
	newFile.close()


	#file.write("musicxml", "static/music/result.xml")
	
