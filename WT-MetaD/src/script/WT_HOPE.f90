program runsimulation
implicit none
open(unit=1,file="path.py")
write(1,"(25A)"),"from Runp import HOPE_run"
close(1)
call system("python2.7 path.py && rm path.py")
end
