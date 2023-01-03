'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

import pandas as pd
import numpy as np

data = pd.read_csv("Training_examples.csv")
concepts = np.array(data.iloc[:,0:-1])
print(concepts)
target = np.array(data.iloc[:,-1])
print(target)

def learn(concepts,target):
  specific_h = concepts[0].copy()
  general_h = [['?' for i in range(len(specific_h))] for i in range(len(specific_h))]
  
  for i,h in enumerate(concepts):
    if target[i]=='Yes':
      for x in range(len(specific_h)):
        if specific_h[x]!=h[x]:
          specific_h[x]='?'
          general_h[x][x]='?'
    if target[i]=='No':
      for x in range(len(specific_h)):
        for x in range(len(specific_h)):
          if specific_h[x]!=h[x]:
            general_h[x][x]=specific_h[x]
          else:
            general_h[x][x]='?'
  indices = [i for i,h in enumerate(general_h) if h == ['?','?','?','?','?','?']]
  for i in indices:
    general_h.remove(['?','?','?','?','?','?'])
  return specific_h,general_h
s_h,g_h = learn(concepts,target)
print(s_h)
print('\n')
print(g_h)
          
