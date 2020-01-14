      SUBROUTINE DFLUX(FLUX,SOL,JSTEP,JINC,TIME,NOEL,NPT,COORDS,JLTYP,
     1                 TEMP,PRESS,SNAME)
C
      INCLUDE 'ABA_PARAM.INC'
C
      parameter(one=1.d0)
      DIMENSION COORDS(3),FLUX(2),TIME(2)
      CHARACTER*80 SNAME
      D0=1D-5
      D1=1e-7
      D2=1e-6
      D3=1e-8	
      D=D0+D1*TEMP+D2*PRESS+D3*TEMP*PRESS
      if (flux(1) .eq. one) then
        FLUX(1)=-D*SOL
        FLUX(2)=-D
      endif
      RETURN
      END
