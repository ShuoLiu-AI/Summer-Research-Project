
subroutine testrand
    REAL x, y
    integer numbin, numvar, graphlen, shrinkratio
    real binarea
    parameter (numbin = 30, numvar = 400, binarea = 6.0, graphlen = 20)
    
    real z(numvar)
    integer seed(1), bin(numbin), max
    real binbound(numbin)
    
    real :: pi = 3.1415926535485009
    
    character output(numbin, graphlen)
    
    seed(1) =  10
    CALL RANDOM_SEED(put=seed)
    
    do i = 1, numvar
        CALL RANDOM_NUMBER(x)
        call RANDOM_NUMBER(y)
        z(i) = sqrt(-2*log(x))*cos(2*pi*y)
    end do
    
    do i = 1,numbin
        binbound(i) = i*binarea/(numbin/2.0) - binarea/2.0
    end do
    
    print *, 'bin bound'
    print*, binbound
    
    DO i = 1, numvar
        if (z(i) > binbound(end)) then
            binbound(end)=binbound(end) + 1
        end if
        
      do j = 1, numbin
          if (z(i) < binbound(j)) then
                bin(j) = bin(j) + 1
                exit
          end if
      end do
    END DO
    
    max = maxval(bin)
    shrinkratio = ceiling(real(max)/consolelen)
    
    print*, shrinkratio
    print*, bin
       
    
    do i = 1, numbin
        do j = 1, bin(i)
            write(*,fmt="(A)", advance='no') '*'
        end do
        write(*,*)
    end do
    
    !print*, 'array'
    !print *, z
end subroutine testrand
    

    
    subroutine write_conv

    USE HDF5 ! This module contains all necessary modules

    IMPLICIT NONE

    !CHARACTER(LEN=8), PARAMETER :: filename = "eps.h5" ! File name
    !character(len=10), parameter :: out_name = "out.peter"
    !CHARACTER(LEN=4), PARAMETER :: dsetname = "eps"     ! Dataset name

    CHARACTER(LEN=20), PARAMETER :: filename = "eps_small.h5" ! File name
    character(len=20), parameter :: out_name = "out_small.peter"
    CHARACTER(LEN=4), PARAMETER :: dsetname = "ez"     ! Dataset name
    
    INTEGER(HID_T) :: in_id, out_id       ! File identifier
    INTEGER(HID_T) :: dset_id       ! Dataset identifier
    INTEGER(HID_T) :: dspace_id     ! Dataspace identifier

    INTEGER     ::   error ! Error flag
    INTEGER     ::  i, j

    integer, parameter :: m = 100
    integer, parameter :: n = 100
    integer, parameter :: l = 100
    integer, parameter :: sizeofreal=8
    
    DOUBLE PRECISION, dimension(100, 100, 100, 33):: data_out ! Data buffers
    integer(HSIZE_T), dimension(4)::dims = (/100, 100, 100,33/)

    INTEGER     ::   rank = 4                       ! Dataset rank

    CALL h5open_f(error)
    
    open(1, file = out_name, status = 'new', access='direct', recl=100*100*100*33*2) 
    call h5fopen_f(filename, H5F_ACC_RDONLY_F, in_id, error)
    
    
    CALL h5screate_simple_f(rank, dims, dspace_id, error)
    
    CALL h5dopen_f(in_id, dsetname, dset_id, error)
    
    CALL h5dread_f(dset_id, H5T_NATIVE_DOUBLE, data_out, dims, error)
    
    
    print*, 'after read'

    CALL h5sclose_f(dspace_id, error)
    CALL h5dclose_f(dset_id, error)

    !write (1) (((data_out(i,j,k), i=1,100), j=1,100), k=1,100)
    write(1, rec=1), data_out
    close(1)
    CALL h5fclose_f(in_id, error)

CALL h5close_f(error)

END subroutine write_conv

subroutine write_conv1

    USE HDF5 ! This module contains all necessary modules

    IMPLICIT NONE

    !CHARACTER(LEN=8), PARAMETER :: filename = "eps.h5" ! File name
    !character(len=10), parameter :: out_name = "out.peter"
    !CHARACTER(LEN=4), PARAMETER :: dsetname = "eps"     ! Dataset name

    CHARACTER(LEN=20), PARAMETER :: filename = "eps_small.h5" ! File name
    character(len=20), parameter :: out_name = "eps_small.peter"
    CHARACTER(LEN=4), PARAMETER :: dsetname = "eps"     ! Dataset name
    
    INTEGER(HID_T) :: in_id, out_id       ! File identifier
    INTEGER(HID_T) :: dset_id       ! Dataset identifier
    INTEGER(HID_T) :: dspace_id     ! Dataspace identifier

    INTEGER     ::   error ! Error flag
    INTEGER     ::  i, j

    integer, parameter :: m = 100
    integer, parameter :: n = 100
    integer, parameter :: l = 100
    integer, parameter :: sizeofreal=8
    
    DOUBLE PRECISION, dimension(100, 100, 100):: data_out ! Data buffers
    integer(HSIZE_T), dimension(3)::dims = (/100, 100, 100/)

    INTEGER     ::   rank = 3                       ! Dataset rank

    CALL h5open_f(error)
    
    open(1, file = out_name, status = 'new', access='direct', recl=100*100*100*2) 
    call h5fopen_f(filename, H5F_ACC_RDONLY_F, in_id, error)
    
    
    CALL h5screate_simple_f(rank, dims, dspace_id, error)
    
    CALL h5dopen_f(in_id, dsetname, dset_id, error)
    
    CALL h5dread_f(dset_id, H5T_NATIVE_DOUBLE, data_out, dims, error)
    
    
    print*, 'after read'

    CALL h5sclose_f(dspace_id, error)
    CALL h5dclose_f(dset_id, error)

    !write (1) (((data_out(i,j,k), i=1,100), j=1,100), k=1,100)
    write(1, rec=1), data_out
    close(1)
    CALL h5fclose_f(in_id, error)

CALL h5close_f(error)

END subroutine write_conv1
    
subroutine read_conv

      integer m,n,l
      parameter (m=100, n=100, l =100)
      double precision x(100, 100, 20)


      open (unit=1,  file='out.peter', form='unformatted',  access='direct', recl=100*100*20*2)



    read (1, rec=2) x
    print*, x

    end subroutine
    
    
subroutine write10

      integer m,n
      parameter (m=8, n=8)
      double precision x(m, n)

    do i = 1,m
        do j = 1,n
            x(i,j) = (i-1)*5+j-1
        end do
    end do
    
      open (unit=1,  file='out5.peter', form='unformatted',  access='direct', recl=m*n*2)


    write (1, rec=1) x
    close(1)
    do i = 1,m
        print*, x(i, :)
    end do

end subroutine
    
subroutine read10

      integer m,n
      parameter (m=8, n=4)
      double precision x(m, n)
    
      open (unit=2,  file='out5.peter', form='unformatted',  access='direct', recl=m*n*2)


    read (2, rec=2) x
    close(2)
    print*, 'read'
    do i = 1,8
        print*, x(i, :)
    end do

end subroutine
