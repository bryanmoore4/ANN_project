from ocrn import dataset as ds
from ocrn import feature as ft
from ocrn import neuralnet as nt
import numpy as np

print "\n \nOCR Prototype: Neural Networks w/ training data and test data \n \n"

n = nt.neuralnet(500,100,1)
print "Neural Network Initialized"

d = ds.dataset(500,1)
print "Training Data Set Initialized"

if d.generateDataSet():
	print "Training Data Set Generated"

if n.loadTrainingData(d.getTrainingDataset()):
	print "Training Data Set loaded"

while(True):
	x = raw_input("q: quit \t t: teach \t e: test \nWhat?\t:\t")
	if x == "q":
		break
	elif x == "t":
		t = int(raw_input("How many times do you want to train your data?\t:\t"))
		n.teach(t)
	elif x == "e":
		e = raw_input("Enter input file, make sure it is the absolute form and NOT in the string form\t:\t")
		x = n.activate(ft.feature.getImageFeatureVector(e))
		print "\nThe highest probability letter from that the image is '"+str(unichr(x))+"'\n"
	else:
		print "Invalid option\n"
