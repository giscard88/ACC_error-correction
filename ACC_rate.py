import numpy
import json
import pylab
import sys
import os

#os.chdir('change_3111')
#os.chdir('nochange_3111')
#os.chdir('/home/giscard/Desktop/ACC/sim_nochange')
os.chdir('change_push_3111')

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


ACC_tp_s=[]
ACC_pt_s=[]
ACC_tp_i_s=[]
ACC_pt_i_s=[]
ACC_other_s=[]

for xin in xrange(100):

    fn5='ACC_tp'+str(xin+1)+'-3518-0.gdf'
    fn6='ACC_pt'+str(xin+1)+'-3519-0.gdf'
    fn7='ACC_tp_i'+str(xin+1)+'-3520-0.gdf'
    fn8='ACC_pt_i'+str(xin+1)+'-3521-0.gdf'
    fn9='ACC_other'+str(xin+1)+'-3522-0.gdf'
    try:
        ACC_tp=numpy.loadtxt(fn5)[:,1]
        ACC_tp_s.append(len(ACC_tp))
    except:
        ACC_tp_s.append(0.)
    try:
        ACC_pt=numpy.loadtxt(fn6)[:,1]
        ACC_pt_s.append(len(ACC_pt))
    except:
        ACC_pt_s.append(0.)
    try:
        ACC_tp_i=numpy.loadtxt(fn7)[:,1]
        ACC_tp_i_s.append(len(ACC_tp_i))
    except:
        ACC_tp_i_s.append(0.)
    try:
        ACC_pt_i=numpy.loadtxt(fn8)[:,1]
        ACC_pt_i_s.append(len(ACC_pt_i))
    except:
        ACC_pt_i_s.append(0.0)
    try:
        ACC_other=numpy.loadtxt(fn9)[:,1]
        ACC_other_s.append(len(ACC_other))
    except:
        ACC_other_s.append(0.0)

ACC_tp_s=numpy.array(ACC_tp_s)/(400.0*3.2)
ACC_pt_s=numpy.array(ACC_pt_s)/(400.0*3.2)
ACC_tp_i_s=numpy.array(ACC_tp_i_s)/(100.0*3.2)
ACC_pt_i_s=numpy.array(ACC_pt_i_s)/(100.0*3.2)
ACC_other_s=numpy.array(ACC_other_s)/(400.0*3.2)

TP_m=numpy.mean(ACC_tp_s)
TP_err=numpy.std(ACC_tp_s)/10.0
PT_m=numpy.mean(ACC_pt_s)
PT_err=numpy.std(ACC_pt_s)/10.0

TP_i_m=numpy.mean(ACC_tp_i_s)
TP_i_err=numpy.std(ACC_tp_i_s)/10.0
PT_i_m=numpy.mean(ACC_pt_i_s)
PT_i_err=numpy.std(ACC_pt_i_s)/10.0

Other_m=numpy.mean(ACC_other_s)
Other_err=numpy.std(ACC_other_s)/10.0

#mean_values=[TP_m, PT_m, TP_i_m, PT_i_m,Other_m]
#err_values=[TP_err, PT_err, TP_i_err, PT_i_err,Other_err]

mean_values=[TP_m, PT_m,Other_m]
err_values=[TP_err, PT_err,Other_err]

xvalue=[1,2,3]
xvalue=numpy.array(xvalue)
xv1=xvalue+0.4
pylab.bar(xvalue,mean_values,width=0.8)
pylab.errorbar(xv1,mean_values,yerr=err_values,fmt='o')
pylab.xticks(xv1,['TP','PT','other'])
pylab.xlim([0.8,4.0])





pylab.show() 
    
