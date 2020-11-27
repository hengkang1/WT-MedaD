# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:57:20 2020

@author: Administrator
"""
import os,sys
from shutil import copy
if not os.path.exists("HOPE-WT.sh"):
    print "there is no HOPE-WT.sh file, please check it out!"
    sys.exit()
with open('HOPE-WT.sh') as p:
    lines=p.readlines()
   # lines=lines.decode("utf-8")
    for line in lines:
        if (line[0:6]=="setenv"):
            value=[str(s) for s in line.split()]
            if(value[1]=="NATOMS"):
                natoms=value[2]
            if(value[1]=="element"):
                element=value[2]
            if(value[1]=="type1"):
                type1=value[2]
            if(value[1]=="type2"):
                type2=value[2]
            if(value[1]=="type3"):
                type3=value[2]
            if(value[1]=="Con_Ini"):
                Con_Ini=value[2]
            if(value[1]=="Potential"):
                Potential=value[2]
            if(value[1]=="Temperature"):
                Temperature=value[2]
            if(value[1]=="hillWidth"):
                hillWidth=value[2]
            if(value[1]=="outputEnergy"):
                outputEnergy=value[2]
            if(value[1]=="hillweight"):
                hillweight=value[2]
            if(value[1]=="newHillFrequency"):
                newHillFrequency=value[2]
            if(value[1]=="writeFreeEnergyFile"):
                writeFreeEnergyFile=value[2]
            if(value[1]=="saveFreeEnergyFile"):
                saveFreeEnergyFile=value[2]
            if(value[1]=="wellTempered"):
                wellTempered=value[2]
            if(value[1]=="biasTemperature"):
                biasTemperature=value[2]
            if(value[1]=="lowerBoundary"):
                lowerBoundary=value[2]
            if(value[1]=="upperBoundary"):
                upperBoundary=value[2]
            if(value[1]=="expandBoundaries"):
                expandBoundaries=value[2]
            if(value[1]=="P_T"):
                P_T=value[2]
            if(value[1]=="timestep"):
                timestep=value[2]
            if(value[1]=="step"):
                step=value[2]
            if(value[1]=="colvarsTrajFrequency"):
                colvarsTrajFrequency=value[2]
            if(value[1]=="colvarsRestartFrequency"):
                colvarsRestartFrequency=value[2]
            if(value[1]=="Colname"):
                Colname=value[2]
            if(value[1]=="width"):
                width=value[2]
if not os.path.exists(Con_Ini):
    print "there is no configuration file, please check it out!"
    sys.exit()
with open(Con_Ini,'r') as p:
    nid=[]
    typ=[]
    x=[]
    y=[]
    z=[]    
    p.readline()
    p.readline()
    p.readline()
    p.readline()
    xl=p.readline()
    vax=[float(s) for s in xl.split()[0:2]]
    dx=vax[1]-vax[0]
    yl=p.readline()
    vay=[float(s) for s in yl.split()[0:2]]
    dy=vay[1]-vay[0]
    zl=p.readline()
    vaz=[float(s) for s in zl.split()[0:2]]
    dz=vaz[1]-vaz[0]
    p.readline()
    p.readline()
    p.readline()
    lines=p.readlines()
   # lines=lines.decode("utf-8")
    for line in lines:
        value=[int(s) for s in line.split()[0:2]]
        value1=[float(s) for s in line.split()[2:5]]
        nid.append(value[0])
        typ.append(value[1])
        x.append(value1[0])
        y.append(value1[1])
        z.append(value1[2])
inter=[]
if not os.path.exists("interest_atom.txt"):
    print "there is no interest_atom.txt file, please check it out!"
    sys.exit()
with open("interest_atom.txt",'r') as m:
    liness=m.readlines()
    for li in liness:
        if (int(li)<int(natoms)):
            inter.append(int(li)) 
for i in range (0,len(inter)):
    pathfi=str(inter[i])
    if not os.path.exists(pathfi):
        os.mkdir(pathfi)
    copy(Con_Ini,pathfi)
    copy(Potential,pathfi)
####################################################
for i in range (0,len(inter)):
    biao=nid.index(inter[i])
    rex=x[biao]
    rey=y[biao]
    rez=z[biao]    
#################################################################
    f=open(str(inter[i])+'/configfile','w')
    f.write('# collective variable example: monitor distances'+'\n')
    f.write(''+'\n')
    f.write('colvarsTrajFrequency '+colvarsTrajFrequency+' # output every 100 steps'+'\n')
    f.write('colvarsRestartFrequency '+colvarsRestartFrequency+'\n')
    f.write(''+'\n')
    f.write('colvar {'+'\n')
    f.write('  name '+Colname+'\n')
    f.write('  width '+width+'\n')
    f.write('  lowerBoundary '+lowerBoundary+'\n')
    f.write('  upperBoundary '+upperBoundary+'\n')
    f.write('  expandBoundaries '+expandBoundaries+'\n')
    f.write(''+'\n')
    f.write('  distance {'+'\n')
    f.write('    group1 {'+'\n')
    f.write('     atomNumbers '+str(inter[i])+'\n')
    f.write('    }'+'\n')
    f.write('     group2 {'+'\n')
    f.write('      dummyAtom ( '+str(rex)+', '+str(rey)+', '+str(rez)+' )'+'\n')
    f.write('    }'+'\n')
    f.write('  }'+'\n')
    f.write('}'+'\n')
    f.write(''+'\n')
    f.write(''+'\n')
    f.write('metadynamics {'+'\n')
    f.write('  name meta'+'\n')
    f.write('  colvars '+Colname+'\n')
    f.write('  hillWidth  ' + hillWidth +'\n')
    f.write('  outputEnergy '+outputEnergy+'\n')
    f.write('  hillWeight '+hillweight+'\n')
    f.write('  newHillFrequency '+newHillFrequency+'\n')
    f.write('  writeFreeEnergyFile '+writeFreeEnergyFile+'\n')
    f.write('  saveFreeEnergyFile '+saveFreeEnergyFile+'\n')
    f.write('  wellTempered '+wellTempered+'\n')
    f.write('  biasTemperature '+biasTemperature+'\n')
    f.write('}'+'\n')
    f.close()
######################################################################
    f=open(str(inter[i])+'/in.lammps','w')
    f.write('# ------------------------ INITIALIZATION ------------------------'+'\n')    
    f.write("units  metal"+'\n')
    f.write("dimension  3"+'\n')
    f.write("boundary  p  p  p"+'\n')
    f.write("atom_style  atomic"+'\n') 
    f.write("atom_modify map array sort 10000 2.0"+'\n')
    f.write(""+'\n')
    f.write('variable  T index  '+Temperature + '\n')
    f.write(""+'\n')
    f.write('read_data  '+ Con_Ini +'\n')
    f.write(''+'\n')
    f.write('# ------------------------ Interatomic Potential ----------------------------'+'\n')
    f.write('pair_style   '+ P_T +'\n')
    if(element=='3'):
        f.write('pair_coeff   * *  ' +Potential + '  '+type1 +'  '+ type2+ '  '+type3+'\n')
    if(element=='2'):
        f.write('pair_coeff   * *  ' +Potential + '  '+type1 +'  '+ type2+'\n')
    f.write('neighbor     2.0 bin'+'\n')
    f.write('neigh_modify check yes every 1 delay 0'+'\n')
    f.write(''+'\n')
    f.write('timestep  ' +timestep +'\n')
    f.write(''+'\n')
    f.write('##########initilization of velocities'+'\n')
    f.write('velocity all create $T 29612 mom yes rot no'+'\n')
    f.write(''+'\n')
    f.write('fix 1 all npt temp $T $T 0.2 aniso 0 0 2'+'\n')
    f.write(''+'\n')
    f.write('thermo 1000'+'\n')
    f.write('thermo_style custom step temp press pe ke etotal enthalpy vol density'+'\n')
    f.write(''+'\n')
    f.write('run   100000'+'\n')
    f.write('unfix 1'+'\n')
    f.write('reset_timestep  0'+'\n')
    f.write('fix 1 all nvt temp $T $T 0.2'+'\n')
    f.write('shell "rm -f out*.colvars.*"'+'\n')
    f.write('fix  2 all colvars configfile'+'\n')
    f.write(''+'\n')
    f.write('thermo 10000'+'\n')
    f.write('thermo_style custom step temp press pe ke etotal enthalpy vol density'+'\n')
    f.write(''+'\n')
    f.write('dump  1 all cfg 100000 snap_*.cfg mass type xs ys zs'+'\n')
    if(element=='2'):
        f.write('dump_modify     1 element '+type1+'  '+ type2+' sort id'+'\n')
    if(element=='3'):
        f.write('dump_modify     1 element '+type1+'  '+ type2+'  '+ type3+' sort id'+'\n')
    f.write('run   '+ step +'\n')
    #################################################################
       
    
    
    
    
    
    
    
    
    
    
