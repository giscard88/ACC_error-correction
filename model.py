import numpy
import json
import pylab
import nest
import sys
flag=(sys.argv[1])
msd=int(sys.argv[2])
n_cues=int(sys.argv[3])
NS_flag=float(sys.argv[4])
PFC_flag=float(sys.argv[5])
ACC_PFC_flag=float(sys.argv[6])




nest.ResetKernel()
nest.SetKernelStatus({"resolution":0.1, "print_time":True, "overwrite_files":True})
nest.SetDefaults('iaf_psc_exp',{'tau_syn_ex':2.0,'tau_syn_in':2.0,'t_ref':3.0})

N_vp = nest.GetKernelStatus(['total_num_virtual_procs'])[0]
pyrngs = [numpy.random.RandomState(s) for s in range(msd, msd+N_vp)]
nest.SetKernelStatus({'grng_seed' : msd+N_vp})
nest.SetKernelStatus({'rng_seeds' : range(msd+N_vp+1, msd+2*N_vp+1)})
numpy.random.seed(msd)

PFC_turn=nest.Create('iaf_psc_exp',400)
PFC_push=nest.Create('iaf_psc_exp',400)
PFC_turn_i=nest.Create('iaf_psc_exp',100)
PFC_push_i=nest.Create('iaf_psc_exp',100)
PFC_inh=nest.Create('iaf_psc_exp',100)

motor_turn=nest.Create('iaf_psc_exp',400)
motor_push=nest.Create('iaf_psc_exp',400)
motor_turn_i=nest.Create('iaf_psc_exp',100)
motor_push_i=nest.Create('iaf_psc_exp',100)


ACC_tp=nest.Create('iaf_psc_exp',400)
ACC_pt=nest.Create('iaf_psc_exp',400)
ACC_tp_i=nest.Create('iaf_psc_exp',100)
ACC_pt_i=nest.Create('iaf_psc_exp',100)
ACC_other=nest.Create('iaf_psc_exp',400)

Hiper=-250.0

nest.SetStatus(ACC_tp,{'I_e':Hiper})
nest.SetStatus(ACC_pt,{'I_e':Hiper})
nest.SetStatus(ACC_tp_i,{'I_e':Hiper})
nest.SetStatus(ACC_pt_i,{'I_e':Hiper})
nest.SetStatus(ACC_other,{'I_e':Hiper})



All_cells={'PFC_turn':PFC_turn,'PFC_push':PFC_push, 'PFC_turn_i':PFC_turn_i, 'PFC_push_i':PFC_push_i,'PFC_inh':PFC_inh, 
           'motor_turn':motor_turn,'motor_push':motor_push,'motor_turn_i':motor_turn_i,'motor_push_i':motor_push_i,
           'ACC_turn':motor_turn,'ACC_push':motor_push,'ACC_turn_i':motor_turn_i,'ACC_push_i':motor_push_i}

noise_PFC=nest.Create('poisson_generator',1,{'rate':800.0})
#inh_PFC=nest.Create('poisson_generator',1,{'rate':20.0})
select_PFC=nest.Create('poisson_generator',1,{'rate':1200.0,'start':0.0,'stop':100.0})
noise_ACC=nest.Create('poisson_generator',1,{'rate':500.0})
noise_motor=nest.Create('poisson_generator',1,{'rate':300.0})
visual_cue1=nest.Create('poisson_generator',1,{'rate':300.0,'start':200.0,'stop':400.0})
visual_cue2=nest.Create('poisson_generator',1,{'rate':300.0,'start':1200.0,'stop':1400.0})
visual_cue3=nest.Create('poisson_generator',1,{'rate':300.0,'start':2200.0,'stop':2400.0})

visual_cue4=nest.Create('poisson_generator',1,{'rate':300.0,'start':3200.0,'stop':3400.0})
visual_cue5=nest.Create('poisson_generator',1,{'rate':300.0,'start':4200.0,'stop':4400.0})
visual_cue6=nest.Create('poisson_generator',1,{'rate':300.0,'start':5200.0,'stop':5400.0})

D_intra=2.0

