#_________________________________sample preparation in LAMMPS
setenv NATOMS  4000                         # Number of all atoms
setenv element 2                            # Number of types of atom
setenv type1   Zr                           #The type of first elememt 
setenv type2   Cu                           #The type of second element
#setenv type3 *
setenv Con_Ini model_300K.lammps            #The inital confguration
setenv P_T eam/alloy                        #Porential type (only for metal)  
setenv Potential ZrCu.lammps.eam #Potental file name
setenv Temperature 300                      #simulation temperature
setenv timestep 0.002                       #simulation timestep
setenv step 10000000     #simulation step
#________________________________________simulation setting in WT-metaD

##############################   Global setting
setenv colvarsTrajFrequency 100
setenv colvarsRestartFrequency 100000

##############################  Colvar setting
setenv Colname  dist
setenv width    0.01    #samping interval 
setenv lowerBoundary 0                       #
setenv upperBoundary 10                        #
setenv expandBoundaries on                        #
###############################  WT-metaD setting
setenv hillWidth 35	                       #Guassain width
setenv outputEnergy on                       #output energy
setenv hillweight 0.01                       #hight of Gaussian hill 
setenv newHillFrequency 1000                 #deposite frequency 
setenv writeFreeEnergyFile on                #write FreeEnergyfile 
setenv saveFreeEnergyFile on                 #save FreeEnergyfile
setenv wellTempered  on                      # Well tempered method for calculation
setenv biasTemperature  2700                 # temperature for bias potential 
#_________________________________mpirun calculation
setenv mpi_commd mpirun                      # your system mpi command
setenv LAMMPS_commd lmp_mpi                  #your LAMMPS  executive program
setenv mpi_np 12                             #applying for CPU cores
