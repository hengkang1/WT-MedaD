program m
integer b,i,natom,typ,j,typp(4000),id
real xl,yl,zl,xe,ye,ze,zb(4000,3),cut
real dx,dy,dz
print*, "input plase input atom numbsr:"
read(*,*),b
print*,"please input cutoff:"
read(*,*)cut
open(unit=1,file="model_300K.lammps")
read(1,*),natom
read(1,*),typ
read(1,*),xe,xl
read(1,*),ye,yl
read(1,*),ze,zl
do i=1,natom
read(1,*),id,typp(id),(zb(id,j),j=1,3)
end do 
    do j=1,natom
        if(j==b)cycle
        dx=zb(j,1)-zb(b,1)
        dy=zb(j,2)-zb(b,2)
        dz=zb(j,3)-zb(b,3)
dx=dx-anint(dx/(xl-xe))*(xl-xe)
dy=dy-anint(dy/(yl-xe))*(yl-ye)
dz=dz-anint(dz/(zl-xe))*(zl-ze)
dis=sqrt(dx**2+dy**2+dz**2)
if(dis.le.cut) print*,j,zb(j,1),zb(j,2),zb(j,3)
end do 
    end
