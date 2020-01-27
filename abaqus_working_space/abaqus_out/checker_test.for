        SUBROUTINE DFLUX(FLUX,SOL,JSTEP,JINC,TIME,NOEL,NPT,COORDS,JLTYP, TEMP,PRESS,SNAME)


            INCLUDE 'ABA_PARAM.INC'

c23456789 (This demonstrates column position!)         

            DIMENSION COORDS(3),FLUX(2),TIME(2)
            CHARACTER*80 SNAME

            real x(3)
            integer m,n,l   
            parameter (m=100, n=100, l =100)
            double precision, save :: data_out(100, 100, 100)
            integer, save:: r_file = 1
            integer, save:: counter = 1
            real t
            counter = counter  + 1

            if (r_file == 1) then
                open (unit=1,  file='C:\peter_abaqus\Summer-Research-Project\abaqus_working_space\abaqus_out\eps-000000000.h5', 
     $          form='unformatted',  access='direct', recl=100*100*100*2)
                read (1, rec=1) data_out
                close(1)
                print *, 'file is read'
                
                r_file = r_file + 1
            end if

            do i =1,3
                x(i) = ceiling((coords(i)+0.5)*100.0)
            end do
        
c            ! t = int(ceiling(time(1)*10))

            FLUX(1)=data_out(int(x(1)), int(x(2)), int(x(3)))**2*10e-4
            
c            ! if (mod(counter, 100) == 0) then
c            !       print *, flux(1)
c            ! end if

c            ! flux(1) = 10e-03
            FLUX(2) = 0


            RETURN
        END

c        ! # shutil.copyfile('C:/temp/dflux.inp', r'C:/peter_abaqus/Summer-Research-Project/abaqus_working_space/abaqus_out/dflux.inp')
c        ! # shutil.copyfile('C:/temp/umat_test.inp', r'C:/peter_abaqus/Summer-Research-Project/abaqus_working_space/abaqus_out/umat_test.inp')