#!/bin/bash



DN='change_push_3111'
mkdir $DN
cp model_control.py $DN
cd $DN
mkdir figures
for i in $(seq 1 1 100)
do
python model_control.py change $i 3 1 1 1 #change or no, seed, n_cues, NS, PFC, ACC_PFC
done

cd ..



