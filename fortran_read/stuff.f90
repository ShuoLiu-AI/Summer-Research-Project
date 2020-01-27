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


subroutine working

  USE HDF5 ! This module contains all necessary modules

  IMPLICIT NONE

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
  
  !
  ! Initialize the dset_data array.
  !
  DO i = 1, 4
     DO j = 1, 6
        dset_data(i,j) = (i-1.0)*6.0 + j
     END DO
  END DO
  
  do i = 1,4
    print*, dset_data(i,:)
  end do
  
  ! Initialize FORTRAN interface.
  !
  CALL h5open_f(error)
  !
  !CALL h5fcreate_f(filename, H5F_ACC_TRUNC_F, file_id, error)
  !
  !CALL h5screate_simple_f(rank, dims, dspace_id, error)
  !
  !CALL h5dcreate_f(file_id, dsetname, H5T_NATIVE_DOUBLE, dspace_id, &
  !  dset_id, error)
  !
  !CALL h5dwrite_f(dset_id, H5T_NATIVE_DOUBLE, dset_data, data_dims, error)
  !
  !
  !
  !!print*, 'before read'
  !!print*, data_out
  !
  !!get the slice of the matrix to output 
  !!call h5sselect_hyperslab_f(dspace_id, H5S_SELECT_SET_F, offset, dims, error, stride, bloc)
  !
  !CALL h5dread_f(dset_id, H5T_NATIVE_DOUBLE, data_out, dims, error)
  !print*, 'after read'
  !do i = 1,4
  !  print*, data_out(i,:)
  !end do
  !
  !CALL h5sclose_f(dspace_id, error)
  !CALL h5dclose_f(dset_id, error)
  !
  !CALL h5fclose_f(file_id, error)
  !
  !CALL h5close_f(error)

