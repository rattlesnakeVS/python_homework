import os
os.chdir("C:\\Users\\non\\Desktop\\pythoncourse\\python_homework\\day_05\\exercise")

execfile("exercise_day5.py")

import pytest


	"""code inside the fastaparser class"""
	"""open file and import in a list"""
	dumm=open("all_contigs.fasta")
	data=dumm.readlines()

	"""don't like the automatic separation so I merge everything in one string"""
	stringall=""
	for row in data:
		stringall+=row

	"""now I separate according to *>*"""
	pars0=stringall.split(">")

	"""now I create a list of list, each sublist containing two elments, the gene ot contig name first
	and then the sequence"""
	parsed=[]
	for elem in pars0:
		if len(elem)>0:
			seq= elem.split("\n")
			seq.pop(0)
			seqstring=""
			for elem2 in seq:
				seqstring+=elem2
			parsed=parsed+[[ elem.split("\n")[0] , seqstring]]

	"""and a dictionnary output with sequences and names"""
	dicout={}
	for elem in parsed:
		if len(elem)>0:
			dicout[elem[0]]=elem[1] 	

	"""contig numbers"""
	count=len(parsed)


	out=[]
	for elem in parsed:
		out=out+[elem[1]]	

	"""output"""
	return out 




"""methods..."""
def extract_length(x):
	shorties=[]
	for elem in out:
		if len(elem)<=x:
			shorties+=[elem]
	return shorties

"""graph of length distribution"""
def length_dist(pat):
	savedir=os.getcwd()
	os.mkdir(pat.split("/")[1])
	os.chdir(pat.split("/")[1])
	dists=[]
	for elem in out:
		dists+=[len(elem)]
	plt.hist(dists)
	plt.savefig(pat.split("/")[-1],pad_inches=0.1)
	plt.close()
	os.chdir(savedir)



plt.savefig(pat.split("/")[-1],pad_inches=0.1)

pat="~/test/genes_lengths.pdf"


"""test dico"""
dico={"rat":"123","chat":"333"}
dist=[1,2,3,4]
plt.hist(dist)
plt.show()
