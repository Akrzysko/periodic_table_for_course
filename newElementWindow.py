# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:46:34 2020

@author: ajkrz
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import elementDefs
import pTableDefs
from elementDefs import astatine

wrappedElements = pTableDefs.wrapAllElements()

pTableDefs.elementFormat(wrappedElements)
pTableDefs.periodicTableFormat(wrappedElements)

class elementWindow(QtWidgets.QWidget):
    def __init__(self, elObj):
        super().__init__()
        
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(0)
        
        self.setGeometry(QtCore.QRect(500, 500, 400, 500))
        
        self.EL_BKG_COLOR = elObj.bkgColor
        self.EL_TEXT_COLOR = elObj.textColor
        self.DEFAULT_FONT = "Arial"
        self.DEFAULT_TEXT_COLOR = "color: rgb(255, 255, 255);"
        
        self.setStyleSheet(self.EL_BKG_COLOR)
        
        self.elementName = QtWidgets.QLabel(elObj.name) 
        font = QtGui.QFont()
        font.setFamily(self.DEFAULT_FONT)
        font.setPointSize(60)
        self.elementName.setFont(font)
        self.elementName.setStyleSheet(self.EL_TEXT_COLOR)
        
        self.elementSymbol = QtWidgets.QLabel(elObj.symbol)
        font = QtGui.QFont()
        font.setFamily(self.DEFAULT_FONT)
        font.setPointSize(100)
        self.elementSymbol.setFont(font)
        self.elementSymbol.setStyleSheet(self.EL_TEXT_COLOR)
        
        self.elementNumber = QtWidgets.QLabel(str(elObj.atomicNumber))
        font = QtGui.QFont()
        font.setFamily(self.DEFAULT_FONT)
        font.setPointSize(60)
        self.elementNumber.setFont(font)
        self.elementNumber.setStyleSheet(self.EL_TEXT_COLOR)
        
        self.elAtomicMass = QtWidgets.QLabel(str(elObj.relAtomicMass))
        font = QtGui.QFont()
        font.setFamily(self.DEFAULT_FONT)
        font.setPointSize(60)
        self.elAtomicMass.setFont(font)
        self.elAtomicMass.setStyleSheet(self.EL_TEXT_COLOR)
        
        
     
        layout.addWidget(self.elementNumber)
        layout.addWidget(self.elementSymbol)
        layout.addWidget(self.elementName)
        layout.addWidget(self.elAtomicMass)
        
        self.setLayout(layout)




