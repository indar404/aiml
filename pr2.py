'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class graph:
  
  def __init__(self,start,heur,graph):
    self.start=start
    self.h=heur
    self.graph =graph
    self.parent={}
    self.sg={}
    self.status={}
  
  def applyaostar(self,start):
    self.aostar(self.start,False)
  
  def getn(self,v):
    return self.graph.get(v,'')
    
  def gs(self,v):
    return self.status.get(v,0)
  
  def ss(self,v,val):
     self.status[v]=val
  
  def gh(self,v):
    return self.h.get(v,0)
  
  def sh(self,v,val):
    self.h[v]=val
    
  def printsol(self):
    print("For graph solution, traverse the graph from start value:",self.start)
    print("---------------------------------------")
    print(self.sg)
    print("---------------------------------------")
  def mincost(self,v):
    minimumcost=0
    costnode={}
    costnode[minimumcost]=[]
    flag=False
    for nodeinfotuple in self.getn(v):
      cost=0
      node=[]
      for n,weight in nodeinfotuple:
        cost+=weight+self.gh(n)
        node.append(n)
        
      if flag==False:
        minimumcost=cost
        costnode[minimumcost]=node
        flag=True
      elif minimumcost>cost:
        minimumcost=cost
        costnode[minimumcost]=node
    return minimumcost,costnode[minimumcost]
  def aostar(self,v,backtracking):
    print("Hueristic ",self.h)
    print("Solition graph",self.sg)
    print("Processing graph",v)
    if self.gs(v)>=0:
      minimumcost,costnode = self.mincost(v)
      print(minimumcost,costnode)
      self.sh(v,minimumcost)
      self.ss(v,len(costnode))
      solved=True
      for child in costnode:
        self.parent[child]=v
        if self.gs(child)!=-1:
          solved=False
      if solved == True:
        self.ss(v,-1)
        self.sg[v]=costnode
        
      if v!=self.start:
        self.aostar(self.parent[v],True)
      if backtracking ==False:
        for child in costnode:
          self.ss(child,0)
          self.aostar(child,False)
h1={'A':1,'B':6,'C':2,'D':12,'E':2,'F':1,'G':5,'H':7,'I':7,'J':1}
graph1={
 'A':[[('B',1),('C',1)],[('D',1)]],
 'B':[[('G',1)],[('H',1)]],
 'C':[[('J',1)]],
 'D':[[('E',1),('F',1)]],
 'G':[[('I',1)]]
 }
G1 = graph('A',h1,graph1)
G1.applyaostar('A')
G1.printsol()

      
