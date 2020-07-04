# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 09:03:30 2020

@author: ajkrz
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import elementDefs
import pTableDefs 
import newElementWindow

wrappedElements = pTableDefs.wrapAllElements()

pTableDefs.elementFormat(wrappedElements)
pTableDefs.periodicTableFormat(wrappedElements)


class elementButton(QtWidgets.QWidget):
    def __init__(self, elObj):
        super().__init__()
        
        self.DEFAULT_FONT = "Arial"
        self.DEFAULT_FONT_SIZE = 32
        
        self.elObj = elObj
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        self.button = QtWidgets.QPushButton(elObj.symbol)
        self.button.setSizePolicy(QtWidgets.QSizePolicy.Minimum, 
                                    QtWidgets.QSizePolicy.Minimum)
        
        
        self.button.setStyleSheet(f"{elObj.bkgColor} \
                                  {elObj.textColor}" )
                                  
        self.button.setFont(QtGui.QFont(self.DEFAULT_FONT, 
                                        self.DEFAULT_FONT_SIZE))
        self.button.clicked.connect(lambda: self.element_window(self, 
                                                                self.elObj))
        
        layout.addWidget(self.button)

    def element_window(self, checked, elObj):
        self.elWin = newElementWindow.elementWindow(elObj)
        self.elWin.show()


class periodicTable(QtWidgets.QWidget):
    def __init__(self, wrappedElObjs):
        super().__init__()
        
        self.BKG_COLOR = "background-color: black;"
        
        pTableLayout = QtWidgets.QGridLayout()
        self.setStyleSheet(self.BKG_COLOR)
        
        for n, E in enumerate(wrappedElObjs):
            pTableLayout.addWidget(elementButton(E), E.rowPos, E.colPos)
            
        emptyRow1 = QtWidgets.QPushButton()
        pTableLayout.addWidget(emptyRow1, 8, 4)
        
        self.setGeometry(QtCore.QRect(100, 100, 300, 400))
        self.setLayout(pTableLayout)
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    pTable = periodicTable(wrappedElements)
    pTable.show()
    app.exec_()        


if __name__ == "__main__":
    main()
