# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from dataclasses import dataclass

@dataclass

class pElement:
    
    name: str = "Uh OHHHH"
    symbol: str = "Uh OHHHH"
    atomicNumber: int = 1241992
    relAtomicMass: float = 124199.2
    atomicOrbitals: str = "Uh OHHHH"
    stateOfMatter: str = "Uh OHHHH"
    groupNumber: int = 0
    elType: str = "Uh OHHHH" 
    
    # formatting options
    bkgColor: str = "default"
    textColor: str = "default"
    rowPos: int = 0
    colPos: int = 0
    
    endHolder: str = "this is the end"
    
    
hydrogen = pElement( "Hydrogen", # name
                    "H", # symobl
                    1, # atomicNumber
                    1.008, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT ONE}", # atomic orbitals
                    "Gas", #stateOfMatter
                    
                    
                        )

helium = pElement( "Helium", # name
                    "He", # symobl
                    2, # atomicNumber
                    4.00, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Gas", #stateOfMatter
                    
                        )

lithium = pElement( "Lithium", # name
                    "Li", # symobl
                    3, # atomicNumber
                    6.94, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT ONE}",  # atomicOrbitals
                    "Solid", #stateOfMatter
                    
                        )

beryllium = pElement( "Beryllium", # name
                    "Be", # symobl
                    4, # atomicNumber
                    9.0122, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", #stateOfMatter
                    
                        )

boron = pElement( "Boron", # name
                    "B", # symobl
                    5, # atomicNumber
                    10.81, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", #stateOfMatter
                        )

carbon = pElement( "Carbon", # name
                    "C", # symobl
                    6, # atomicNumber
                    12.011, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", #stateOfMatter
                    
                        )

nitrogen = pElement( "Nitrogen", # name
                    "N", # symobl
                    7, # atomicNumber
                    14.007, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT THREE}", # atomicOrbitals
                    "Gas", #stateOfMatter
                        )

oxygen = pElement( "Oxygen", # name
                    "O", # symobl
                    8, # atomicNumber
                    15.999, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT FOUR}", # atomicOrbitals
                    "Gas", #stateOfMatter
                    
                        )

flourine = pElement( "Flourine", # name
                    "F", # symobl
                    9, # atomicNumber
                    18.998, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT FIVE}", # atomicOrbitals
                    "Gas", #stateOfMatter
                    
                        )
 
neon = pElement( "Neon", # name
                    "Ne", # symobl
                    10, # atomicNumber
                    20.180, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}", # atomicOrbitals
                    "Gas", # stateOfMatter
                    
                        )

sodium = pElement( "Sodium", # name
                    "Na", # symobl
                    11, # atomicNumber
                    22.990, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )

magnesium = pElement( "Magnesium", # name
                    "Mg", # symobl
                    12, # atomicNumber
                    24.305, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )

aluminum = pElement( "Aluminum", # name
                    "Al", # symobl
                    13, # atomicNumber
                    26.982, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )

silicon = pElement( "Silicon", # name
                    "Si", # symobl
                    14, # atomicNumber
                    32.06, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    

phosphorus = pElement( "Phorphorus", # name
                    "P", # symobl
                    15, # atomicNumber
                    30.974, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT THREE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
  
sulfur = pElement( "Sulfur", # name
                    "S", # symobl
                    16, # atomicNumber
                    32.06, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT FOUR}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        ) 
chlorine = pElement( "Chlorine", # name
                    "Cl", # symobl
                    17, # atomicNumber
                    35.45, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT FIVE}", # atomicOrbitals
                    "Gas", # stateOfMatter
                    
                        )
    
argon = pElement( "Argon", # name
                    "Ar", # symobl
                    18, # atomicNumber
                    39.948, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}", # atomicOrbitals
                    "Gas", # stateOfMatter
                    
                        ) 

