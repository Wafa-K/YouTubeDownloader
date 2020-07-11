import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import os
from os import path

import sys
import pafy
import humanize

import urllib.request

FROM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"main.ui"))

class MainApp(QMainWindow , FROM_CLASS):
    def __init__(self, parent=None):
        super(MainApp,self). __init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()


    def Handel_UI(self):
        self.setWindowTitle('YouTube Downloader')
        self.setFixedSize(583,264)


    def Handel_Buttons(self):
        self.pushButton_3.clicked.connect(self.Quality)
        self.pushButton.clicked.connect( self.Download )
        self.pushButton_2.clicked.connect( self.Handel_Browse )

    def Handel_Browse(self):
        save= QFileDialog.getExistingDirectory(self, "Select Download Directory")
        self.lineEdit_2.setText(save)


    def Quality(self):
        video_link = self.lineEdit.text()
        v = pafy.new(video_link)
        st= v.videostreams
        #print(st)

        for s in st:
            size = humanize.naturalsize(s.get_filesize())
            data = '{} {} {} {}'.format(s.mediatype , s.extension , s.quality, size)
            self.comboBox.addItem(data)

    def Download(self):
        video_link = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        v = pafy.new( video_link )
        st = v.videostreams
        quality= self.comboBox.currentIndex()

        down= st[quality].download(filepath=save_location)

        QMessageBox.information(self, "Download Complete", " Download Complete")
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.comboBox.clear()



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
