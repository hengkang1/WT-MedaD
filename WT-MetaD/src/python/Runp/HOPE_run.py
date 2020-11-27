# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:18:27 2020

@author: Administrator
"""
from Sim import HOPE
import os,sys
if not os.path.exists("HOPE-WT.sh"):
    print "there is no HOPE-WT.sh file, please check it out!"
    sys.exit()
with open('HOPE-WT.sh') as p:
    lines=p.readlines()
   # lines=lines.decode("utf-8")
    for line in lines:
        if (line[0:6]=="setenv"):
            value=[str(s) for s in line.split()]
            if(value[1]=="mpi_commd"):
                mpi_commd=value[2]
            if(value[1]=="LAMMPS_commd"):
                lmp_mpi=value[2]
            if(value[1]=="mpi_np"):
                mpi_np=value[2]
            if(value[1]=="NATOMS"):
                natoms=value[2]
inter=[]
comd=mpi_commd+" -np "+mpi_np+" "+lmp_mpi+" <in.lammps &&"
comd3="cd ../"
with open("interest_atom.txt",'r') as m:
    liness=m.readlines()
    for li in liness:
        if (int(li)<int(natoms)):
            inter.append(int(li))
for i in range (0,len(inter)):
    fi=str(inter[i])
    comd1="cd "+fi+" &&"
    os.system(comd1+comd+comd3)
    
    
            
            
            
            
            
