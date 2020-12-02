program runsimulation
implicit none
open(unit=1,file="path5.py")
write(1,"(20A)"),"from Sim import D_FE"
close(1)
call system("python path5.py && rm path5.py")
end
