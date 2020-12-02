program runsimulation
implicit none
open(unit=1,file="path6.py")
write(1,"(25A)"),"from Runp import D_FE_run"
close(1)
call system("python path6.py && rm path6.py")
end
