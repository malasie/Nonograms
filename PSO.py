# Metoda BPSO

import pyswarms as ps
import numpy as np
import Nonogramy
import matplotlib.pyplot as plt

l_kolumn,l_wierszy=Nonogramy.Panda.wielkosc()
kratki_kol, kratki_wier, bloki_kol, bloki_wier=Nonogramy.Panda.nonogram()



def f(lista):
    l=np.copy(lista)
    M = []
    while l.size > 0:
      M.append(l[:(l_kolumn)])
      l = l[(l_kolumn):]
    M=np.array(M)
    
    zamblK=[]
    zamblW=[]
    zamKrK=[]
    zamKrW=[]

    for i in range(l_kolumn):
        zam=False
        bl=0
        kr=0
        for j in range(l_wierszy):
            if M[i,j]==1:
                kr=kr+1
                zam=True
                if j==l_wierszy-1:
                    bl=bl+1
            elif zam==True:
                bl=bl+1
                zam=False
        zamblW.append(bl)
        zamKrW.append(kr)       
    for i in range(l_wierszy):
        zam=False
        bl=0
        kr=0
        for j in range(l_kolumn):
            if M[j,i]==1:
                kr=kr+1 
                zam=True
                if j==l_kolumn-1:
                    bl=bl+1
            elif zam==True:
                bl=bl+1
                zam=False
        zamblK.append(bl)
        zamKrK.append(kr)
    suma=0
    for a in range(l_kolumn):
        suma=suma+np.abs(zamblK[a]-bloki_kol[a])+np.abs(zamKrK[a]-kratki_kol[a])
    
    for b in range(l_wierszy):
        suma=suma+np.abs(zamblW[b]-bloki_wier[b])+np.abs(zamKrW[b]-kratki_wier[b])

    return suma

def g(x): 
    n_particles = x.shape[0]
    j = [f(x[i]) for i in range(n_particles)]
    
    return np.array(j)



options = {'c1': 1, 'c2': 1, 'w':0.95, 'k':20, 'p':1}
optimizer = ps.discrete.binary.BinaryPSO(n_particles=70, dimensions=l_kolumn*l_wierszy,
options=options)


cos, pos=optimizer.optimize(g, iters=8000)



l=np.copy(pos)
l=np.array(l)
M = []
while l.size > 0:
    M.append(l[:(l_kolumn)])
    l = l[(l_kolumn):]
M=np.array(M)


roz=''
for i in range(l_wierszy):
    w='|'
    for j in M[i]:
        if j==0:
            w=w+'  '
        else: w=w+'##'
    roz=roz+w+"|\n"
print(roz)
            

plt.plot(optimizer.cost_history)