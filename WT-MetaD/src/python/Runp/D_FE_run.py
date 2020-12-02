# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 15:25:38 2020

@author: Administrator
E-mail:kangheng921117@163.com
"""
import os,sys
if not os.path.exists("RMSD-WT.sh"):
    print "there is no RMSD-WT.sh file, please check it out!"
    sys.exit()
with open('RMSD-WT.sh') as p:
    lines=p.readlines()
   # lines=lines.decode("utf-8")
    for line in lines:
        if (line[0:6]=="setenv"):
            value=[str(s) for s in line.split()]
            if(value[1]=="step"):
                step=value[2]
os.system('mkdir FEL-I')
filename="out."+step+'.pmf.BAK'
with open('interest_atom.txt','r') as k:
     Ia=[]
     lines=k.readlines()
     for line in lines:
         value=[int(s) for s in line.split()]
         Ia.append(value[0])
for i in range (0,len(Ia)):
    path=str(Ia[i])
    if not os.path.exists(path+'/'+filename):
        continue
	print 'the group '+path+' has not sccuess'
    else:
	print 'calculate group '+path+' please waiting!'
        os.system('cd '+path+" && CalDF1 && mv FEL.txt ../FEL-I/FEL-"+path+".txt && cd ../ && sleep 5")

        
        
        
        
        
        