conn_dict={'rule':'all_to_all'}
syn_dict={'weight':200.0,'delay':D_intra}
nest.Connect(noise_PFC,PFC_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(noise_PFC,PFC_push,conn_spec=conn_dict,syn_spec=syn_dict)

#conn_dict={'rule':'all_to_all'}
#syn_dict={'weight':-1000.0,'delay':D_intra}
#nest.Connect(inh_PFC,PFC_turn,conn_spec=conn_dict,syn_spec=syn_dict)
#nest.Connect(inh_PFC,PFC_push,conn_spec=conn_dict,syn_spec=syn_dict)



syn_dict={'weight':200.0,'delay':D_intra}
nest.Connect(select_PFC,PFC_turn,conn_spec=conn_dict,syn_spec=syn_dict)

nest.Connect(noise_motor,motor_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(noise_motor,motor_push,conn_spec=conn_dict,syn_spec=syn_dict)

nest.Connect(visual_cue1,motor_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(visual_cue1,motor_push,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(visual_cue2,motor_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(visual_cue2,motor_push,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(visual_cue3,motor_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(visual_cue3,motor_push,conn_spec=conn_dict,syn_spec=syn_dict)

nest.Connect(visual_cue4,motor_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(visual_cue4,motor_push,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(visual_cue5,motor_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(visual_cue5,motor_push,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(visual_cue6,motor_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(visual_cue6,motor_push,conn_spec=conn_dict,syn_spec=syn_dict)

nest.Connect(noise_ACC,ACC_tp,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(noise_ACC,ACC_pt,conn_spec=conn_dict,syn_spec=syn_dict)
#nest.Connect(noise_ACC,ACC_other,conn_spec=conn_dict,syn_spec=syn_dict)


noise_PFC_i=nest.Create('poisson_generator',1,{'rate':800.0})
noise_ACC_i=nest.Create('poisson_generator',1,{'rate':800.0})
noise_motor_i=nest.Create('poisson_generator',1,{'rate':900.0})

#nest.Connect(noise_PFC_i,PFC_inh,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(noise_PFC_i,PFC_turn_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(noise_PFC_i,PFC_push_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(noise_motor_i,motor_turn_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(noise_motor_i,motor_push_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(noise_ACC_i,ACC_tp_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(noise_ACC_i,ACC_pt_i,conn_spec=conn_dict,syn_spec=syn_dict)


sd_PFC_turn=nest.Create('spike_detector',params={'label':'PFC_turn'+str(msd),'withtime':True,'withgid':True,'to_file':True})
sd_PFC_push=nest.Create('spike_detector',params={'label':'PFC_push'+str(msd),'withtime':True,'withgid':True,'to_file':True})
sd_PFC_turn_i=nest.Create('spike_detector',params={'label':'PFC_turn_i'+str(msd),'withtime':True,'withgid':True,'to_file':True})
sd_PFC_push_i=nest.Create('spike_detector',params={'label':'PFC_push_i'+str(msd),'withtime':True,'withgid':True,'to_file':True})

sd_ACC_tp=nest.Create('spike_detector',params={'label':'ACC_tp'+str(msd),'withtime':True,'withgid':True,'to_file':True})
sd_ACC_pt=nest.Create('spike_detector',params={'label':'ACC_pt'+str(msd),'withtime':True,'withgid':True,'to_file':True})
sd_ACC_tp_i=nest.Create('spike_detector',params={'label':'ACC_tp_i'+str(msd),'withtime':True,'withgid':True,'to_file':True})
sd_ACC_pt_i=nest.Create('spike_detector',params={'label':'ACC_pt_i'+str(msd),'withtime':True,'withgid':True,'to_file':True})
sd_ACC_other=nest.Create('spike_detector',params={'label':'ACC_other'+str(msd),'withtime':True,'withgid':True,'to_file':True})

sd_motor_turn=nest.Create('spike_detector',params={'label':'motor_turn'+str(msd),'withtime':True,'withgid':True,'to_file':True})
sd_motor_push=nest.Create('spike_detector',params={'label':'motor_push'+str(msd),'withtime':True,'withgid':True,'to_file':True})
sd_motor_turn_i=nest.Create('spike_detector',params={'label':'motor_turn_i'+str(msd),'withtime':True,'withgid':True,'to_file':True})
sd_motor_push_i=nest.Create('spike_detector',params={'label':'motor_push_i'+str(msd),'withtime':True,'withgid':True,'to_file':True})



nest.Connect(PFC_turn,sd_PFC_turn)
nest.Connect(PFC_push,sd_PFC_push)
nest.Connect(PFC_turn_i,sd_PFC_turn_i)
nest.Connect(PFC_push_i,sd_PFC_push_i)
nest.Connect(motor_turn,sd_motor_turn)
nest.Connect(motor_push,sd_motor_push)
nest.Connect(motor_turn_i,sd_motor_turn_i)
nest.Connect(motor_push_i,sd_motor_push_i)
nest.Connect(ACC_tp,sd_ACC_tp)
nest.Connect(ACC_pt,sd_ACC_pt)
nest.Connect(ACC_tp_i,sd_ACC_tp_i)
nest.Connect(ACC_pt_i,sd_ACC_pt_i)
nest.Connect(ACC_other,sd_ACC_other)






#Let's start with recurrent connections
#Let's built PFC 
conn_dict={'rule':'pairwise_bernoulli','p':0.1}
syn_dict={'weight':150.0,'delay':D_intra}
nest.Connect(PFC_turn,PFC_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(PFC_push,PFC_push,conn_spec=conn_dict,syn_spec=syn_dict)

conn_dict={'rule':'pairwise_bernoulli','p':0.05}
syn_dict={'weight':50.0*PFC_flag,'delay':D_intra}
nest.Connect(PFC_turn,PFC_push,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(PFC_push,PFC_turn,conn_spec=conn_dict,syn_spec=syn_dict)


conn_dict={'rule':'pairwise_bernoulli','p':0.1}
syn_dict={'weight':200.0,'delay':D_intra}
nest.Connect(PFC_push,PFC_turn_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(PFC_turn,PFC_push_i,conn_spec=conn_dict,syn_spec=syn_dict)
conn_dict={'rule':'pairwise_bernoulli','p':0.1}
syn_dict={'weight':20.0,'delay':D_intra}
nest.Connect(PFC_push,PFC_push_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(PFC_turn,PFC_turn_i,conn_spec=conn_dict,syn_spec=syn_dict)

conn_dict={'rule':'pairwise_bernoulli','p':0.2}
syn_dict={'weight':-400.0,'delay':D_intra}
nest.Connect(PFC_turn_i,PFC_turn_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(PFC_push_i,PFC_push_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(PFC_turn_i,PFC_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(PFC_push_i,PFC_push,conn_spec=conn_dict,syn_spec=syn_dict)


#Let's motor cortex
conn_dict={'rule':'pairwise_bernoulli','p':0.1}
syn_dict={'weight':50.0,'delay':D_intra}
nest.Connect(motor_turn,motor_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(motor_push,motor_push,conn_spec=conn_dict,syn_spec=syn_dict)

conn_dict={'rule':'pairwise_bernoulli','p':0.1}
syn_dict={'weight':50.0,'delay':D_intra}
nest.Connect(motor_turn,motor_turn_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(motor_push,motor_push_i,conn_spec=conn_dict,syn_spec=syn_dict)

conn_dict={'rule':'pairwise_bernoulli','p':0.3}
syn_dict={'weight':-400.0,'delay':D_intra}
nest.Connect(motor_turn_i,motor_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(motor_push_i,motor_push,conn_spec=conn_dict,syn_spec=syn_dict)

conn_dict={'rule':'pairwise_bernoulli','p':0.3}
syn_dict={'weight':-400.0,'delay':D_intra}
nest.Connect(motor_turn_i,motor_turn_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(motor_push_i,motor_push_i,conn_spec=conn_dict,syn_spec=syn_dict)


#Let's build ACC 
conn_dict={'rule':'pairwise_bernoulli','p':0.1}
syn_dict={'weight':80.0,'delay':D_intra}
nest.Connect(ACC_tp,ACC_tp,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(ACC_pt,ACC_pt,conn_spec=conn_dict,syn_spec=syn_dict)

#conn_dict={'rule':'pairwise_bernoulli','p':0.04}
#syn_dict={'weight':50.0,'delay':D_intra}
#nest.Connect(ACC_tp,ACC_pt,conn_spec=conn_dict,syn_spec=syn_dict)
#nest.Connect(ACC_pt,ACC_tp,conn_spec=conn_dict,syn_spec=syn_dict)

conn_dict={'rule':'pairwise_bernoulli','p':0.05}
syn_dict={'weight':10.0,'delay':D_intra}
#nest.Connect(ACC_tp,ACC_tp_i,conn_spec=conn_dict,syn_spec=syn_dict)
#nest.Connect(ACC_pt,ACC_pt_i,conn_spec=conn_dict,syn_spec=syn_dict)

conn_dict={'rule':'pairwise_bernoulli','p':0.05}
syn_dict={'weight':-50.0,'delay':D_intra}
nest.Connect(ACC_tp_i,ACC_tp_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(ACC_pt_i,ACC_pt_i,conn_spec=conn_dict,syn_spec=syn_dict)

conn_dict={'rule':'pairwise_bernoulli','p':0.05}
syn_dict={'weight':-100.0,'delay':D_intra}
nest.Connect(ACC_tp_i,ACC_tp,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(ACC_pt_i,ACC_pt,conn_spec=conn_dict,syn_spec=syn_dict)


conn_dict={'rule':'pairwise_bernoulli','p':0.2}
syn_dict={'weight':60.0,'delay':D_intra}
nest.Connect(ACC_other,ACC_other,conn_spec=conn_dict,syn_spec=syn_dict)
conn_dict={'rule':'pairwise_bernoulli','p':0.1}
syn_dict={'weight':100.0*NS_flag,'delay':D_intra}
nest.Connect(ACC_tp,ACC_other,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(ACC_pt,ACC_other,conn_spec=conn_dict,syn_spec=syn_dict)

conn_dict={'rule':'pairwise_bernoulli','p':0.1}
syn_dict={'weight':100.0*NS_flag,'delay':D_intra}
nest.Connect(ACC_other,ACC_tp_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(ACC_other,ACC_pt_i,conn_spec=conn_dict,syn_spec=syn_dict)


D_inter=5.0




#PFC->ACC
conn_dict={'rule':'pairwise_bernoulli','p':0.1}
syn_dict={'weight':3.0,'delay':D_inter}
nest.Connect(PFC_turn,ACC_tp,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(PFC_push,ACC_pt,conn_spec=conn_dict,syn_spec=syn_dict)

#ACC->PFC
conn_dict={'rule':'pairwise_bernoulli','p':0.3}
syn_dict={'weight':100.0*ACC_PFC_flag,'delay':D_inter}
nest.Connect(ACC_tp,PFC_turn_i,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(ACC_pt,PFC_push_i,conn_spec=conn_dict,syn_spec=syn_dict)

#conn_dict={'rule':'pairwise_bernoulli','p':0.8}
#syn_dict={'weight':100.0,'delay':D_inter}
#nest.Connect(ACC_tp,PFC_push,conn_spec=conn_dict,syn_spec=syn_dict)
#nest.Connect(ACC_pt,PFC_turn,conn_spec=conn_dict,syn_spec=syn_dict)

#conn_dict={'rule':'pairwise_bernoulli','p':0.2}
#syn_dict={'weight':100.0,'delay':D_inter}
#nest.Connect(ACC_tp,PFC_push,conn_spec=conn_dict,syn_spec=syn_dict)
#nest.Connect(ACC_pt,PFC_turn,conn_spec=conn_dict,syn_spec=syn_dict)



#PFC->motor cortex
conn_dict={'rule':'pairwise_bernoulli','p':0.05}
syn_dict={'weight':10.0,'delay':D_inter}
nest.Connect(PFC_turn,motor_turn,conn_spec=conn_dict,syn_spec=syn_dict)
nest.Connect(PFC_push,motor_push,conn_spec=conn_dict,syn_spec=syn_dict)

#motor cortex->ACC
# all-to-all connections from motor cortex to ACC are established is to make ACC active when the conflict occurs.
conn_dict={'rule':'pairwise_bernoulli','p':0.2}
syn_dict={'weight':100.0,'delay':D_inter} 
nest.Connect(motor_turn,ACC_tp,conn_spec=conn_dict,syn_spec=syn_dict)  
nest.Connect(motor_turn,ACC_pt,conn_spec=conn_dict,syn_spec=syn_dict) 
nest.Connect(motor_push,ACC_tp,conn_spec=conn_dict,syn_spec=syn_dict) 
nest.Connect(motor_push,ACC_pt,conn_spec=conn_dict,syn_spec=syn_dict)



nest.Simulate(2000.0)
if flag=='change':
    nest.SetStatus(ACC_tp,{'I_e':0.0})
    nest.SetStatus(ACC_pt,{'I_e':0.0})
    nest.SetStatus(ACC_tp_i,{'I_e':0.0})
    nest.SetStatus(ACC_pt_i,{'I_e':0.0})
    nest.SetStatus(ACC_other,{'I_e':0.0})

nest.Simulate(400.0) #2400.0

spikes_motor_turn1=nest.GetStatus(sd_motor_turn,"events")[0]
spikes_motor_push1=nest.GetStatus(sd_motor_push,"events")[0]
times_turn=spikes_motor_turn1['times']
times_push=spikes_motor_push1['times']
sel_turn=numpy.where((times_turn>2200.0)&(times_turn<=2400.))
sel_push=numpy.where((times_push>2200.0)&(times_push<=2400.))

turn_n=len(sel_turn[0])
push_n=len(sel_push[0])

print turn_n, push_n
if flag=='change':
    if push_n>turn_n:
        #print 'okay'
        nest.SetStatus(ACC_tp,{'I_e':Hiper})
        nest.SetStatus(ACC_pt,{'I_e':Hiper})
        nest.SetStatus(ACC_tp_i,{'I_e':Hiper})
        nest.SetStatus(ACC_pt_i,{'I_e':Hiper})
        nest.SetStatus(ACC_other,{'I_e':Hiper})
    else:
        nest.SetStatus(ACC_tp,{'I_e':0.0})
        nest.SetStatus(ACC_pt,{'I_e':0.0})
        nest.SetStatus(ACC_tp_i,{'I_e':0.0})
        nest.SetStatus(ACC_pt_i,{'I_e':0.0})
        nest.SetStatus(ACC_other,{'I_e':0.0})
else:
    if push_n<turn_n:
        #print 'okay'
        nest.SetStatus(ACC_tp,{'I_e':Hiper})
        nest.SetStatus(ACC_pt,{'I_e':Hiper})
        nest.SetStatus(ACC_tp_i,{'I_e':Hiper})
        nest.SetStatus(ACC_pt_i,{'I_e':Hiper})
        nest.SetStatus(ACC_other,{'I_e':Hiper})
    else:
        nest.SetStatus(ACC_tp,{'I_e':0.0})
        nest.SetStatus(ACC_pt,{'I_e':0.0})
        nest.SetStatus(ACC_tp_i,{'I_e':0.0})
        nest.SetStatus(ACC_pt_i,{'I_e':0.0})
        nest.SetStatus(ACC_other,{'I_e':0.0})


if n_cues==3:
    nest.Simulate(800.0) #3400.0
else:
    nest.Simulate(1000.0) #3400.0

    spikes_motor_turn1=nest.GetStatus(sd_motor_turn,"events")[0]
    spikes_motor_push1=nest.GetStatus(sd_motor_push,"events")[0]
    times_turn=spikes_motor_turn1['times']
    times_push=spikes_motor_push1['times']
    sel_turn=numpy.where((times_turn>3200.0)&(times_turn<=3400.))
    sel_push=numpy.where((times_push>3200.0)&(times_push<=3400.))

    turn_n=len(sel_turn[0])
    push_n=len(sel_push[0])

    print turn_n, push_n
    if flag=='change':
        if push_n>turn_n:
            #print 'okay'
            nest.SetStatus(ACC_tp,{'I_e':Hiper})
            nest.SetStatus(ACC_pt,{'I_e':Hiper})
            nest.SetStatus(ACC_tp_i,{'I_e':Hiper})
            nest.SetStatus(ACC_pt_i,{'I_e':Hiper})
            nest.SetStatus(ACC_other,{'I_e':Hiper})
        else:
            nest.SetStatus(ACC_tp,{'I_e':0.0})
            nest.SetStatus(ACC_pt,{'I_e':0.0})
            nest.SetStatus(ACC_tp_i,{'I_e':0.0})
            nest.SetStatus(ACC_pt_i,{'I_e':0.0})
            nest.SetStatus(ACC_other,{'I_e':0.0})
    else:
        if push_n<turn_n:
            #print 'okay'
            nest.SetStatus(ACC_tp,{'I_e':Hiper})
            nest.SetStatus(ACC_pt,{'I_e':Hiper})
            nest.SetStatus(ACC_tp_i,{'I_e':Hiper})
            nest.SetStatus(ACC_pt_i,{'I_e':Hiper})
            nest.SetStatus(ACC_other,{'I_e':Hiper})
        else:
            nest.SetStatus(ACC_tp,{'I_e':0.0})
            nest.SetStatus(ACC_pt,{'I_e':0.0})
            nest.SetStatus(ACC_tp_i,{'I_e':0.0})
            nest.SetStatus(ACC_pt_i,{'I_e':0.0})
            nest.SetStatus(ACC_other,{'I_e':0.0})


    nest.Simulate(1000.0) #4400.0

    spikes_motor_turn1=nest.GetStatus(sd_motor_turn,"events")[0]
    spikes_motor_push1=nest.GetStatus(sd_motor_push,"events")[0]
    times_turn=spikes_motor_turn1['times']
    times_push=spikes_motor_push1['times']
    sel_turn=numpy.where((times_turn>4200.0)&(times_turn<=4400.))
    sel_push=numpy.where((times_push>4200.0)&(times_push<=4400.))

    turn_n=len(sel_turn[0])
    push_n=len(sel_push[0])

    print turn_n, push_n
    if flag=='change':
        if push_n>turn_n:
            #print 'okay'
            nest.SetStatus(ACC_tp,{'I_e':Hiper})
            nest.SetStatus(ACC_pt,{'I_e':Hiper})
            nest.SetStatus(ACC_tp_i,{'I_e':Hiper})
            nest.SetStatus(ACC_pt_i,{'I_e':Hiper})
            nest.SetStatus(ACC_other,{'I_e':Hiper})
        else:
            nest.SetStatus(ACC_tp,{'I_e':0.0})
            nest.SetStatus(ACC_pt,{'I_e':0.0})
            nest.SetStatus(ACC_tp_i,{'I_e':0.0})
            nest.SetStatus(ACC_pt_i,{'I_e':0.0})
            nest.SetStatus(ACC_other,{'I_e':0.0})
    else:
        if push_n<turn_n:
            #print 'okay'
            nest.SetStatus(ACC_tp,{'I_e':Hiper})
            nest.SetStatus(ACC_pt,{'I_e':Hiper})
            nest.SetStatus(ACC_tp_i,{'I_e':Hiper})
            nest.SetStatus(ACC_pt_i,{'I_e':Hiper})
            nest.SetStatus(ACC_other,{'I_e':Hiper})
        else:
            nest.SetStatus(ACC_tp,{'I_e':0.0})
            nest.SetStatus(ACC_pt,{'I_e':0.0})
            nest.SetStatus(ACC_tp_i,{'I_e':0.0})
            nest.SetStatus(ACC_pt_i,{'I_e':0.0})
            nest.SetStatus(ACC_other,{'I_e':0.0})

    nest.Simulate(1000.0) #5400.0




    spikes_motor_turn1=nest.GetStatus(sd_motor_turn,"events")[0]
    spikes_motor_push1=nest.GetStatus(sd_motor_push,"events")[0]
    times_turn=spikes_motor_turn1['times']
    times_push=spikes_motor_push1['times']
    sel_turn=numpy.where((times_turn>5200.0)&(times_turn<=5400.))
    sel_push=numpy.where((times_push>5200.0)&(times_push<=5400.))

    turn_n=len(sel_turn[0])
    push_n=len(sel_push[0])

    print turn_n, push_n
    if flag=='change':
        if push_n>turn_n:
            #print 'okay'
            nest.SetStatus(ACC_tp,{'I_e':Hiper})
            nest.SetStatus(ACC_pt,{'I_e':Hiper})
            nest.SetStatus(ACC_tp_i,{'I_e':Hiper})
            nest.SetStatus(ACC_pt_i,{'I_e':Hiper})
            nest.SetStatus(ACC_other,{'I_e':Hiper})
        else:
            nest.SetStatus(ACC_tp,{'I_e':0.0})
            nest.SetStatus(ACC_pt,{'I_e':0.0})
            nest.SetStatus(ACC_tp_i,{'I_e':0.0})
            nest.SetStatus(ACC_pt_i,{'I_e':0.0})
            nest.SetStatus(ACC_other,{'I_e':0.0})
    else:
        if push_n<turn_n:
            #print 'okay'
            nest.SetStatus(ACC_tp,{'I_e':Hiper})
            nest.SetStatus(ACC_pt,{'I_e':Hiper})
            nest.SetStatus(ACC_tp_i,{'I_e':Hiper})
            nest.SetStatus(ACC_pt_i,{'I_e':Hiper})
            nest.SetStatus(ACC_other,{'I_e':Hiper})
        else:
            nest.SetStatus(ACC_tp,{'I_e':0.0})
            nest.SetStatus(ACC_pt,{'I_e':0.0})
            nest.SetStatus(ACC_tp_i,{'I_e':0.0})
            nest.SetStatus(ACC_pt_i,{'I_e':0.0})
            nest.SetStatus(ACC_other,{'I_e':0.0})

    nest.Simulate(1000.0) #6400.0

spikes_PFC_turn=nest.GetStatus(sd_PFC_turn,"events")[0]
spikes_PFC_push=nest.GetStatus(sd_PFC_push,"events")[0]
spikes_PFC_turn_i=nest.GetStatus(sd_PFC_turn_i,"events")[0]
spikes_PFC_push_i=nest.GetStatus(sd_PFC_push_i,"events")[0]

spikes_ACC_tp=nest.GetStatus(sd_ACC_tp,"events")[0]
spikes_ACC_pt=nest.GetStatus(sd_ACC_pt,"events")[0]
spikes_ACC_tp_i=nest.GetStatus(sd_ACC_tp_i,"events")[0]
spikes_ACC_pt_i=nest.GetStatus(sd_ACC_pt_i,"events")[0]
spikes_ACC_other=nest.GetStatus(sd_ACC_other,"events")[0]

spikes_motor_turn=nest.GetStatus(sd_motor_turn,"events")[0]
spikes_motor_push=nest.GetStatus(sd_motor_push,"events")[0]
spikes_motor_turn_i=nest.GetStatus(sd_motor_turn_i,"events")[0]
spikes_motor_push_i=nest.GetStatus(sd_motor_push_i,"events")[0]

pylab.figure(1)
pylab.scatter(spikes_PFC_turn['times'],spikes_PFC_turn['senders'],s=1,c='r', edgecolor='',label='turn')
pylab.scatter(spikes_PFC_push['times'],spikes_PFC_push['senders'],s=1,c='b', edgecolor='',label='push')
pylab.scatter(spikes_PFC_turn_i['times'],spikes_PFC_turn_i['senders'],s=1,c='k', edgecolor='',label='turn_i')
pylab.scatter(spikes_PFC_push_i['times'],spikes_PFC_push_i['senders'],s=1,c='g', edgecolor='',label='push_i')
pylab.legend()
pylab.title('PFC')
pylab.savefig('figures/PFC'+str(msd)+'.png')
#pylab.savefig('PFC'+str(msd)+'.eps')



pylab.figure(2)
pylab.scatter(spikes_motor_turn['times'],spikes_motor_turn['senders'],s=1,c='r', edgecolor='',label='turn')
pylab.scatter(spikes_motor_push['times'],spikes_motor_push['senders'],s=1,c='b', edgecolor='',label='push')
pylab.scatter(spikes_motor_turn_i['times'],spikes_motor_turn_i['senders'],s=1,c='k', edgecolor='',label='turn_i')
pylab.scatter(spikes_motor_push_i['times'],spikes_motor_push_i['senders'],s=1,c='g', edgecolor='',label='push_i')
pylab.legend()
pylab.title('motor')
pylab.savefig('figures/motor'+str(msd)+'.png')
#pylab.savefig('motor'+str(msd)+'.eps')


pylab.figure(3)
pylab.scatter(spikes_ACC_tp['times'],spikes_ACC_tp['senders'],s=1,c='r', edgecolor='',label='turn')
pylab.scatter(spikes_ACC_pt['times'],spikes_ACC_pt['senders'],s=1,c='b', edgecolor='',label='push')
pylab.scatter(spikes_ACC_tp_i['times'],spikes_ACC_tp_i['senders'],s=1,c='k', edgecolor='',label='turn_i')
pylab.scatter(spikes_ACC_pt_i['times'],spikes_ACC_pt_i['senders'],s=1,c='g', edgecolor='',label='push_i')
pylab.scatter(spikes_ACC_other['times'],spikes_ACC_other['senders'],s=1,c='m', edgecolor='',label='other')
pylab.legend(loc=3)
pylab.title('ACC')
pylab.savefig('figures/ACC'+str(msd)+'.png')
#pylab.savefig('ACC'+str(msd)+'.eps')





#pylab.show()






5
