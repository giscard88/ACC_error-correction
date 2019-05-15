import numpy
import json
import pylab
import sys
import os

os.chdir('change_3111')
#os.chdir('/home/giscard/Desktop/ACC/sim_nochange')


bins=[]
width=50.0
num=int(3200./width)
centers=[]

for xin in xrange(num):
    bins.append(xin*width)
bins.append(3200.0)

print bins
for xin in xrange(num):
    centers.append((bins[xin]+bins[xin+1])*0.5)




PFC_diff=[]



pylab.figure(1)

for xin in xrange(100):


    fn1='ACC_other'+str(xin+1)+'-3522-0.gdf'
    NS=numpy.loadtxt(fn1)[:,1]
    



    
    

    [y1,edge]=numpy.histogram(NS,bins)
    y1=y1/400.0/(width/1000.0)
    max_v=numpy.amax(y1)
    y1=y1/max_v
    


    pylab.plot(centers,y1,'-b')
pylab.xlim([2000,2300])


pylab.figure(2)
for xin in xrange(100):


    fn1='ACC_tp'+str(xin+1)+'-3518-0.gdf'
    NS=numpy.loadtxt(fn1)[:,1]
    
    
    

    [y1,edge]=numpy.histogram(NS,bins)
    y1=y1/400.0/(width/1000.0)
    max_v=numpy.amax(y1)
    y1=y1/max_v
    


    pylab.plot(centers,y1,'-b')
pylab.xlim([2000,2300])


pylab.show() 
    
