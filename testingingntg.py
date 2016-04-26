from ocrn import dataset as ds
from ocrn import feature as ft
from ocrn import neuralnet as nt
from ocrn import percentage
import numpy as np
import main2


n = nt.neuralnet(100,100,1)
d = ds.dataset(100,1)
d.generateDataSet()
n.loadTrainingData(d.getTrainingDataset())
while(True):
    x = raw_input("q: quit \t t: teach \t e: test \nWhat?\t:\t")
    if x == "q":
        break
    elif x == "t":
        gen_num = 500
        n.teach(gen_num)
        print percentage(n.teach(gen_num))
    elif x == "e":
        name = 'C:/Users/bryanmoo/Documents/Python Scripts/OCR_Neural_Network_V1.1/data/trainingdata/00011_2014_03_25_19_02_50_torsey__b.png'
        test_result = n.activate(ft.feature.getImageFeatureVector(name))
        print test_result
        test_result = "\nThe highest probability letter from that the image is '"+str(unichr(test_result))+"'\n"
        print test_result


#def file_open(self):
#    name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
#    self.lineEdit.setText(name)
#    test_result = main2.test(str(name))
#    test_result = "\nThe highest probability letter from that the image is '"+str(unichr(test_result))+"'\n"
#    print self.Generations_display.append(test_result)
#    #PUT NAME INOT THE FILE EDIT INPUT ##
##        with file:
##            text = file.read()
##            self.textEdit.setText(text)
#
#def generations(self):
#    gen_num = QtGui.QInputDialog.getInteger(self, '# of Generations',"Enter your # of generations")
#    gen_num = gen_num[0]
#    main2.teach(gen_num)
#    f = open('data_1.txt','r')
#    for i in f:
#        p = i.split(' ')
#        self.Generations_display.append(p[0] + ' : ' + p[2])
#    f.close()