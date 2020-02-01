	    SUBROUTINE UMAT(STRESS,STATEV,DDSDDE,SSE,SPD,SCD,
     & RPL,DDSDDT,DRPLDE,DRPLDT,
     & STRAN,DSTRAN,TIME,DTIME,TEMP,DTEMP,PREDEF,DPRED,CMNAME,
     & NDI,NSHR,NTENS,NSTATV,PROPS,NPROPS,COORDS,DROT,PNEWDT,
     & CELENT,DFGRD0,DFGRD1,NOEL,NPT,LAYER,KSPT,JSTEP,KINC)

!     Adapted from template file "umat.for" (plane stress), available from SIMULIA
!     COPYRIGHT (2012,2019) EVER J. BARBERO, ALL RIGHTS RESERVED

!     TRUNCATED MAXIMUM STRAIN (TMS) WITH MATRIX CUTOFF
!     [ref.] Section 7.3.2 in ISBN: 978-1-138-19680-3, CRC Press (2018)
!     Ex_3.13_TMS in ISBN: 987-1-4665-1661-8 (2013) 

      INCLUDE 'ABA_PARAM.INC'
      CHARACTER*80 CMNAME	!CMNAME<=MATERL in R10
      DIMENSION STRESS(NTENS),STATEV(NSTATV),
     & DDSDDE(NTENS,NTENS),DDSDDT(NTENS),DRPLDE(NTENS),
     & STRAN(NTENS),DSTRAN(NTENS),TIME(2),PREDEF(1),DPRED(1),
     & PROPS(NPROPS),COORDS(3),DROT(3,3),DFGRD0(3,3),DFGRD1(3,3),
     & JSTEP(4)
!
! -----------------------------------------------------------
!      UMAT FOR SHELL ELEMENTS S8R5, S4R, S3
! -----------------------------------------------------------
!      NDI: # of direct components (11,...) of DDSDDE, DDSDDT, and DRPLDE
!      NSHR: # of engineering shear components (12,...) of DDSDDE, DDSDDT, and DRPLDE
!      NTENS = NDI + NSHR: Size of the stress or strain component array
!      For solids: NTENS = 6
!      For plane stress/strain: NTENS = 5
!      STRAN : strain from previous increment
!      DSTRAN: increment of strain for current iteration
!      DDSDDE: stiffness matrix
!
!      PROPS(NPROPS): Array with material property data
!      NPROPS: # of material properties. In CAE > Property > User Material
!      NPROPS = 11 : 5 elastic properties + 6 strength values 
!        (redundant to be able to use MAXSTR and TSAIWU if we wish to program those)
!
!      STATEV(NSTATV): Array of state variables
!      NSTATEV: # of state variables
!      STATEV(1) : IF1 (fiber tensile failure index). Inverse of safety factor. 
!      STATEV(2) : IF2 (fiber compression failure index). Inverse of safety factor.  
!      STATEV(3) : IF3 (fiber shear failure index). Inverse of safety factor. 
!      STATEV(4) : IF4 (matrix cutoff index). Inverse of safety factor. 
!
!     RESPECT THIS ORDER WHEN YOU ENTER MATERIAL PROPERTIS IN CAE
      E1		= PROPS(1)      !modulus fiber direction
      E2		= PROPS(2)      !modulus transverse direction
      PR12	    = PROPS(3)      !Poisson's ratio 12
      G12       = PROPS(4)      !in-plane shear modulus
      G23       = PROPS(5)      !thru-thickness shear modulus
!
      F1T		= PROPS(6)	! Tensile strength fiber direction
      F1C		= PROPS(7)	! Compression strength fiber direction, positive value
      F2T		= PROPS(8)	! Transverse tensile strength
      F2C		= PROPS(9)	! Transverse compression strength, positive value
      F6		= PROPS(10)	! In-plane shear shtrength
      f12		= PROPS(11)	! Tsai-wu interaction coefficient 
!
      E3        = E2            !transversely isotropic lamina
      PR13      = PR12          !transversely isotropic lamina
      G13       = G12           !transversely isotropic lamina
      PR23	    = E2/(2*G23)-1  !transversely isotropic lamina
