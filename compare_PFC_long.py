import numpy
import json
import pylab
import sys
import os

#os.chdir('change_3111')
os.chdir('change_6011')
#os.chdir('/home/giscard/Desktop/ACC/sim_nochange')


bins=[]
width=50.0
num=int(6400./width)
centers=[]

for xin in xrange(num):
    bins.append(xin*width)
bins.append(6400.0)

print bins
for xin in xrange(num):
    centers.append((bins[xin]+bins[xin+1])*0.5)




PFC_diff=[]





for xin in xrange(100):


    fn1='PFC_turn'+str(xin+1)+'-3514-0.gdf'
    PFC_turn=numpy.loadtxt(fn1)[:,1]
    fn2='PFC_push'+str(xin+1)+'-3515-0.gdf'
    PFC_push=numpy.loadtxt(fn2)[:,1]

    

    [y1,edge]=numpy.histogram(PFC_turn,bins)
    [y2,edge]=numpy.histogram(PFC_push,bins)
    y1=y1/400.0/(width/1000.0)
    y2=y2/400.0/(width/1000.0)
    turn_max=numpy.amax(y1)
    push_max=numpy.amax(y2)
    if push_max>turn_max:
        max_v=push_max
    else:
        max_v=turn_max

    yv=(y1-y2)/max_v


    pylab.plot(centers,yv,'-b')



pylab.show() 
    
