import os
import sys
from PyQt4 import QtGui, QtCore
import Layout_OCR_app as design
from ocrn import dataset as ds
from ocrn import feature as ft
from ocrn import neuralnet as nt



class ExampleApp(QtGui.QWidget, design.Ui_Form):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
#        palette = QtGui.QPalette()
#        palette.setBrush(palette.Background,QtGui.QBrush(QtGui.QPixmap("waves.jpg")))        
#        self.setPalette(palette)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setAcceptDrops(True)
        self.progressBar =self.progressBar
        self.Teach.clicked.connect(self.generations)
        self.Open_file.clicked.connect(self.file_open)
        self.Quit.clicked.connect(self.close_app)
        self.n = nt.neuralnet(500,300,100,1)
        self.d = ds.dataset(500,1)
        self.d.generateDataSet()
        self.n.loadTrainingData(self.d.getTrainingDataset())
        self.setWindowIcon(QtGui.QIcon('wolf.png'))
        self.setWindowTitle("OCR GUI by Bryan Moore")
        self.construct.clicked.connect(self.skelton)
        
        
    def skelton(self):
        layers = QtGui.QInputDialog.getInteger(self, '# of layers',"Enter your # of Layers \nincluding input but not output")
        layers = layers[0]
        size_layers = []
        size_layers.extend([0]*layers)
        for i in range(len(size_layers)):
            size_layers[i] = QtGui.QInputDialog.getInteger(self, 'Size of layer',"Enter the size of Layer each layer")[0]
        size_layers.append(1)
        size_layers.insert(0,500)
        self.n = nt.neuralnet(*size_layers)
        self.d = ds.dataset(size_layers[0],1)
        self.d.generateDataSet()
        self.n.loadTrainingData(self.d.getTrainingDataset())
        

        
    def print_progress(self,iterable,gen_num):
        self.b = (float(iterable)/float(gen_num))*100
        if self.b%1==0:
            self.progressBar.setValue(self.b)
            
    def Teacher(self,gen_num):
        self.Number_gen.setText(str(gen_num))
        for i in range(1,gen_num+1):
            self.Generations_display.append(str(i) + " : " + str(self.n.trainer.train()))
            self.print_progress(i,gen_num)
        
    def Tester(self,filename):
        self.test_result = self.n.activate(ft.feature.getImageFeatureVector(str(filename)))
        self.test_result = "\nThe highest probability letter from that the image is '"+str(unichr(self.test_result))+"'\n"
        self.Generations_display.append(self.test_result)
    
    def close_app(self):
        choice = QtGui.QMessageBox.question(self, 'Quit Window',
                                            "Do you want to quit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Quit intialized!")
            sys.exit()
        else:
            pass


        
    def file_open(self):
        self.name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        self.lineEdit.setText(self.name)
        self.test_result = str(self.Tester(self.name))
#        print self.test_result
#        print self.Generations_display.append(self.test_result)
        
        
    
    def generations(self):
        gen_num = QtGui.QInputDialog.getInteger(self, '# of Generations',"Enter your # of generations")
        gen_num = gen_num[0]
        self.Teacher(gen_num)
        


def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
