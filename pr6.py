import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")
pe = len(data.loc[data[data.columns[-1]]=='Yes'])
te = len(data)
ne = te-pe
training = data.sample(frac=0.74,replace=False)
test = pd.concat([data,training]).drop_duplicates(keep=False)

prob={}

for col in training.columns[:-1]:
  prob[col]={}
  values = set(data[col])
  for value in values:
    temp =   training.loc[training[col]==value]
    tp = len(temp.loc[temp[temp.columns[-1]]=='Yes'])
    tt = len(temp)
    tn = tt-tp
    prob[col][value]= [tp/tt,tn/tt]
pred=[]
prediction=0

for i in range(len(test)):
  row = test.iloc[i,:]
  fpp  = pe/te
  fpn = ne/te
  for col in test.columns[:-1]:
    fpp*=prob[col][row[col]][0]
    fpn*=prob[col][row[col]][1]
  if fpp>fpn:
    pred.append('Yes')
  else:
    pred.append('No')
  if pred[-1]==row[-1]:
    prediction+=1

print('\nActual Values : ',list(test[test.columns[-1]]))
print('Predicted : ',pred)
print('Accuracy : ',prediction/len(test))
    
  
