# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['HDRandom']

# %% ../nbs/00_core.ipynb 3
from math import fmod

# %% ../nbs/00_core.ipynb 5
class HDRandom:
    """
    HDR Random Number Generator, based on https://www.probabilitymanagement.org/hdr
    """
    def __init__(self, 
                 entity: int, # entity integer seed (assigned or should be 0) 
                 varId: int,  # varId integer seed
                 seed3: int,  # seed3 integer seed
                 seed4: int): # seed4 integer seed
        self.entity = entity
        self.varId =  varId
        self.seed3 =  seed3
        self.seed4 =  seed4
        
    def generate(self, 
                 counter: int # a counter value 
                )-> float:
        """
        Generates a random number for this counter value
        """
        return (fmod((fmod(fmod(999999999999989,fmod(counter*2499997 + (self.varId)*1800451 + (self.entity)*2000371 + (self.seed3)*1796777 + (self.seed4)*2299603, 7450589 ) * 4658 + 7450581 ) * 383, 99991 ) * 7440893 + fmod( fmod( 999999999999989, fmod( counter*2246527 + (self.varId)*2399993 + (self.entity)*2100869 + (self.seed3)*1918303 + (self.seed4)*1624729, 7450987 ) * 7580 + 7560584 ) * 17669, 7440893 )) * 1343, 4294967296 ) + 0.5 ) / 4294967296
    
    def __str__(self):
        return f"Random Number Generator entity={self.entity} varId={self.varId} seed3={self.seed3} seed4{self.seed4}"
    
    __repr__ = __str__