END subroutine working
!
!subroutine wr_rd_data
!
!  USE HDF5 ! This module contains all necessary modules
!
!  IMPLICIT NONE
!
!  !CHARACTER(LEN=8), PARAMETER :: filename = "ez.h5" ! File name
!  CHARACTER(LEN=4), PARAMETER :: dsetname = "ez"     ! Dataset name
!  character(len=40), parameter :: filename = "D:\source\working_with_meep\ez.h5"
!
!  INTEGER(HID_T) :: file_id       ! File identifier
!  INTEGER(HID_T) :: dset_id       ! Dataset identifier
!
!  INTEGER     ::   error ! Error flag
!  INTEGER     ::  i, j
!
!  double precision, DIMENSION(100,100) ::  data_out ! Data buffers
!
!  INTEGER(HSIZE_T), DIMENSION(4) :: data_dims
!  integer(HSIZE_T), dimension(2):: out_dims
!  integer(HSIZE_T), dimension(4)::start, count
!
!  integer::rank_2, rank_4
!  
!  integer(HID_T):: out_space_id, file_space_id
!  
!  rank_2 = 2
!  rank_4 = 4
!  
!  out_dims = (/100,100/)
!  data_dims = (/100, 100, 100, 834/)
!  
!  call h5screate_simple_f(rank_2, out_dims, out_space_id, error)
!  call h5screate_simple_f(rank_4, data_dims, file_space_id, error)
!  
!  
!  !
!  ! Initialize the dset_data array.
!  !
!  !DO i = 1, 4
!  !   DO j = 1, 6
!  !      dset_data(i,j) = (i-1)*6 + j
!  !   END DO
!  !END DO
!
!  !
!  ! Initialize FORTRAN interface.
!  !
!  CALL h5open_f(error)
!
!  !
!  ! Open an existing file.
!  !
!  CALL h5fopen_f (filename, H5F_ACC_RDWR_F, file_id, error)
!
!  !
!  ! Open an existing dataset.
!  !
!  CALL h5dopen_f(file_id, dsetname, dset_id, error)
!
!  !create a dataset
!  !
!  ! Write the dataset.
!  !
!
!  !CALL h5dwrite_f(dset_id, H5T_NATIVE_INTEGER, dset_data, data_dims, error)
!
!  !
!  ! Read the dataset.
!  !
!  
!  start = (/0,0,0,0/)
!  count = (/100,1,100,1/)
!  
!  call h5sselect_hyperslab_f(file_space_id, h5s_select_set_f, start, count, error)
!  
!  CALL h5dread_f(dset_id, H5T_IEEE_F64LE, data_out, out_dims, error, out_space_id, file_space_id)
!   ! CALL h5dread_f(dset_id, H5T_NATIVE_INTEGER, data_out, data_dims, error)
!    
!    do i = 1,out_dims(1)
!        print*, data_out(i,:)
!    end do
!  !
!  ! Close the dataset.
!  !
!  CALL h5dclose_f(dset_id, error)
!
!  !
!  ! Close the file.
!  !
!  CALL h5fclose_f(file_id, error)
!
!  !
!  ! Close FORTRAN interface.
!  !
!  CALL h5close_f(error)
!end subroutine 
!subroutine wr_rd_data_eps
!
!  USE HDF5 ! This module contains all necessary modules
!
!  IMPLICIT NONE
!
!  CHARACTER(LEN=8), PARAMETER :: filename = "ez.h5" ! File name
!  CHARACTER(LEN=4), PARAMETER :: dsetname = "eps"     ! Dataset name
!  !character(len=40), parameter :: meep_output_fname = "D:\source\working_with_meep\ez.h5"
!  character(len=100), parameter :: meep_output_fname = "D:\source\working_with_meep\eps-000010.21.h5"
!
!  INTEGER(HID_T) :: file_id       ! File identifier
!  INTEGER(HID_T) :: dset_id       ! Dataset identifier
!
!  INTEGER     ::   error ! Error flag
!  INTEGER     ::  i, j
!
!  double precision, DIMENSION(100,100) ::  data_out ! Data buffers
!
!  INTEGER(HSIZE_T), DIMENSION(3) :: data_dims
!  integer(HSIZE_T), dimension(2):: out_dims
!  integer(HSIZE_T), dimension(3)::start, count
!
!  integer::rank_2, rank_3
!  
!  integer(HID_T):: out_space_id, file_space_id
!  
!  rank_2 = 2
!  rank_3 = 3
!  
!  out_dims = (/100,100/)
!  data_dims = (/100, 100, 100/)
!  
!  call h5screate_simple_f(rank_2, out_dims, out_space_id, error)
!  call h5screate_simple_f(rank_3, data_dims, file_space_id, error)
!  
!  
!  !
!  ! Initialize the dset_data array.
!  !
!  !DO i = 1, 4
!  !   DO j = 1, 6
!  !      dset_data(i,j) = (i-1)*6 + j
!  !   END DO
!  !END DO
!
!  !
!  ! Initialize FORTRAN interface.
!  !
!  CALL h5open_f(error)
!
!  !
!  ! Open an existing file.
!  !
!  CALL h5fopen_f (meep_output_fname, H5F_ACC_RDWR_F, file_id, error)
!
!  !
!  ! Open an existing dataset.
!  !
!  CALL h5dopen_f(file_id, dsetname, dset_id, error)
!
!  !create a dataset
!  !
!  ! Write the dataset.
!  !
!
!  !CALL h5dwrite_f(dset_id, H5T_NATIVE_INTEGER, dset_data, data_dims, error)
!
!  !
!  ! Read the dataset.
!  !
!  
!  start = (/0,0,53/)
!  count = (/100,100,1/)
!  
!  call h5sselect_hyperslab_f(file_space_id, h5s_select_set_f, start, count, error)
!  
!  CALL h5dread_f(dset_id, H5T_NATIVE_DOUBLE, data_out, out_dims, error, out_space_id, file_space_id)
!   ! CALL h5dread_f(dset_id, H5T_NATIVE_INTEGER, data_out, data_dims, error)
!    
!    do i = 1,out_dims(1)
!        print*, data_out(i,:)
!    end do
!  !
!  ! Close the dataset.
!  !
!  CALL h5dclose_f(dset_id, error)
!
!  !
!  ! Close the file.
!  !
!  CALL h5fclose_f(file_id, error)
!
!  !
!  ! Close FORTRAN interface.
!  !
!  CALL h5close_f(error)
!end subroutine 
!subroutine offset_data
!
!  USE HDF5 ! This module contains all necessary modules 
!
!  IMPLICIT NONE
!
!  CHARACTER(LEN=9), PARAMETER :: filename = "subset.h5"  ! File name
!  CHARACTER(LEN=8), PARAMETER :: dsetname = "IntArray"   ! Dataset name
!
!  INTEGER(HID_T) :: file_id       ! File identifier 
!  INTEGER(HID_T) :: dset_id       ! Dataset identifier 
!  INTEGER(HID_T) :: dataspace     ! Dataspace identifier 
!  INTEGER(HID_T) :: memspace      ! memspace identifier 
!
!  !
!  ! To change the subset size, modify size of dimsm, sdata, dim0_sub,
!  ! dim1_sub, and count
!  !
!  INTEGER(HSIZE_T), DIMENSION(1:2) :: dimsm = (/4,3/) ! Dataset dimensions
!  INTEGER, DIMENSION(1:4,1:3) :: sdata                  ! Subset buffer
!  INTEGER :: dim0_sub = 4   
!  INTEGER :: dim1_sub = 3 
!  INTEGER(HSIZE_T), DIMENSION(1:2) :: count = (/4,3/)  ! Size of hyperslab
!  INTEGER(HSIZE_T), DIMENSION(1:2) :: offset = (/2,1/) ! Hyperslab offset
!  INTEGER(HSIZE_T), DIMENSION(1:2) :: stride = (/1,1/) ! Hyperslab stride 
!  INTEGER(HSIZE_T), DIMENSION(1:2) :: block = (/1,1/)  ! Hyperslab block size 
!
!  INTEGER(HSIZE_T), DIMENSION(1:2) :: dimsf = (/10,8/) ! Dataset dimensions
!
!
!  INTEGER, DIMENSION(1:10,1:8) :: data     ! Data to write
!  INTEGER, DIMENSION(1:10,1:8) :: rdata    ! Data to read 
!
!  INTEGER :: rank = 2      ! Dataset rank ( in file )
!  INTEGER :: dim0 = 10     ! Dataset size in file
!  INTEGER :: dim1 = 8 
!
!  INTEGER :: i, j 
!
!  INTEGER :: error         ! Error flag
!  INTEGER(HSIZE_T), DIMENSION(2) :: data_dims
!
!  !
!  ! Write data to the HDF5 file.  
!  !
!
!  !
!  ! Data initialization. 
!  !
!  DO i = 1, dim0 
!     DO j = 1, dim1
!        IF (i .LE. (dim0 / 2)) THEN
!           data(i,j) = 1 
!        ELSE 
!           data(i,j) = 2 
!        END IF
!     END DO
!  END DO
!
!  !
!  ! Initialize FORTRAN interface. 
!  !
!  CALL h5open_f(error) 
!
!  !
!  ! Create a new file using default properties.
!  ! 
!  CALL h5fcreate_f(filename, H5F_ACC_TRUNC_F, file_id, error)
!
!  !
!  ! Create the data space for the  dataset. 
!  !
!  CALL h5screate_simple_f(rank, dimsf, dataspace, error)
!
!  !
!  ! Create the dataset with default properties.
!  !
!  CALL h5dcreate_f(file_id, dsetname, H5T_NATIVE_INTEGER, dataspace, &
!       dset_id, error)
!
!  !
!  ! Write the dataset.
!  !
!  data_dims(1) = dim0 
!  data_dims(2) = dim1 
!  CALL h5dwrite_f(dset_id, H5T_NATIVE_INTEGER, data, data_dims, error)
!
!  !
!  ! Data Written to File 
!  !
!  WRITE(*,'(/,A)') "Original Data Written to File:"
!  DO i = 1, dim0
!     WRITE(*,'(100(1X,I0,1X))') DATA(i,1:dim1)
!  END DO
!
!  !
!  !
!  ! Close the dataspace, dataset, and file.
!  !
!  CALL h5sclose_f(dataspace, error)
!  CALL h5dclose_f(dset_id, error)
!  CALL h5fclose_f(file_id, error)
!
!  !
!  ! Initialize subset data array.
!  !
!  sdata(1:dim0_sub,1:dim1_sub) = 5
!
!  !
!  ! Open the file.
!  !
!  CALL h5fopen_f(filename, H5F_ACC_RDWR_F, file_id, error)
!
!  !
!  ! Open the  dataset.
!  !
!  CALL h5dopen_f(file_id, dsetname, dset_id, error)
!
!  !
!  ! Get dataset's dataspace identifier and select subset.
!  !
!  CALL h5dget_space_f(dset_id, dataspace, error)
!  CALL h5sselect_hyperslab_f(dataspace, H5S_SELECT_SET_F, &
!       offset, count, error, stride, BLOCK) 
!  !
!  ! Create memory dataspace.
!  !
!  CALL h5screate_simple_f(rank, dimsm, memspace, error)
!
!  WRITE(*,'(/,A)') "Write subset to file specifying:"
!  WRITE(*,'(A,/)') "   offset=2x1 stride=1x1 count=4x3 block=1x1"
!
!  !
!  ! Write subset to dataset  
!  !
!  data_dims(1:2) = (/dim0_sub, dim1_sub/) 
!  CALL h5dwrite_f(dset_id, H5T_NATIVE_INTEGER, sdata, data_dims, error, &
!       memspace, dataspace)
!
!  data_dims(1:2) = (/dim0, dim1/)
!  CALL h5dread_f(dset_id, H5T_NATIVE_INTEGER, rdata, data_dims, error)
!
!  !
!  ! Read entire dataset back 
!  !
!  WRITE(*,'(A)') "Data in File after Subset Written:"
!  DO i = 1, dim0 
!    WRITE(*,'(100(1X,I0,1X))') rdata(i,1:dim1)
!  END DO
!  PRINT *, " "
!
!  !
!  ! Close everything opened.
!  !
!  CALL h5sclose_f(dataspace, error)
!  CALL h5sclose_f(memspace, error)
!  CALL h5dclose_f(dset_id, error)
!  CALL h5fclose_f(file_id, error)
!
!  !
!  ! Close FORTRAN interface.
!  !
!  CALL h5close_f(error)
!
!
!end subroutine 