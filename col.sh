#!/bin/bash

DN='change_6111'
mkdir $DN
cp model.py $DN
cd $DN
mkdir figures
for i in $(seq 1 1 100)
do
python model.py change $i 6 1 1 1 #change or no, seed, n_cues, NS, PFC, ACC_PFC
done

cd ..

DN='change_6011'
mkdir $DN
cp model.py $DN
cd $DN
mkdir figures
for i in $(seq 1 1 100)
do
python model.py change $i 6 0 1 1 #change or no, seed, n_cues, NS, PFC, ACC_PFC
done

cd ..

DN='change_6101'
mkdir $DN
cp model.py $DN
cd $DN
mkdir figures
for i in $(seq 1 1 100)
do
python model.py change $i 6 1 0 1 #change or no, seed, n_cues, NS, PFC, ACC_PFC
done

cd ..

DN='change_6110'
mkdir $DN
cp model.py $DN
cd $DN
mkdir figures
for i in $(seq 1 1 100)
do
python model.py change $i 6 1 1 0 #change or no, seed, n_cues, NS, PFC, ACC_PFC
done

cd ..


DN='change_3111'
mkdir $DN
cp model.py $DN
cd $DN
mkdir figures
for i in $(seq 1 1 100)
do
python model.py change $i 3 1 1 1 #change or no, seed, n_cues, NS, PFC, ACC_PFC
done

cd ..

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

DN='change_3011'
mkdir $DN
cp model.py $DN
cd $DN
mkdir figures
for i in $(seq 1 1 100)
do
python model.py change $i 3 0 1 1 #change or no, seed, n_cues, NS, PFC, ACC_PFC
done

cd ..
