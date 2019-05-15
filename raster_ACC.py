import numpy
import json
import pylab
import sys
import os

os.chdir('change_3111')
#os.chdir('change_3011')
#os.chdir('/home/giscard/Desktop/ACC/sim_nochange')
sel=str(1)
fn1='ACC_tp'+sel+'-3518-0.gdf'
PFC_turn_ids=numpy.loadtxt(fn1)[:,0]
PFC_turn_times=numpy.loadtxt(fn1)[:,1]

id_min=int(numpy.amin(PFC_turn_ids))

ids=range(id_min,id_min+40)
print ids

yv=0
for xin in ids:
    index=numpy.where(PFC_turn_ids==xin)[0]
    yp=numpy.ones(len(index))*yv
    #print len(index), len(yp), len(PFC_turn_times[index])
    pylab.scatter(PFC_turn_times[index],yp,s=1,c='r',edgecolors='none')
    yv=yv+1

fn1='ACC_tp_i'+sel+'-3520-0.gdf'
PFC_turn_ids=numpy.loadtxt(fn1)[:,0]
PFC_turn_times=numpy.loadtxt(fn1)[:,1]

id_min=int(numpy.amin(PFC_turn_ids))

ids=range(id_min,id_min+10)
print ids


for xin in ids:
    index=numpy.where(PFC_turn_ids==xin)[0]
    yp=numpy.ones(len(index))*yv
    #print len(index), len(yp), len(PFC_turn_times[index])
    pylab.scatter(PFC_turn_times[index],yp,s=1,c='g',edgecolors='none')
    yv=yv+1

fn1='ACC_pt'+sel+'-3519-0.gdf'
PFC_turn_ids=numpy.loadtxt(fn1)[:,0]
PFC_turn_times=numpy.loadtxt(fn1)[:,1]

id_min=int(numpy.amin(PFC_turn_ids))

ids=range(id_min,id_min+40)
print ids


for xin in ids:
    index=numpy.where(PFC_turn_ids==xin)[0]
    yp=numpy.ones(len(index))*yv
    #print len(index), len(yp), len(PFC_turn_times[index])
    pylab.scatter(PFC_turn_times[index],yp,s=1,c='b',edgecolors='none')
    yv=yv+1
fn1='ACC_pt_i'+sel+'-3521-0.gdf'
PFC_turn_ids=numpy.loadtxt(fn1)[:,0]
PFC_turn_times=numpy.loadtxt(fn1)[:,1]

id_min=int(numpy.amin(PFC_turn_ids))

ids=range(id_min,id_min+10)
print ids


for xin in ids:
    index=numpy.where(PFC_turn_ids==xin)[0]
    yp=numpy.ones(len(index))*yv
    #print len(index), len(yp), len(PFC_turn_times[index])
    pylab.scatter(PFC_turn_times[index],yp,s=1,c='k',edgecolors='none')
    yv=yv+1


fn1='ACC_other'+sel+'-3522-0.gdf'
PFC_turn_ids=numpy.loadtxt(fn1)[:,0]
PFC_turn_times=numpy.loadtxt(fn1)[:,1]

id_min=int(numpy.amin(PFC_turn_ids))

ids=range(id_min,id_min+40)
print ids


for xin in ids:
    index=numpy.where(PFC_turn_ids==xin)[0]
    yp=numpy.ones(len(index))*yv
    #print len(index), len(yp), len(PFC_turn_times[index])
    pylab.scatter(PFC_turn_times[index],yp,s=1,c='m',edgecolors='none')
    yv=yv+1

pylab.xlim([2000,2500])
pylab.ylim([-5,145])
pylab.show()

'''

fn1='PFC_push1-3515-0.gdf'
PFC_push_ids=numpy.loadtxt(fn1)[:,0]
PFC_push_times=numpy.loadtxt(fn1)[:,1]

fn1='PFC_turn_i1-3516-0.gdf'
PFC_turn_i_ids=numpy.loadtxt(fn1)[:,0]
PFC_turn_i_times=numpy.loadtxt(fn1)[:,1]

fn1='PFC_push_i1-3517-0.gdf'
PFC_push_i_ids=numpy.loadtxt(fn1)[:,0]
PFC_push_i_times=numpy.loadtxt(fn1)[:,1]
'''

# end of script




