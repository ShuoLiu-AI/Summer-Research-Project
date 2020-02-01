	      SUBROUTINE UMAT(STRESS,STATEV,DDSDDE,SSE,SPD,SCD,&
     & RPL,DDSDDT,DRPLDE,DRPLDT,&
     & STRAN,DSTRAN,TIME,DTIME,TEMP,DTEMP,PREDEF,DPRED,CMNAME,&
     & NDI,NSHR,NTENS,NSTATV,PROPS,NPROPS,COORDS,DROT,PNEWDT,&
     & CELENT,DFGRD0,DFGRD1,NOEL,NPT,LAYER,KSPT,JSTEP,KINC)

!     COPYRIGHT (2012) EVER J. BARBERO, ALL RIGHTS RESERVED
!     Ex. 3.13 Finite Element Analysis of Composite Materials with Abaqus

      INCLUDE 'ABA_PARAM.INC'
      PARAMETER (EPS=2.22D-16) !SMALLEST NUMBER REAL*8 CAN STORE
!
      CHARACTER*80 CMNAME	!CMNAME<=MATERL in R10
      DIMENSION STRESS(NTENS),STATEV(NSTATV),&
     & DDSDDE(NTENS,NTENS),DDSDDT(NTENS),DRPLDE(NTENS),&
     & STRAN(NTENS),DSTRAN(NTENS),TIME(2),PREDEF(1),DPRED(1),&
     & PROPS(NPROPS),COORDS(3),DROT(3,3),DFGRD0(3,3),DFGRD1(3,3),&
     & JSTEP(4)
!
!      A = 1.
!      EPS   = EPSILON(A)        !NEGLIGIBLE COMPARED TO 1.0, SAME TYPE AS A
!      TINY2 = TINY(A)           !SMALLEST NUMBER OF SAME TYPE AS A
!      HUGE2 = HUGE(A)           !LARGEST NUMBER OF SAME TYPE AS A
! -----------------------------------------------------------
!     UMAT FOR SHELL ELEMENTS S8R5
!     F77 IMPLICIT NAME CONVENTION
! -----------------------------------------------------------
!      NDI: # of direct components (11,...) of DDSDDE, DDSDDT, and DRPLDE
!      NSHR: # of engineering shear components (12,...) of DDSDDE, DDSDDT, and DRPLDE
!      NTENS = NDI + NSHR: Size of the stress or strain component array
! -----------------------------------------------------------
!
      E1		= PROPS(1)
      E2		= PROPS(2)
      E3        = E2
      PR12	    = PROPS(3)
      PR13      = PR12
      PR23	    = PROPS(4)	
      G12       = PROPS(5)
      G13       = G12
      G23       = E2/2/(1.+PR23)
!
      F1T		= PROPS(6)	! Strength 1 tension
      F1C		= PROPS(7)	! Strength 1 compresion positive value
      F2T		= PROPS(8)	! Strength 2 tension
      F2C		= PROPS(9)	! Strength 2 compresion positive value
      F6		= PROPS(10)	! Strength 12 shear
      F12		= PROPS(11)	! Tsai-wu interaction coefficient 
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
!     TSAI-WU FAILURE criterion 
!
      S_1	= STRESS(1)
      S_2	= STRESS(2)
      S_6	= STRESS(3) !PLANE STRESS

      A	= S_1**2./(F1T*F1C)+S_2**2./(F2T*F2C)+&
     &    S_6**2./(F6)**2+ F12*S_1*S_2/SQRT(F1T*F1C*F2T*F2C)

      B	= (1./F1T-1/F1C)*S_1 + (1./F2T-1/F2C)*S_2

      R = HUGE(R)
      IF (A.GT.EPS) R = -B/2./A + SQRT((B/2./A)**2.+1./A)

      F_I	= 1/R
!
!     STORE FAILURE INDEX AND STRENGTH RATIO IN STATE VARIABLE ARRAY 
!
      STATEV(1) = F_I
      STATEV(2) = R
!
      RETURN
      END