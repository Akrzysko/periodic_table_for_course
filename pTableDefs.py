# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:25:16 2020

@author: ajkrz
"""
import elementDefs
from elementDefs import pElement
from elementDefs import ( hydrogen, helium, lithium,
                          beryllium, boron, carbon, 
                          nitrogen, oxygen, flourine,
                          neon, sodium, magnesium, 
                          aluminum, silicon, phosphorus,
                          sulfur, chlorine, argon,
                          potassium, calcium, scandium,
                          titanium, vanadium, chromium,
                          maganese, iron, cobalt, 
                          nickel, copper, zinc,
                          gallium, germanium, arsenic,
                          selenium, bromine, krypton,
                          rubidium, strontium, yttrium,
                          zirconium, niobium, molybdenum,
                          technetium, ruthenium, rhodium, 
                          palladium, silver, cadmium,
                          indium, tin, antimony,
                          tellurium, iodine, xenon,
                          caesium, barium, lanthanum,
                          cerium, praseodymium, neodymium,
                          promethium, samarium, europium,
                          gadolinum, terbium, dysprosium,
                          holmium, erbium, thulium,
                          ytterbium, lutetium, halfnium,
                          tantalum, tungsten, rhenium,
                          osmium, iridium, platinum,
                          gold, mercury, thallium, 
                          lead, bismuth, polonium,
                          astatine, radon, francium,
                          radium, actinium, thorium,
                          protactinium, uranium, neptunium, plutonium,
                          americium, curium, berkelium,
                          californium, einsteinium, fermium,
                          mendelevium, nobelium, lawrencium,
                          rutherfordium, dubnium, seaborgium,
                          bohrium, hassium, meitnerium,
                          darmstadtium, roentgenium, copernicium,
                          nihonium, flerovium, moscovium,
                          livermorium, tennessine, oganesson
                          
                          )

def wrapAllElements():
    elementsToWrap =  (  hydrogen, helium, lithium,
                          beryllium, boron, carbon, 
                          nitrogen, oxygen, flourine,
                          neon, sodium, magnesium, 
                          aluminum, silicon, phosphorus,
                          sulfur, chlorine, argon,
                          potassium, calcium, scandium,
                          titanium, vanadium, chromium,
                          maganese, iron, cobalt, 
                          nickel, copper, zinc,
                          gallium, germanium, arsenic,
                          selenium, bromine, krypton,
                          rubidium, strontium, yttrium,
                          zirconium, niobium, molybdenum,
                          technetium, ruthenium, rhodium, 
                          palladium, silver, cadmium,
                          indium, tin, antimony,
                          tellurium, iodine, xenon,
                          caesium, barium, lanthanum,
                          cerium, praseodymium, neodymium,
                          promethium, samarium, europium,
                          gadolinum, terbium, dysprosium,
                          holmium, erbium, thulium,
                          ytterbium, lutetium, halfnium,
                          tantalum, tungsten, rhenium,
                          osmium, iridium, platinum,
                          gold, mercury, thallium, 
                          lead, bismuth, polonium,
                          astatine, radon, francium,
                          radium, actinium, thorium,
                          protactinium, uranium, neptunium, plutonium,
                          americium, curium, berkelium,
                          californium, einsteinium, fermium,
                          mendelevium, nobelium, lawrencium,
                          rutherfordium, dubnium, seaborgium,
                          bohrium, hassium, meitnerium,
                          darmstadtium, roentgenium, copernicium,
                          nihonium, flerovium, moscovium,
                          livermorium, tennessine, oganesson
                          
                          
                          )
    
    return elementsToWrap    



wrappedElements = wrapAllElements()


        
def defineElTypes(wrappedEObjs):
    allElements = range(118)
    
    alkaliMetals = [3, 11, 19, 37, 55, 87]
    alkalineMetals = [4, 12, 20, 38, 56, 88]
    lanthanoids = range(57, 72)
    actinoids = range(89, 104)
    postTmetals = [13, 31, 49, 50, 81, 82, 83, 84, 114]
    metalloids = [5, 14, 32, 33, 51, 52, 85]
    otherNonMetals = [1, 6, 7, 8, 9, 15, 16, 17, 34, 35, 53]
    nobleGases = [2, 10, 18, 36, 54, 86]
    noGroup = [109, 110, 111, 113, 115, 116, 117, 118]
    transitionMetals = []
    
    for E in wrappedEObjs:
        if E.atomicNumber in alkaliMetals:
            E.elType = "Alkali Metals"
        if E.atomicNumber in alkalineMetals:
            E.elType = "Alkaline Earth Metals"
        if E.atomicNumber in lanthanoids:
            E.elType = "Lanthanoids"
        if E.atomicNumber in actinoids:
            E.elType = "Actinoids"
        if E.atomicNumber in postTmetals:
            E.elType = "Post-Transition Metals"
        if E.atomicNumber in metalloids:
            E.elType = "Metalloids"
        if E.atomicNumber in otherNonMetals:
            E.elType = "Other Nonmetals"
        if E.atomicNumber in nobleGases:
            E.elType = "Noble Gases"
        if E.atomicNumber in noGroup:
            E.elType = "unDefined Group"
        if E.elType == "Uh OHHHH":
            E.elType = "Transition Metals"            
          

def elementFormat(wrappedEObjs):
    
    defineElTypes(wrappedEObjs)
    
    for E in wrappedEObjs:
        if E.elType == "Alkali Metals":
            E.bkgColor = "background-color: #02ff1f;" # green
        if E.elType == "Alkaline Earth Metals":
            E.bkgColor = "background-color: #aa0000;" # red
        if E.elType == "Lanthanoids":
            E.bkgColor = "background-color: #ffaa00;" # orange
        if E.elType == "Actinoids":
            E.bkgColor = "background-color: #b64fff;" # puprle
        if E.elType == "Post-Transition Metals":
            E.bkgColor = "background-color: #13e8ff;" # light blue
        if E.elType == "Metalloids":
            E.bkgColor = "background-color: #aa8e1c;" # mustard
        if E.elType == "Other Nonmetals":
            E.bkgColor = "background-color: #df25ff;" # pink
        if E.elType == "Noble Gases":
            E.bkgColor = "background-color: #0000ff;" # dark blue 
        if E.elType == "unDefined Group":
            E.bkgColor = "background-color: #aaaa7f;" # brownish
        if E.elType == "Transition Metals":
            E.bkgColor = "background-color: #aa557f;" # pink brown
            
    for E in wrappedEObjs:
        
        if E.stateOfMatter == "Solid":
            E.textColor = "color: #ffffff;"
        if E.stateOfMatter == "Liquid":
            E.textColor = "color: #c9faff;"
        if E.stateOfMatter == "Gas":
            E.textColor = "color: #ffc3b4;"
        if E.stateOfMatter == "Unknown":
            E.textColor = "color: #596573;"

elementFormat(wrappedElements)



def periodicTableFormat(wrappedEObjs):
    defineElTypes(wrappedEObjs)
    
    #set default values
    for E in wrappedEObjs:
        E.rowPos = 0
        E.colPos = 0
        
        if E.name == "Hydrogen":
            E.rowPos = 1
            E.colPos = 1
    
    
    column1 = [E for E in wrappedEObjs if E.elType == "Alkali Metals"]
    column2 = [E for E in wrappedEObjs if E.elType == "Alkaline Earth Metals"]
    column18 = [E for E in wrappedEObjs if E.elType == "Noble Gases"]
    

    row2 = [E for E in wrappedEObjs if E.atomicNumber in range(5, 10)]
    row3 = [E for E in wrappedEObjs if E.atomicNumber in range(13, 18)]
    row4 = [E for E in wrappedEObjs if E.atomicNumber in range(21, 36)]
    row5 = [E for E in wrappedEObjs if E.atomicNumber in range(39, 54)]
    row6 = [E for E in wrappedEObjs if E.atomicNumber in range(72, 86)]
    row7 = [E for E in wrappedEObjs if E.atomicNumber in range(104, 119)]
    
    lanthRow = [E for E in wrappedEObjs if E.atomicNumber in range(57, 72)]
    actRow = [E for E in wrappedEObjs if E.atomicNumber in range(89, 104)]

    
     
    for n, E in enumerate(column1):
        E.colPos = 1
        E.rowPos = n+2
    
    for n, E in enumerate(column2):
        E.colPos = 2
        E.rowPos = n+2
        
    for n, E in enumerate(column18):
        E.colPos = 18
        E.rowPos = n+1
        
    for n, E in enumerate(row2):
        E.colPos = n+13
        E.rowPos = 2
        
    for n, E in enumerate(row3):
        E.colPos = n+13
        E.rowPos = 3
    
    for n, E in enumerate(row4):
        E.colPos = n+3
        E.rowPos = 4
        
    for n, E in enumerate(row5):
        E.colPos = n+3
        E.rowPos = 5
      
    for n, E in enumerate(row6):
        E.colPos = n+4
        E.rowPos = 6    
        
    for n, E in enumerate(row7):
        E.colPos = n+4
        E.rowPos = 7    
        
    for n, E in enumerate(lanthRow):
        E.colPos = n+4
        E.rowPos = 9  
        
    for n, E in enumerate(actRow):
        E.colPos = n+4
        E.rowPos = 10    
        
        
