SUBROUTINE DFLUX(FLUX,SOL,JSTEP,JINC,TIME,NOEL,NPT,COORDS,JLTYP, TEMP,PRESS,SNAME)

      USE HDF5 ! This module contains all necessary modules

      ! INCLUDE 'ABA_PARAM.INC'

      DIMENSION COORDS(3),FLUX(2),TIME(2)
      CHARACTER*80 SNAME

      
    
    
      CHARACTER(LEN=8), PARAMETER :: filename = "dsetf.h5" ! File name
      CHARACTER(LEN=4), PARAMETER :: dsetname = "dset"     ! Dataset name
      
      INTEGER(HID_T) :: file_id       ! File identifier
      INTEGER(HID_T) :: dset_id       ! Dataset identifier
      INTEGER(HID_T) :: dspace_id     ! Dataspace identifier
    
      INTEGER     ::   error ! Error flag
      INTEGER     ::  i, j
    
      DOUBLE PRECISION, dimension(4, 6):: data_out ! Data buffers
      DOUBLE PRECISIOn, dimension(4, 6):: dset_data
      integer(HSIZE_T), dimension(2)::data_dims = (/4,6/)
      integer(HSIZE_T), dimension(2)::dims = (/4,6/)
    
      INTEGER     ::   rank = 2                        ! Dataset rank
    

      ! DO i = 1, 4
      !    DO j = 1, 6
      !       dset_data(i,j) = (i-1.0)*6.0 + j
      !    END DO
      ! END DO
    
      ! do i = 1,4
      !   print*, dset_data(i,:)
      ! end do

      FLUX(1)=-250.*SOL
      FLUX(2)=-250.

      CALL h5open_f(error)
      ! CALL h5fcreate_f(filename, H5F_ACC_TRUNC_F, file_id, error)
      ! CALL h5screate_simple_f(rank, dims, dspace_id, error)
      ! CALL h5dcreate_f(file_id, dsetname, H5T_NATIVE_DOUBLE, dspace_id, &
      !   dset_id, error)
      ! CALL h5dwrite_f(dset_id, H5T_NATIVE_DOUBLE, dset_data, data_dims, error)
      ! CALL h5dread_f(dset_id, H5T_NATIVE_DOUBLE, data_out, dims, error)
      ! print*, 'after read'
      ! do i = 1,4
      !   print*, data_out(i,:)
      ! end do
      ! CALL h5sclose_f(dspace_id, error)
      ! CALL h5dclose_f(dset_id, error)

      ! CALL h5fclose_f(file_id, error)
      
      CALL h5close_f(error)

      RETURN
END

