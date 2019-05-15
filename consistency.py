import numpy
import json
import pylab
import sys
import os

os.chdir('change_6111')
#os.chdir('/home/giscard/Desktop/ACC/sim_nochange')




CI=[]
r1_turn=[]
r2_turn=[]
r3_turn=[]
r4_turn=[]
r1_push=[]
r2_push=[]
r3_push=[]
r4_push=[]




sel_bins1=[2200.0,2400.0]
sel_bins2=[3200.0,3400.0]
sel_bins3=[4200.0,4400.0]
sel_bins4=[5200.0,5400.0]


for xin in xrange(100):



    fn10='motor_turn'+str(xin+1)+'-3523-0.gdf'
    motor_turn=numpy.loadtxt(fn10)[:,1]
    fn11='motor_push'+str(xin+1)+'-3524-0.gdf'
    motor_push=numpy.loadtxt(fn11)[:,1]
    

    [t1,edge]=numpy.histogram(motor_turn,sel_bins1)
    [p1,edge]=numpy.histogram(motor_push,sel_bins1)

    [t2,edge]=numpy.histogram(motor_turn,sel_bins2)
    [p2,edge]=numpy.histogram(motor_push,sel_bins2)

    [t3,edge]=numpy.histogram(motor_turn,sel_bins3)
    [p3,edge]=numpy.histogram(motor_push,sel_bins3)

    [t4,edge]=numpy.histogram(motor_turn,sel_bins4)
    [p4,edge]=numpy.histogram(motor_push,sel_bins4)
  
    r1_turn.append(t1)
    r2_turn.append(t2)
    r3_turn.append(t3)
    r4_turn.append(t4)

    r1_push.append(p1)
    r2_push.append(p2)
    r3_push.append(p3)
    r4_push.append(p4)

      

    
r1_turn=numpy.array(r1_turn)/(0.2*400.0)
r2_turn=numpy.array(r2_turn)/(0.2*400.0)
r3_turn=numpy.array(r3_turn)/(0.2*400.0)
r4_turn=numpy.array(r4_turn)/(0.2*400.0)

r1_push=numpy.array(r1_push)/(0.2*400.0)
r2_push=numpy.array(r2_push)/(0.2*400.0)
r3_push=numpy.array(r3_push)/(0.2*400.0)
r4_push=numpy.array(r4_push)/(0.2*400.0)

pylab.figure(1)
m1=numpy.amax(r1_turn)
m2=numpy.amax(r1_push)

if m1>=m2:
    max_v=m1
else:
    max_v=m2

xv=[0,max_v*1.1]
yv=[0,max_v*1.1]
pylab.plot(xv,yv,'-b')    
pylab.scatter(r1_push,r1_turn,s=50)
pylab.xlabel('push')
pylab.ylabel('turn')
pylab.xlim([0,max_v*1.1])
pylab.ylim([0,max_v*1.1])
pylab.title('first')

pylab.figure(2)
m1=numpy.amax(r2_turn)
m2=numpy.amax(r2_push)

if m1>=m2:
    max_v=m1
else:
    max_v=m2

xv=[0,max_v*1.1]
yv=[0,max_v*1.1]
pylab.plot(xv,yv,'-b')    
pylab.scatter(r2_push,r2_turn,s=50)
pylab.xlabel('push')
pylab.ylabel('turn')
pylab.xlim([0,max_v*1.1])
pylab.ylim([0,max_v*1.1])
pylab.title('second')

pylab.figure(3)
m1=numpy.amax(r3_turn)
m2=numpy.amax(r3_push)

if m1>=m2:
    max_v=m1
else:
    max_v=m2

xv=[0,max_v*1.1]
yv=[0,max_v*1.1]
pylab.plot(xv,yv,'-b')    
pylab.scatter(r3_push,r3_turn,s=50)
pylab.xlabel('push')
pylab.ylabel('turn')
pylab.xlim([0,max_v*1.1])
pylab.ylim([0,max_v*1.1])
pylab.title('third')

pylab.figure(4)
m1=numpy.amax(r4_turn)
m2=numpy.amax(r4_push)

if m1>=m2:
    max_v=m1
else:
    max_v=m2

xv=[0,max_v*1.1]
yv=[0,max_v*1.1]
pylab.plot(xv,yv,'-b')    
pylab.scatter(r4_push,r4_turn,s=50)
pylab.xlabel('push')
pylab.ylabel('turn')
pylab.xlim([0,max_v*1.1])
pylab.ylim([0,max_v*1.1])
pylab.title('fourth')

pylab.show()














