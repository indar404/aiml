import csv
import random
import math
import operator

def load(filename,split,tn,ts):
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        data = list(lines)
        for x in range(len(data)-1):
            for y in range(4):
                data[x][y]=float(data[x][y])
            if random.random()<split:
                tn.append(data[x])
            else:
                ts.append(data[x])
                
def eucl(ins1,ins2,length):
    distance=0
    for x in range(length):
        distance += pow((ins1[x]-ins2[x]),2)
    return math.sqrt(distance)

def getneighbor(tn,tsi,k):
    length = len(tn)
    distance=[]
    dist=0
    for x in range(length):
        dist = eucl(tsi,tn[x],len(tsi)-1)
        distance.append((tn[x],dist))
    distance.sort(key=operator.itemgetter(1))
    neighbor=[]
    for x in range(k):
        neighbor.append(distance[x][0])
    return neighbor

def response(neighbor):
    classvotes={}
    for x in range(len(neighbor)):
        response = neighbor[x][-1]
        if response in classvotes:
            classvotes[response]+=1
        else:
            classvotes[response]=1
    sortedvotes = sorted(classvotes.items(),key=operator.itemgetter(1),reverse=True)
    return sortedvotes[0][0]
def accuracay(ts,prediction):
  correct=0
  for x in range(len(ts)):
    if prediction[x]==ts[x][-1]:
      correct+=1
  return (correct/float(len(ts))) *100
    
tn=[]
ts=[]
split=0.67
k=3
load('KNN-input.csv',split,tn,ts)
length = len(ts)
predictions=[]


print('\n The predictions are:')
for x in range(length):
    
    neighbor = getneighbor(tn,ts[x],k)
   
    result = response(neighbor)
    predictions.append(result)
    print(' predicted=' + repr(result) + ', actual=' + repr(ts[x][-1]))
print(accuracay(ts,predictions))
