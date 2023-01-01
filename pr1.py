'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

def astar(start,stop):
  parent={}
  g={}
  parent[start]=start
  g[start]=0
  openset = set(start)
  closedset = set()
  while len(openset)>=0:
    n=None
    for v in openset:
      if n is None or g[v]+h(v)<g[n]+h(n):
        n=v
    if n is stop or graph[n]==None:
      pass
    else:
        for m,weight in getn(n):
          if m not in openset and m not in closedset:
            parent[m]=n
            g[m]=g[n]+weight
            openset.add(m)
          elif g[m]>g[n]+weight:
              g[m]=g[n]+weight
              parent[m]=n
              if m in closedset:
                closedset.remove(m)
                openset.add(m)
    if n==stop:
      path=[]
      while parent[n]!=n:
        path.append(n)
        n=parent[n]
      path.append(start)
      path.reverse()
      print('Path found {}'.format(path))
      
      return path
    openset.remove(n)
    closedset.add(n)
  return None
def getn(n):
  if n in graph:
    return graph[n]
  else:
    return None
def h(v):
  H_dist={'A':11,'B':6,'C':99,'D':1,'E':7,'G':0,}
  return H_dist[v]
graph={
  'A':[('B',2),('E',3)],
 'B':[('C',1),('G',9)],
 'D':[('G',1)],
 'E':[('D',5)],
  
  
}

astar('A','G')
