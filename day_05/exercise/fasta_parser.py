"""useful modules"""
import os
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt 
import pylab as plb

"""test if a path exists"""
def is_path(s):
    try:
        open(s)
        return True
    except IOError:
        return False



class FastaParser(object):
	def __init__(self,path=""):
		import os
		import numpy as np
		import matplotlib.mlab as mlab
		import matplotlib.pyplot as plt 
		import pylab as plb
		self.path=path
		if type(self.path)!=str or len(self.path)==0:
			raise TypeError ("FastaParser requires one argument in teh form of a .fasta file path")

		elif is_path(self.path)==False:
			raise IOError("Incorrect file or directory")

		"""open file and import in a list"""
		dumm=open(self.path)
		data=dumm.readlines()
		"""don't like the automatic separation so I merge everything in one string"""
		stringall=""
		for row in data:
			stringall+=row
		"""now I separate according to *>*"""
		pars0=stringall.split(">")
		"""now I create a list of list, each sublist containintwo elments, the gene name first
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
		"""now I can count sequences in the file i.e. elements in parsed and make it an attribute of the class"""
		self.count=len(parsed)
		"""now I create an list output with just sequences"""
		self.out=[]
		for elem in parsed:
			self.out=self.out+[elem[1]]	
		"""and a dictionnary output with sequences and names"""
		self.dicout={}
		for elem in parsed:
			self.dicout[elem[0]]=elem[1] 			

	"""the list object"""
	def __getitem__(self,key):
		if type(key)==int:
			return self.out[key]
		elif type(key)==str:
			return self.dicout[key]

	"""defines the length"""
	def __len__(self):
		return self.count

	"""methods"""
	"""create a list of the sequences shorter or equal to x"""
	def extract_length(self,x):
		shorties=[]
		for elem in self.out:
			if len(elem)<=x:
				shorties+=[elem]
		return shorties

	"""create a figure and save it under the given name and path"""	
	def length_dist(self,pat):
		savedir=os.getcwd()
		os.mkdir(pat.split("/")[1])
		os.chdir(pat.split("/")[1])
		dists=[]
		for elem in self.out:
			dists+=[len(elem)]
		plt.hist(dists)
		plt.savefig(pat.split("/")[-1],pad_inches=0.1)
		plt.close()
		os.chdir(savedir)

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
