import numpy
import json
import pylab
import sys
import os

os.chdir('/home/giscard/Desktop/ACC/sim')


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

PFC_turn_s=[]
PFC_push_s=[]
PFC_turn_i_s=[]
PFC_push_i_s=[]

ACC_tp_s=[]
ACC_pt_s=[]
ACC_tp_i_s=[]
ACC_pt_i_s=[]
ACC_other_s=[]

motor_turn_s=[]
motor_push_s=[]
motor_turn_i_s=[]
motor_push_i_s=[]






for xin in xrange(100):
    fn1='PFC_turn'+str(xin+1)+'-3511-0.gdf'
    PFC_turn=numpy.loadtxt(fn1)[:,1]
    fn2='PFC_push'+str(xin+1)+'-3512-0.gdf'
    PFC_push=numpy.loadtxt(fn2)[:,1]
    fn3='PFC_turn_i'+str(xin+1)+'-3513-0.gdf'
    PFC_turn_i=numpy.loadtxt(fn3)[:,1]
    fn4='PFC_push_i'+str(xin+1)+'-3514-0.gdf'
    PFC_push_i=numpy.loadtxt(fn4)[:,1]

    [y1,edge]=numpy.histogram(PFC_turn,bins)
    [y2,edge]=numpy.histogram(PFC_push,bins)
    [y3,edge]=numpy.histogram(PFC_turn_i,bins)
    [y4,edge]=numpy.histogram(PFC_push_i,bins)




    fn5='ACC_tp'+str(xin+1)+'-3515-0.gdf'
    ACC_tp=numpy.loadtxt(fn5)[:,1]
    fn6='ACC_pt'+str(xin+1)+'-3516-0.gdf'
    ACC_pt=numpy.loadtxt(fn6)[:,1]
    fn7='ACC_tp_i'+str(xin+1)+'-3517-0.gdf'
    ACC_tp_i=numpy.loadtxt(fn7)[:,1]
    fn8='ACC_pt_i'+str(xin+1)+'-3518-0.gdf'
    ACC_pt_i=numpy.loadtxt(fn8)[:,1]
    fn9='ACC_other'+str(xin+1)+'-3519-0.gdf'
    ACC_other=numpy.loadtxt(fn9)[:,1]

    [y5,edge]=numpy.histogram(ACC_tp,bins)
    [y6,edge]=numpy.histogram(ACC_pt,bins)
    [y7,edge]=numpy.histogram(ACC_tp_i,bins)
    [y8,edge]=numpy.histogram(ACC_pt_i,bins)
    [y9,edge]=numpy.histogram(ACC_other,bins)



    



    fn10='motor_turn'+str(xin+1)+'-3520-0.gdf'
    motor_turn=numpy.loadtxt(fn10)[:,1]
    fn11='motor_push'+str(xin+1)+'-3521-0.gdf'
    motor_push=numpy.loadtxt(fn11)[:,1]
    fn12='motor_turn_i'+str(xin+1)+'-3522-0.gdf'
    motor_turn_i=numpy.loadtxt(fn12)[:,1]
    fn13='motor_push_i'+str(xin+1)+'-3523-0.gdf'
    motor_push_i=numpy.loadtxt(fn13)[:,1]

    [y10,edge]=numpy.histogram(motor_turn,bins)
    [y11,edge]=numpy.histogram(motor_push,bins)
    [y12,edge]=numpy.histogram(motor_turn_i,bins)
    [y13,edge]=numpy.histogram(motor_push_i,bins)




    y1=y1/400.0/(width/1000.0)
    y2=y2/400.0/(width/1000.0)
    y3=y3/100.0/(width/1000.0)
    y4=y4/100.0/(width/1000.0)

    y5=y5/400.0/(width/1000.0)
    y6=y6/400.0/(width/1000.0)
    y7=y7/100.0/(width/1000.0)
    y8=y8/100.0/(width/1000.0)
    y9=y9/400.0/(width/1000.0)

    y10=y10/400.0/(width/1000.0)
    y11=y11/400.0/(width/1000.0)
    y12=y12/100.0/(width/1000.0)
    y13=y13/100.0/(width/1000.0)

    pylab.figure(1)
    if xin==0:
        pylab.plot(centers,y1,'r',label='PFC_turn')
        pylab.plot(centers,y2,'b',label='PFC_push')
        pylab.plot(centers,y3,'k',label='PFC_turn_i')
        pylab.plot(centers,y4,'g',label='PFC_push_i')
    else:
        pylab.plot(centers,y1,'r')
        pylab.plot(centers,y2,'b')
        pylab.plot(centers,y3,'k')
        pylab.plot(centers,y4,'g')
    pylab.title('PFC')
    pylab.legend()

    pylab.figure(2)
    if xin==0:
        pylab.plot(centers,y5,'r',label='ACC_turn')
        pylab.plot(centers,y6,'b',label='ACC_push')
        pylab.plot(centers,y7,'k',label='ACC_turn_i')
        pylab.plot(centers,y8,'g',label='ACC_push_i')
        pylab.plot(centers,y9,'m',label='ACC_other')
    else:
        pylab.plot(centers,y5,'r')
        pylab.plot(centers,y6,'b')
        pylab.plot(centers,y7,'k')
        pylab.plot(centers,y8,'g')
        pylab.plot(centers,y9,'m')
    pylab.title('ACC')
    pylab.legend()

    pylab.figure(3)
    if xin==0:
        pylab.plot(centers,y10,'r',label='motor_turn')
        pylab.plot(centers,y11,'b',label='motor_push')
        pylab.plot(centers,y12,'k',label='motor_turn_i')
        pylab.plot(centers,y13,'g',label='motor_push_i')
    else:
        pylab.plot(centers,y10,'r')
        pylab.plot(centers,y11,'b')
        pylab.plot(centers,y12,'k')
        pylab.plot(centers,y13,'g')
    pylab.title('motor')
    pylab.legend()

pylab.show()

    
