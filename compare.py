import numpy
import json
import pylab
import sys
import os

os.chdir('/home/giscard/Desktop/ACC/sim')
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


motor_turn_s=[]
motor_push_s=[]
motor_turn_i_s=[]
motor_push_i_s=[]



sel_bins=[2200.0,2400.0]


for xin in xrange(100):



    fn10='motor_turn'+str(xin+1)+'-3520-0.gdf'
    motor_turn=numpy.loadtxt(fn10)[:,1]
    fn11='motor_push'+str(xin+1)+'-3521-0.gdf'
    motor_push=numpy.loadtxt(fn11)[:,1]
    

    [y10,edge]=numpy.histogram(motor_turn,sel_bins)
    [y11,edge]=numpy.histogram(motor_push,sel_bins)
    
    motor_turn_s.append(y10)
    motor_push_s.append(y11)

motor_turn_s=numpy.array(motor_turn_s)
motor_push_s=numpy.array(motor_push_s)

motor_turn_s=motor_turn_s/(0.2*400.0)
motor_push_s=motor_push_s/(0.2*400.0)

m1=numpy.amax(motor_turn_s)
m2=numpy.amax(motor_push_s)

if m1>=m2:
    max_v=m1
else:
    max_v=m2

xv=[0,max_v*1.1]
yv=[0,max_v*1.1]
pylab.plot(xv,yv,'-b')    
pylab.scatter(motor_push_s,motor_turn_s,s=50)
pylab.xlabel('push')
pylab.ylabel('turn')
pylab.xlim([0,max_v*1.1])
pylab.ylim([0,max_v*1.1])




pylab.show() 
    
