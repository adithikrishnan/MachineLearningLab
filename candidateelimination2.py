# -*- coding: utf-8 -*-
"""CandidateElimination2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fqh7hc1Aeg0VzKrcP0Jrz3ArzVMb7DsK
"""

import csv
with open('/content/findsss.csv') as finds:
  reader = csv.reader(finds)
  data = list(reader)
print(data)
  
h = [0,0,0,0,0,0]
gh=list()
for row in data: # for(row=0;r0w<n;row++)
  if row[-1]=='Yes':
    j=0
    for col in row:
      if col!='Yes':
        #print(col)
        if h[j]!=col and h[j]==0:
          h[j]=col
        elif h[j]!=col and h[j]!=0:
          h[j]='?'
      j=j+1
  elif row[1]!='Yes':
    i=0
    for col in row:
      if col!='No':
        if h[i]!=col and h[i]!='?' and h[i]!=0:
          g=['?','?','?','?','?','?']
          g[i]=h[i]
          gh.append(g)
          i+=1
print(h)
print(gh)

