import numpy
import json
import pylab
import sys
import os

#os.chdir('change_3111')
#os.chdir('nochange_3111')
os.chdir('change_6110')
#os.chdir('/home/giscard/Desktop/ACC/sim_nochange')

fn1='motor_turn1-3523-0.gdf'
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
    pylab.scatter(PFC_turn_times[index],yp,s=5,c='r',edgecolors='none')
    yv=yv+1

fn1='motor_turn_i1-3525-0.gdf'
PFC_turn_ids=numpy.loadtxt(fn1)[:,0]
PFC_turn_times=numpy.loadtxt(fn1)[:,1]

id_min=int(numpy.amin(PFC_turn_ids))

ids=range(id_min,id_min+10)
print ids


for xin in ids:
    index=numpy.where(PFC_turn_ids==xin)[0]
    yp=numpy.ones(len(index))*yv
    #print len(index), len(yp), len(PFC_turn_times[index])
    pylab.scatter(PFC_turn_times[index],yp,s=5,c='b',edgecolors='none')
    yv=yv+1

fn1='motor_push1-3524-0.gdf'
PFC_turn_ids=numpy.loadtxt(fn1)[:,0]
PFC_turn_times=numpy.loadtxt(fn1)[:,1]

id_min=int(numpy.amin(PFC_turn_ids))

ids=range(id_min,id_min+40)
print ids


for xin in ids:
    index=numpy.where(PFC_turn_ids==xin)[0]
    yp=numpy.ones(len(index))*yv
    #print len(index), len(yp), len(PFC_turn_times[index])
    pylab.scatter(PFC_turn_times[index],yp,s=5,c='r',edgecolors='none')
    yv=yv+1
fn1='motor_push_i1-3526-0.gdf'
PFC_turn_ids=numpy.loadtxt(fn1)[:,0]
PFC_turn_times=numpy.loadtxt(fn1)[:,1]

id_min=int(numpy.amin(PFC_turn_ids))

ids=range(id_min,id_min+10)
print ids


for xin in ids:
    index=numpy.where(PFC_turn_ids==xin)[0]
    yp=numpy.ones(len(index))*yv
    #print len(index), len(yp), len(PFC_turn_times[index])
    pylab.scatter(PFC_turn_times[index],yp,s=5,c='b',edgecolors='none')
    yv=yv+1
pylab.xlim([-400,3300])
pylab.ylim([-5,105])
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




