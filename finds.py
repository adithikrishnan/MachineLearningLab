# -*- coding: utf-8 -*-
"""FindS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GzD52nL8RAoGf77_wypF_P52AqKeE3dN

FINDS ALGORITHM
"""

import csv
with open("/content/data.csv") as f:
  reader = csv.reader(f)
  data = list(reader)

data

h=['0','0','0','0','0','0']

for row in data:
  if row[-1] == 'Y':
    j=0
    for col in row:
      if col != 'Y':
        if col != h[j] and h[j] == '0':
          h[j] = col
        elif col != h[j] and h[j] != '0':
          h[j] = '?'
      j += 1

h