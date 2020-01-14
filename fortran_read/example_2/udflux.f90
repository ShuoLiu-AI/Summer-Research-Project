! * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
!   Copyright by The HDF Group.                                               *
!   Copyright by the Board of Trustees of the University of Illinois.         *
!   All rights reserved.                                                      *
!                                                                             *
!   This file is part of HDF5.  The full HDF5 copyright notice, including     *
!   terms governing use, modification, and redistribution, is contained in    *
!   the COPYING file, which can be found at the root of the source code       *
!   distribution tree, or in https://support.hdfgroup.org/ftp/HDF5/releases.  *
!   If you do not have access to either file, you may request a copy from     *
!   help@hdfgroup.org.                                                        *
! * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
!
!
! The following example shows how to create an empty dataset.
! It creates a file called 'dsetf.h5', defines the
! dataset dataspace, creates a dataset which is a 4x6 integer array,
! and then closes the dataspace, the dataset, and the file.
!
! This example is used in the HDF5 Tutorial.

subroutine H5_CRTDAT

      USE HDF5 ! This module contains all necessary modules
    
      IMPLICIT NONE
    
      CHARACTER(LEN=8), PARAMETER :: filename = "dsetf.h5" ! File name
      CHARACTER(LEN=4), PARAMETER :: dsetname = "dset"     ! Dataset name
    
      INTEGER(HID_T) :: file_id       ! File identifier
      INTEGER(HID_T) :: dset_id       ! Dataset identifier
      INTEGER(HID_T) :: dspace_id     ! Dataspace identifier
    
    
      INTEGER(HSIZE_T), DIMENSION(2) :: dims = (/4,6/) ! Dataset dimensions
      INTEGER     ::   rank = 2                        ! Dataset rank
    
      INTEGER     ::   error ! Error flag
    
      CALL h5open_f(error)
      CALL h5fcreate_f(filename, H5F_ACC_TRUNC_F, file_id, error)
      CALL h5screate_simple_f(rank, dims, dspace_id, error)
      CALL h5dcreate_f(file_id, dsetname, H5T_NATIVE_INTEGER, dspace_id, &
           dset_id, error)
      CALL h5dclose_f(dset_id, error)
      CALL h5sclose_f(dspace_id, error)
      CALL h5fclose_f(file_id, error)
      CALL h5close_f(error)
    
END subroutine H5_CRTDAT
    
    

SUBROUTINE DFLUX(FLUX,SOL,JSTEP,JINC,TIME,NOEL,NPT,COORDS,JLTYP, TEMP,PRESS,SNAME)

      INCLUDE 'ABA_PARAM.INC'

      DIMENSION COORDS(3),FLUX(2),TIME(2)
      CHARACTER*80 SNAME
      
      call H5_CRTDAT
      FLUX(1)=-250.*SOL
      FLUX(2)=-250.
      ! write(*, 1000) COORDS(1), COORDS(2), COORDS(3)
      ! 1000 format (3(f5.2))
      RETURN
END