potassium = pElement( "Potassium", # name
                    "K", # symobl
                    19, # atomicNumber
                    39.098, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
calcium = pElement( "Calcium", # name
                    "Ca", # symobl
                    20, # atomicNumber
                    40.078, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
scandium = pElement( "Scandium", # name
                    "Sc", # symobl
                    21, # atomicNumber
                    44.956, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
titanium = pElement( "Titanium", # name
                    "Ti", # symobl
                    22, # atomicNumber
                    47.867, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
vanadium = pElement( "Vanadium", # name
                    "Va", # symobl
                    23, # atomicNumber
                    50.942, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT THREE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
chromium = pElement( "Chromium", # name
                    "Cr", # symobl
                    24, # atomicNumber
                    51.996, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT ONE}"\
                    "3d\N{SUPERSCRIPT FIVE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
maganese = pElement( "Maganese", # name
                    "Mn", # symobl
                    25, # atomicNumber
                    54.938, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT FIVE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
iron = pElement( "Iron", # name
                    "Fe", # symobl
                    26, # atomicNumber
                    55.845, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT SIX}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
cobalt = pElement( "Cobalt", # name
                    "Co", # symobl
                    27, # atomicNumber
                    58.933, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT SEVEN}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
nickel = pElement( "Nickel", # name
                    "Ni", # symobl
                    28, # atomicNumber
                    58.693, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT EIGHT}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
copper = pElement( "Copper", # name
                    "Cu", # symobl
                    29, # atomicNumber
                    63.546, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT ONE}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
zinc = pElement( "Zinc", # name
                    "Zn", # symobl
                    30, # atomicNumber
                    65.38, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
gallium = pElement( "Gallium", # name
                    "Ga", # symobl
                    31, # atomicNumber
                    69.723, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
germanium = pElement( "Germanium", # name
                    "Ge", # symobl
                    32, # atomicNumber
                    78.630, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )

arsenic = pElement( "Arsenic", # name
                    "As", # symobl
                    33, # atomicNumber
                    74.922, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT THREE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
selenium = pElement( "Selenium", # name
                    "Se", # symobl
                    34, # atomicNumber
                    78.971, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT FOUR}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )

bromine = pElement( "Bromine", # name
                    "Br", # symobl
                    35, # atomicNumber
                    79.904, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT FIVe}", # atomicOrbitals
                    "Liquid", # stateOfMatter
                    
                        )
    
krypton = pElement( "Krypton", # name
                    "Kr", # symobl
                    36, # atomicNumber
                    83.798, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}", # atomicOrbitals
                    "Gas", # stateOfMatter
                    
                        )

rubidium = pElement( "Rubidium", # name
                    "Rb", # symobl
                    37, # atomicNumber
                    85.468, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
strontium = pElement( "Strontium", # name
                    "Sr", # symobl
                    38, # atomicNumber
                    87.62, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )

yttrium = pElement( "Yttrium", # name
                    "Y", # symobl
                    39, # atomicNumber
                    88.906, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )

zirconium = pElement( "Zirconium", # name
                    "Zr", # symobl
                    40, # atomicNumber
                    91.224, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )

niobium = pElement( "Niobium", # name
                    "Nb", # symobl
                    41, # atomicNumber
                    92.906, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT ONE}"\
                    "4d\N{SUPERSCRIPT FOUR}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
molybdenum = pElement( "Molybdenum", # name
                    "Mo", # symobl
                    42, # atomicNumber
                    95.95, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT ONE}"\
                    "4d\N{SUPERSCRIPT FIVE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
technetium = pElement( "Technetium", # name
                    "Tc", # symobl
                    43, # atomicNumber
                    98, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT FIVE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
ruthenium = pElement( "Ruthenium", # name
                    "Ru", # symobl
                    44, # atomicNumber
                    101.07, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT ONE}"\
                    "4d\N{SUPERSCRIPT SEVEN}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
rhodium = pElement( "Rhodium", # name
                    "Rh", # symobl
                    45, # atomicNumber
                    102.91, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT ONE}"\
                    "4d\N{SUPERSCRIPT EIGHT}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )

palladium = pElement( "Palladium", # name
                    "Pd", # symobl
                    46, # atomicNumber
                    106.42, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
silver = pElement( "Silver", # name
                    "Ag", # symobl
                    47, # atomicNumber
                    107.87, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT ONE}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
cadmium = pElement( "Cadmium", # name
                    "Cd", # symobl
                    48, # atomicNumber
                    112.41, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
indium = pElement( "Indium", # name
                    "In", # symobl
                    49, # atomicNumber
                    114.82, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
tin = pElement( "Tin", # name
                    "Sn", # symobl
                    50, # atomicNumber
                    118.71, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
antimony = pElement( "Antimony", # name
                    "Sb", # symobl
                    51, # atomicNumber
                    121.76, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT THREE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
tellurium = pElement( "Tellurium", # name
                    "Te", # symobl
                    52, # atomicNumber
                    127.60, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT FOUR}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
iodine = pElement( "Iodine", # name
                    "I", # symobl
                    53, # atomicNumber
                    126.90, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT FIVE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
xenon = pElement( "Xenon", # name
                    "Xe", # symobl
                    54, # atomicNumber
                    131.29, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}", # atomicOrbitals
                    "Gas", # stateOfMatter
                    
                        )
    
caesium = pElement( "Caesium", # name
                    "Cs", # symobl
                    55, # atomicNumber
                    132.91, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
barium = pElement( "Barium", # name
                    "Ba", # symobl
                    56, # atomicNumber
                    137.33, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
lanthanum = pElement( "lanthanum", # name
                    "La", # symobl
                    57, # atomicNumber
                    138.91, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "5d\N{SUPERSCRIPT ONE}",# atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
cerium = pElement( "Cerium", # name
                    "Ce", # symobl
                    58, # atomicNumber
                    140.12, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}"\
                    "5d\N{SUPERSCRIPT ONE}",# atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )

praseodymium = pElement( "Praseodymium", # name
                    "Pr", # symobl
                    59, # atomicNumber
                    140.12, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT THREE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
neodymium = pElement( "Neodymium", # name
                    "Nd", # symobl
                    60, # atomicNumber
                    144.24, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT FOUR}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
promethium = pElement( "Promethium", # name
                    "Pm", # symobl
                    61, # atomicNumber
                    145, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT FIVE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
samarium = pElement( "Samarium", # name
                    "Sm", # symobl
                    62, # atomicNumber
                    150.36, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT SIX}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
europium = pElement( "Europium", # name
                    "Eu", # symobl
                    63, # atomicNumber
                    151.96, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT SEVEN}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
gadolinum = pElement( "Gadolinium", # name
                    "Gd", # symobl
                    64, # atomicNumber
                    157.25, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT SEVEN}"\
                    "5d\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
terbium = pElement( "Terbium", # name
                    "Tb", # symobl
                    65, # atomicNumber
                    158.93, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT NINE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
dysprosium = pElement( "Dysprosium", # name
                    "Dy", # symobl
                    66, # atomicNumber
                    162.50, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
holmium = pElement( "Holmium", # name
                    "Dy", # symobl
                    67, # atomicNumber
                    164.93, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
erbium = pElement( "Erbium", # name
                    "Dr", # symobl
                    68, # atomicNumber
                    167.26, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
thulium = pElement( "Thulium", # name
                    "Tm", # symobl
                    69, # atomicNumber
                    168.93, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT THREE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
ytterbium = pElement( "Ytterbium", # name
                    "Yb", # symobl
                    70, # atomicNumber
                    173.05, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
lutetium = pElement( "Lutetium", # name
                    "Lu", # symobl
                    71, # atomicNumber
                    174.97, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
halfnium = pElement( "Halfnium", # name
                    "Hf", # symobl
                    72, # atomicNumber
                    178.49, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
tantalum = pElement( "Tantalum", # name
                    "Hf", # symobl
                    73, # atomicNumber
                    180.95, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT THREE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
tungsten = pElement( "Tungsten", # name
                    "W", # symobl
                    74, # atomicNumber
                    183.84, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT FOUR}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
rhenium = pElement( "Rhenium", # name
                    "Re", # symobl
                    75, # atomicNumber
                    186.21, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT FIVE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
osmium = pElement( "Osmium", # name
                    "Os", # symobl
                    76, # atomicNumber
                    190.23, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT SIX}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
iridium = pElement( "Iridium", # name
                    "Ir", # symobl
                    77, # atomicNumber
                    190.23, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT SEVEN}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
platinum = pElement( "Platinum", # name
                    "Pt", # symobl
                    78, # atomicNumber
                    195.08, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT ONE}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT NINE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )

gold = pElement( "Gold", # name
                    "Au", # symobl
                    79, # atomicNumber
                    196.97, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT ONE}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
mercury = pElement( "Mercury", # name
                    "Hg", # symobl
                    80, # atomicNumber
                    200.59, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
thallium = pElement( "Thallium", # name
                    "Tl", # symobl
                    81, # atomicNumber
                    204.38, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
lead = pElement( "Lead", # name
                    "Pb", # symobl
                    82, # atomicNumber
                    207.2, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
bismuth = pElement( "Bismuth", # name
                    "Bi", # symobl
                    83, # atomicNumber
                    208.98, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT THREE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
polonium = pElement( "Polonium", # name
                    "Po", # symobl
                    84, # atomicNumber
                    209, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT FOUR}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )

astatine = pElement( "Astatine", # name
                    "At", # symobl
                    85, # atomicNumber
                    210, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT FIVE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
radon = pElement( "Radon", # name
                    "Rn", # symobl
                    86, # atomicNumber
                    222, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
francium = pElement( "Francium", # name
                    "Fr", # symobl
                    87, # atomicNumber
                    223, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
radium = pElement( "Radium", # name
                    "Ra", # symobl
                    88, # atomicNumber
                    226, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
actinium = pElement( "Actinium", # name
                    "Ac", # symobl
                    89, # atomicNumber
                    227, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "6d\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
thorium = pElement( "Thorium", # name
                    "Th", # symobl
                    90, # atomicNumber
                    232.04, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "6d\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
protactinium = pElement( "Protactinium", # name
                    "Pa", # symobl
                    91, # atomicNumber
                    231.04, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT TWO}"\
                    "6d\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
uranium = pElement( "Uranium", # name
                    "U", # symobl
                    92, # atomicNumber
                    238.03, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT THREE}"\
                    "6d\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
neptunium = pElement( "Neptunium", # name
                    "Np", # symobl
                    93, # atomicNumber
                    237, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
plutonium = pElement( "Plutonium", # name
                    "Pu", # symobl
                    94, # atomicNumber
                    244, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT SIX}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
americium = pElement( "Americium", # name
                    "Am", # symobl
                    95, # atomicNumber
                    243, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT SEVEN}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
curium = pElement( "Curium", # name
                    "Cm", # symobl
                    96, # atomicNumber
                    247, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT SEVEN}"\
                    "6d\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
berkelium = pElement( "Berkelium", # name
                    "Bk", # symobl
                    97, # atomicNumber
                    247, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT NINE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
californium = pElement( "Californium", # name
                    "Cf", # symobl
                    98, # atomicNumber
                    251, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
einsteinium = pElement( "Einsteinium", # name
                    "Es", # symobl
                    99, # atomicNumber
                    252, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
fermium = pElement( "Fermium", # name
                    "Fm", # symobl
                    100, # atomicNumber
                    257, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
mendelevium = pElement( "Mendelevium", # name
                    "Md", # symobl
                    101, # atomicNumber
                    258, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT THREE}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
nobelium = pElement( "Nobelium", # name
                    "No", # symobl
                    102, # atomicNumber
                    259, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}", # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
lawrencium = pElement( "Lawrencium", # name
                    "Lr", # symobl
                    103, # atomicNumber
                    266, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "7p\N{SUPERSCRIPT ONE}" , # atomicOrbitals
                    "Solid", # stateOfMatter
                    
                        )
    
rutherfordium = pElement( "Rutherfordium", # name
                    "Rf", # symobl
                    104, # atomicNumber
                    267, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT TWO}" , # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
dubnium = pElement( "Dubnium", # name
                    "Db", # symobl
                    105, # atomicNumber
                    268, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT THREE}" , # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
seaborgium = pElement( "Seaborgium", # name
                    "Sg", # symobl
                    106, # atomicNumber
                    269, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT FOUR}" , # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
bohrium = pElement( "Bohrium", # name
                    "Bh", # symobl
                    107, # atomicNumber
                    270, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT FIVE}" , # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
hassium = pElement( "Hassium", # name
                    "Hs", # symobl
                    108, # atomicNumber
                    270, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT SIX}" , # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
meitnerium = pElement( "Meitnerium", # name
                    "Mt", # symobl
                    109, # atomicNumber
                    278, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT SEVEN}" , # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
darmstadtium = pElement( "Darmstadtium", # name
                    "Ds", # symobl
                    110, # atomicNumber
                    281, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT ONE}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT NINE}" , # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
roentgenium = pElement( "Roentgenium", # name
                    "Rg", # symobl
                    111, # atomicNumber
                    282, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT NINE}" , # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
copernicium = pElement( "Copernicium", # name
                    "Cn", # symobl
                    112, # atomicNumber
                    285, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}" , # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
nihonium = pElement( "Nihonium", # name
                    "Nh", # symobl
                    113, # atomicNumber
                    286, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "7p\N{SUPERSCRIPT ONE}", # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
flerovium = pElement( "Flerovium", # name
                    "Fl", # symobl
                    114, # atomicNumber
                    289, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "7p\N{SUPERSCRIPT TWO}", # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
moscovium = pElement( "Moscovium", # name
                    "Mc", # symobl
                    115, # atomicNumber
                    290, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "7p\N{SUPERSCRIPT THREE}", # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
livermorium = pElement( "Livermorium", # name
                    "Lv", # symobl
                    116, # atomicNumber
                    293, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "7p\N{SUPERSCRIPT FOUR}", # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
tennessine = pElement( "Tennessine", # name
                    "Ts", # symobl
                    117, # atomicNumber
                    294, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "7p\N{SUPERSCRIPT FIVE}", # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
    
oganesson = pElement( "Oganesson", # name
                    "Og", # symobl
                    118, # atomicNumber
                    294, # relAtomicMass units: g/mol
                    "1s\N{SUPERSCRIPT TWO}"\
                    "2s\N{SUPERSCRIPT TWO}"\
                    "2p\N{SUPERSCRIPT SIX}"\
                    "3s\N{SUPERSCRIPT TWO}"\
                    "3p\N{SUPERSCRIPT SIX}"\
                    "4s\N{SUPERSCRIPT TWO}"\
                    "3d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "4p\N{SUPERSCRIPT SIX}"\
                    "5s\N{SUPERSCRIPT TWO}"\
                    "4d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "5p\N{SUPERSCRIPT SIX}"\
                    "6s\N{SUPERSCRIPT TWO}"\
                    "4f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "5d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "6p\N{SUPERSCRIPT SIX}"\
                    "7s\N{SUPERSCRIPT TWO}"\
                    "5f\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT FOUR}"\
                    "6d\N{SUPERSCRIPT ONE}""\N{SUPERSCRIPT ZERO}"\
                    "7p\N{SUPERSCRIPT SIX}", # atomicOrbitals
                    "Unknown", # stateOfMatter
                    
                        )
