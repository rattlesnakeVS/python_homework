#!/usr/bin/env python

"""
Python course EBC 2016
Day 4 - Exercise instructions
Lucas Sinclair <lucas.sinclair@me.com>

* Write a program in a file called "exercise_day4.py"
* You have until the start of the next course at 13h00
tomorrow to finish it.
* Once the program is done, upload it in your github repository
"python_homework" in a directory named "day4".

The program should read the file named "lulu_mix_16.csv". This file 
should be placed in your "home" directory. Your program should use the
 OS environment variable "$HOME" to find the file.
This file is a comma separated values format. It contains information
 about different music tracks.

For each line in the file (excluding the header) the program should
 produce a new "Song" instance. It should place all the Song instances
  created in a list called "songs".

### Each Song object should have these attributes:

* title
The title of the song as a string.

* artist
The artist of the song as a string.

* duration
The duration of the song as an integer in seconds.

When creating new Song instances:

-> If the duration of a song is not a number, set it to 0, but issue 
a warning.
-> If the duration of a song is negative, raise an Exception and stop
 the program.

### Each Song object should have these methods:

* pretty_duration(self)
Returns a nice string describing the duration. For instance if the
duration is 3611, this methods takes no input and returns "01 hours 
00 minutes 11 seconds" as a string.

* play(self)
Automatically opens a webpage on your computer with a youtube search
 for the title.

Once your program is ready the following four lines of code should
 run without errors. (After you have removed the negative duration song!).
"""

songs = None # TODO

for s in songs: print s.artist
for s in songs: print s.pretty_duration()
print sum(s.duration for s in songs), "seconds in total"
songs[6].play_with_yout()

"""**********************************************"""
"""import modules and select dir"""
import warnings
import webbrowser as wb
import os
os.chdir("C:\\Users\\non\\Desktop\\pythoncourse\\python_ebc_2016\\day_04\\exercise")

"""read data"""
dumm=open('lulu_mix_16.csv')
playlist=dumm.readlines()
"""turn the data in a nicest form"""
playlist2=[]
for song in playlist:
	playlist2=playlist2+[[song.split(",")[0],song.split(",")[1],song.split(",")[2]]]


"""test the instance of an integer in a string, will be useful to define the class 
Song and check duration is in the right format although it is a string"""
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

"""define the class song"""
class Song(object):
	def __init__(self,title="",artist="",duration=""): #constructor
		self.title=title
		self.artist=artist
		self.duration=duration
		if is_number(self.duration)==False :
			self.duration=0
			warnings.warn("Warning, duration is not in the right format and will be set to 0")
		else:
			self.duration=int(self.duration)
		if self.duration<0:
			raise Exception("error negative duration")
	def pretty_duration(self):
		hs=self.duration/3600
		ms=(self.duration-(3600*hs))/60
		ss=(self.duration-(3600*hs))-(60*ms)
		print "Song duration:",hs,"hours ",ms,"minutes ",ss,"seconds, thank you very much!"
	def play_with_yout(self):
		wb.open("https://www.youtube.com/results?search_query="+self.title)



"""create Song objects from data and place them in the list songs"""
songs=[]
for song in playlist2:
	songs=songs+[Song( song[0], song[1] , song[2])]


"""remove songs wth negqtive duration from original data"""
for song in playlist2:
	if is_number(song[2])==True:
		if int(song[2])<0:
			song[2]=-int(song[2])

"""create songs again"""
songs=[]
for song in playlist2:
	songs=songs+[Song( song[0], song[1] , song[2])]



"""run the given code"""
songs = None # I had to exclude that line because if songs is an object of
 			 # type None I can't iterate on it!

for s in songs: print s.artist
for s in songs: print s.pretty_duration()
print sum(s.duration for s in songs), "seconds in total"
songs[6].play_with_yout()