!
!     ELASTIC STIFFNESS
!
      DO 20 K1=1,NTENS
        DO 10 K2=1,NTENS
           DDSDDE(K2,K1)=0.0D0
 10     CONTINUE
 20   CONTINUE
!     PR21	= PR12*E2/E1
      IF (NDI.EQ.2) THEN
        DDSDDE(1,1)	= -1/(-E1+PR12**2.*E2)*E1**2.
	    DDSDDE(1,2)	= -PR12*E1/(-E1+PR12**2.*E2)*E2
        DDSDDE(2,1)	= DDSDDE(1,2)
        DDSDDE(2,2)	= -E1/(-E1+PR12**2.*E2)*E2
        DDSDDE(3,3)	= G12
        IF (NSHR.GT.1) THEN
          DDSDDE(4,4) = G13
          DDSDDE(5,5) = G23
        ENDIF
      ELSE
        WRITE (6,3)
      ENDIF
 3    FORMAT(1x,'ERROR-UMAT: ONLY PLANE STRESS IMPLEMENTED')
!
!     CALCULATE STRESS FROM ELASTIC STRAINS
!
      DO 70 K1=1,NTENS
        DO 60 K2=1,NTENS
           STRESS(K2)=STRESS(K2)+DDSDDE(K2,K1)*DSTRAN(K1)
 60     CONTINUE
 70   CONTINUE
!
!     Calculate strains to failure from strength values
!      
      stran = stran + dstran
      call tmsfc (stran, F1t/E1, F1c/E1, F2t/E2, PR12, statev)
!      
      RETURN
      END SUBROUTINE

      subroutine tmsfc (strain, xet, xec, yet, nu12, SDV)
    ! evaluates the failure index (FI) for truncated max. strain
    ! [ref.] Section 7.3.2 in ISBN: 978-1-138-19680-3, CRC Press (2018)

    ! NOTE THE ORDER 1...4 TO INTERPRET RESULTS IN CAE LATER
    ! SDV (same as STATEV): failure index = 1 / safety factor
    ! SDV(1) : IF1 (fiber tensile failure index). Inverse of safety factor. 
    ! SDV(2) : IF2 (fiber compression failure index). Inverse of safety factor.  
    ! SDV(3) : IF3 (fiber shear failure index). Inverse of safety factor. 
    ! SDV(4) : IF4 (matrix cutoff index). Inverse of safety factor. 

    ! strain : is the current strain
    ! trunc. max. strain does not consider interlaminar stresses/strains
    ! ht : hygro-thermal strains
    ! xet : fiber tensile strain to failure 
    ! xec : fiber compression strain to failure
    ! yet : lamina transverse tensile strain 
    
      implicit none
      double precision strain(5), xet, xec, yet, nu12
      double precision SDV(4)
      double precision s, tmp, ht(4)
      double precision, parameter :: zero=0.0D0

      ! hygro-thermal strains should be discounted from the ultimate values
      ht = zero        !but set them to zero for now
      SDV = zero       !initialize when calculating I_F (like Abaqus)
    
    ! fiber direction f.c.
        if ( strain(1).gt.zero.and.(xet-ht(1)).ne.zero )  SDV(1)= strain(1)/(xet-ht(1))  !fiber tension, when strain is positive
        if ( strain(1).lt.zero.and.(xec-ht(1)).ne.zero )  SDV(2)=-strain(1)/(xec+ht(1))  !fiber compression, when strain is negative

    ! fiber shear cut-off, it is not a matrix cut off, but part of fiber failure
        s = (1+nu12)*max((xet-ht(1)),(xec+ht(1)))
        tmp = dabs(strain(1)-strain(2))
        if( tmp.gt.zero.and.s.ne.zero ) SDV(3)=tmp/s                                     !fiber shear, on 2nd and 4th quadrants only

    ! matrix cut off on current layer
      if ( strain(2).gt.zero.and.(yet-ht(1)).ne.zero )  SDV(4)=strain(2)/(yet-ht(2))       !matrix failure, when the transverse strain is positive

      end subroutine
