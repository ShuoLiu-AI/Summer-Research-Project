SUBROUTINE DFLUX(FLUX,SOL,JSTEP,JINC,TIME,NOEL,NPT,COORDS,JLTYP, TEMP,PRESS,SNAME)


      INCLUDE 'ABA_PARAM.INC'

      DIMENSION COORDS(3),FLUX(2),TIME(2)
      CHARACTER*80 SNAME

      integer m,n,l
      parameter (m=100, n=100, l =100)
      double precision, save :: data_out(100, 100, 100)
      integer, save:: r_file = 1

      if (r_file == 1) then
            open (unit=1,  file='C:\peter_abaqus\Summer-Research-Project\fortran_read\out.peter', form='unformatted',  access='direct', recl=100*100*100*2)
            print *, 'file is read'
      end if
      r_file = r_file + 1

      print *, coords
      ! read (1, rec=1) data_out
    
      FLUX(1)=-250.*SOL
      FLUX(2)=-250.


      RETURN
END

