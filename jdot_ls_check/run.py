#!/usr/bin/env python3
import os
from subprocess import *
from inlist_project_generator import *
def check_okay(return_code):
    if return_code != 0:
        exit()
def inlist2(i):
    ret2=run('cp'+
def inlist1(i):
    namefile=open('inlist1_run','r')
    nm=namefile.read()
    index=round(i*0.005+0.45,3)
#    fluxarr=np.genfromtxt('../planet/fluxfile.txt')
#    flux=fluxarr[i]
#    print(flux)
    nm1=nm.replace('<<period>>','_'+ str(index)+'days_')
    model_name=str(index)+'_P'
    nm2=nm1.replace('<<model_period>>',model_name)
#    nm3=nm2.replace('<<flux>>',str(flux))
    namefile.close()
    filename=open('inlist1','w')
    filename.write(nm2)
    filename.close()
def do_one(inlist_project_name):
    ret3=run('cp '+inlist_project_name+' inlist_project',shell=True)
    run_ret=run('./rn',shell=True)
namefile3=open('namefile3.txt','r')
nm3=namefile3.read()
nmlist3=nm3.split()
ret=run('rm ./LOGS1/history*.data',shell=True)
ret=run('rm ./LOGS2/history*.data',shell=True)
ret=run('rm ./LOGS1/profile*.data',shell=True)
ret=run('rm ./LOGS2/profile*.data',shell=True)
ret=run('rm *_days_.data',shell=True)
index=0.48
if os.path.isfile('../planet/planet_evolve_'+str(index)+'_P.mod')==True and os.path.isfile('../planet/LOGS/history_'+str(index)+'_days.data')==True:
    inlist1(i)
    inlist2(i)
    do_one(nmlist3[i])

