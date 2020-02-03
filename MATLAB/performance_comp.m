%% importing the files
fid = fopen('C:\peter_abaqus\Summer-Research-Project\working_with_meep\parallel performance 2.log','r');
a = fread(fid,'double','ieee-le');
space_dim = [2, 6]; 
parallel2 = reshape(a, space_dim(1), space_dim(2));
fclose(fid);

fid = fopen('C:\peter_abaqus\Summer-Research-Project\working_with_meep\parallel performance 4.log','r');
a = fread(fid,'double','ieee-le');
space_dim = [2, 6]; 
parallel4 = reshape(a, space_dim(1), space_dim(2));
fclose(fid);

fid = fopen('C:\peter_abaqus\Summer-Research-Project\working_with_meep\parallel performance 6.log','r');
a = fread(fid,'double','ieee-le');
space_dim = [2, 6]; 
parallel6 = reshape(a, space_dim(1), space_dim(2));
fclose(fid);


fid = fopen('C:\peter_abaqus\Summer-Research-Project\working_with_meep\serial performance.log','r');
a = fread(fid,'double','ieee-le');
space_dim = [2, 6]; 
serial = reshape(a, space_dim(1), space_dim(2));
fclose(fid);

figure()
plot(serial(1,:), serial(2,:))
hold on
plot(parallel2(1,:), parallel2(2,:))
hold on
plot(parallel4(1,:), parallel4(2,:))
hold on
plot(parallel6(1,:), parallel6(2,:))
title('speed and efficiency of multi-core processing')
xlabel('number of cells division')
ylabel('execution time')
legend('core = 1', 'core = 2', 'core = 4', 'core = 6')

figure()
plot(serial(1,:), serial(2,:)./parallel2(2,:))
hold on
plot(serial(1,:), serial(2,:)./parallel4(2,:))
hold on
plot(serial(1,:), serial(2,:)./parallel6(2,:))
title('speed up ratio')
xlabel('number of cells division')
ylabel('ratio of speed up')
legend('core = 2', 'core = 4', 'core = 6')