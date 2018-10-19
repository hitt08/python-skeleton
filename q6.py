# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question06(numServers, targetServer, times):
  # modify and then return the variable below
  if(targetServer==0):
      answer=0
  else :
      neighbours=[n for n in range(1,numServers)]
      neighbours.remove(targetServer)
      dist=times[0,targetServer]
      for i in neighbours:
          c=times[0,i]
          if(c<dist):
              c_neighbours=list(neighbours)
              c_neighbours.remove(i)
              c=min_dist(c_neighbours,targetServer,i,times,c)
          dist=c if(c<dist) else dist
      answer = dist
  return answer

def min_dist(neighbours,targetServer,srcServer,times,dist):
    c=dist+times[srcServer,targetServer]
    if(len(neighbours)==0):
        min=c
    else :
        min=c
        for n in neighbours:
            new_neighbours=list(neighbours)
            new_neighbours.remove(n)
            new_dist=min_dist(new_neighbours,targetServer,n,times,dist+times[srcServer,n])
            if(new_dist<min):
                min=new_dist
    return(min)
