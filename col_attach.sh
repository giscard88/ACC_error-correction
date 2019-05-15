#!/bin/bash

#DN='change_3111'
#mkdir $DN
#cp model.py $DN
#cd $DN
#mkdir figures
#for i in $(seq 1 1 100)
#do
#python model.py change $i 3 1 1 1 #change or no, seed, n_cues, NS, PFC, ACC_PFC
#done

#cd ..

DN='nochange_3111'
mkdir $DN
cp model.py $DN
cd $DN
mkdir figures
for i in $(seq 1 1 100)
do
python model.py nochange $i 3 1 1 1 #change or no, seed, n_cues, NS, PFC, ACC_PFC
done

cd ..

#DN='change_3011'
#mkdir $DN
#cp model.py $DN
#cd $DN
#mkdir figures
#for i in $(seq 1 1 100)
#do
#python model.py change $i 3 0 1 1 #change or no, seed, n_cues, NS, PFC, ACC_PFC
#done

#cd ..
