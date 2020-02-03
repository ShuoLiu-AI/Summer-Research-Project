%% importing the files
fid = fopen('C:\peter_abaqus\Summer-Research-Project\fortran_read\out_small.peter','r');
a = fread(fid,'double','ieee-le');
space_dim = [100, 100, 100];
a = reshape(a, space_dim(1), space_dim(2), space_dim(3), length(a)/(space_dim(1)*space_dim(2)*space_dim(3)));
fclose(fid);

%% importing the files
fid = fopen('C:\peter_abaqus\Summer-Research-Project\working_with_meep\ez_straight_waveg.bin','r');
a = fread(fid,'double','ieee-le');
space_dim = [201, 160, 80]; 
a = reshape(a, space_dim(1), space_dim(2), space_dim(3), length(a)/(space_dim(1)*space_dim(2)*space_dim(3)));
fclose(fid);
imshow(rescale(squeeze(a(1,:,:))))


%% importing the files
fid = fopen('C:\peter_abaqus\Summer-Research-Project\working_with_meep\tese_res_50.bin','r');
whole_field = fread(fid,'double','ieee-le');
fclose(fid);

% fid = fopen('C:\peter_abaqus\Summer-Research-Project\working_with_meep\one_cube_3d.bin','r');
% whole_field_2 = fread(fid,'double','ieee-le');
% fclose(fid);

% whole_field = whole_field -  whole_field_2;

space_dim = [33, 100, 100, 100];

if length(space_dim) == 3
    whole_field = reshape(whole_field, space_dim(1), space_dim(2), length(whole_field)/(space_dim(1)*space_dim(2)));
elseif length(space_dim) == 4 
    whole_field = reshape(whole_field, space_dim(1), space_dim(2), space_dim(3), length(whole_field)/(space_dim(1)*space_dim(2)*space_dim(3)));
elseif length(space_dim) == 5
    whole_field = reshape(whole_field, space_dim(1), space_dim(2), space_dim(3),space_dim(4), length(whole_field)/(space_dim(1)*space_dim(2)*space_dim(3)*space_dim(4)));
end

% imshow(rescale(squeeze(whole_field(1,1,:,:))))

%% export the file 

%% plotting options
plot_coutour=1;

%% plot iso-surface

b = a(:,:,:,1);
M = mean( b , 'all' );
isosurface(b, M)


%% plotting the time serie values
figure()
part_field = squeeze(whole_field(:, :, :, 50));

Q = size(part_field, 1);
W = squeeze(part_field(1,:,:));
h = pcolor(W);
h.FaceColor = 'interp';
set(h, 'EdgeColor', 'none');
drawnow();
pause(0.3);
for K = 2 : Q
    W = squeeze(part_field(K,:,:));
    set(h, 'CData', W);
    drawnow();
    pause(0.3);
end

%% plotting slice 3D scalar field output

figure()

plot_limit = 15:85;

if length(size(whole_field)) == 4
    plot_whole_field = whole_field;
    plot_whole_field = plot_whole_field(:, plot_limit, plot_limit, plot_limit);
    Q = size(plot_whole_field, 1);
    time_slice = squeeze(plot_whole_field(1,:,:,:));
elseif length(size(whole_field)) == 5
    plot_whole_field = squeeze(whole_field(1, :, :,:,:));
    plot_whole_field = plot_whole_field(:, plot_limit, plot_limit, plot_limit);
    Q = size(plot_whole_field, 1);
    time_slice = squeeze(plot_whole_field(1,:,:,:));
end

h = slice(rid_val(time_slice), [], 1:size(time_slice,3), []);
xlabel('x')
ylabel('y')
zlabel('z')
alpha(.1)
set(h, 'EdgeColor', 'none');
%set(h , 'FaceColor','interp');
drawnow();
pause(0.3);
for K = 2 : 33
    time_slice = rid_val(squeeze(plot_whole_field(K, :, :, :)));
    title(K)
    for J = 1:length(h)
        set(h(J), 'CData', squeeze(time_slice( J, :, :)));
    end
    drawnow();
    pause(0.6);
end

function out_arr = rid_val(in_arr)
    out_arr = in_arr;
    arr_abs = abs(in_arr);
    arr_mean = mean(mean(mean(arr_abs)));
    out_arr(arr_abs < (arr_mean))=nan;
end