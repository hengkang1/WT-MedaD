# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 23:03:08 2020

@author: Administrator
E-mail:kangheng921117@163.com
"""
import os,sys
###################
def D_FE(filename):
    with open(filename,'r') as f:
        CV=[]
        CVn=[]
        FRE=[]
        FREn=[]
        f.readline()
        f.readline()
        f.readline()
        lines=f.readlines()
        for line in lines:
            value=[float(s) for s in line.split()]
            if(value[0]>0):
                CV.append(value[0])
                FRE.append(value[1])
        for i in range (0,len(CV)-2):
            if((FRE[i+1]-FRE[i])*(FRE[i+2]-FRE[i+1])<0):
                CVn.append(CV[i+1])
                FREn.append(FRE[i+1])  
        return CVn,FREn
if not os.path.exists("../RMSD-WT.sh"):
    print "there is no RMSD-WT.sh file, please check it out!"
    sys.exit()
with open('../RMSD-WT.sh') as p:
    lines=p.readlines()
   # lines=lines.decode("utf-8")
    for line in lines:
        if (line[0:6]=="setenv"):
            value=[str(s) for s in line.split()]
            if(value[1]=="step"):
                step=value[2]
filename="out."+str(step)+'.pmf.BAK'
(CVn,FREn)=D_FE(filename)
inn=CVn[0]
sad=CVn[1]
fin=CVn[2]
AF=(FREn[1]-FREn[0])
RF=(FREn[1]-FREn[2])
fileout=open('FEL.txt','w')
fileout.write(str(inn)+'\n')
fileout.write(str(sad)+'\n')
fileout.write(str(fin)+'\n')
fileout.write(str(AF)+'\n')
fileout.write(str(RF))

             
        
        
        
        
        
        
        
        
