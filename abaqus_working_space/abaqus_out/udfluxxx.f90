      SUBROUTINE DFLUX(FLUX,SOL,JSTEP,JINC,TIME,NOEL,NPT,COORDS,JLTYP, TEMP,PRESS,SNAME)

      INCLUDE 'ABA_PARAM.INC'

      DIMENSION COORDS(3),FLUX(2),TIME(2)
      CHARACTER*80 SNAME
      FLUX(1)=-250.*SOL
      FLUX(2)=-250.
      write(*, 1000) COORDS(1), COORDS(2), COORDS(3)
      1000 format (3(E14.4, 2x))
      write(*, 1001), time(1), time(2)
      1001 format (2(f8.5, 2x))
      RETURN
      END
 