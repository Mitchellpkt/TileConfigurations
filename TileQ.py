# Looking *'s shading question
# See "readme"

# Global prelims
import itertools
import operator
from itertools import chain, repeat, islice
import numpy as np
    
def pad_infinite(iterable, padding=None):
   return chain(iterable, repeat(padding))

def pad(iterable, size, padding=None):
   return islice(pad_infinite(iterable, padding), size)
   
def hasha(layout, vN):
    flatboard = range(1,vN**2+1)
    squareboard = np.reshape(flatboard, (vN,vN)).tolist()
    return sum(p*q for p,q in zip(layout, flatboard))
   
print('LFC')

# vN gives dimension of the board (i.e. vN=4 ==> 4x4 board)
# In loop style right now. To work with 1 n, set range(n,n+1) for the loop
for vN in range(1,8):
    
    #next 5 lines my clunky way to generate all possible combos
    [apaddedseed,aalllayouts] = [[],[]];
    for ci in range(0,vN**2+1):
        apaddedseed.append(list(pad(np.ones(ci, dtype=np.int), vN**2, 0)))   
    for seed in apaddedseed:
        aalllayouts.extend(np.unique([x for x in itertools.permutations(seed,len(seed))]).tolist())
    aac = [y for y in [x for x in aalllayouts]]
    aacs = [np.reshape(x, (vN,vN)).tolist() for x in aac]
    
    #Set troubleshoot to 1 for more verbose
    troubleshoot = 0
    if troubleshoot == 1:
        hashes = [];
        for ci in aac:
            hashes.append(hasha(ci,vN))
            print('----\nBoard index ' + str(aac.index(ci)) + '\n' +str(np.array(aacs[aac.index(ci)]))+'\n Hash = ' + str(hasha(ci,vN)))
        print('\n\n Note: ' + str(len(hashes)) + ' hashes, and ' + str(len(np.unique(hashes).tolist())) + ' unique hashes')
    
    #Eliminate duplicates
    [victors, victorsflat] = [[],[]]
    for l in aacs:
        lf = str(np.reshape(l,(1,vN**2))[0].tolist())
        bad = 0
        for tf in range(4):
            if victorsflat.count(lf) > 0:
                bad = 1
            else:
                l = np.rot90(l)
                lf = str(np.reshape(l,(1,vN**2))[0].tolist())
        if bad == 0: 
            victors.append(l.tolist())
            victorsflat.append(lf)
    
    #set showvictors = 1 to see the unique matrices        
    showvictors = 1
    if showvictors == 0:
        for ci in victors:
            print('\n')
            print(np.array(ci))
            pass
            
    print('There were ' + str(len(victors)) + ' for n = ' + str(vN))
