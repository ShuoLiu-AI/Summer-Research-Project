%% importing the files

for i = 1:10
    dir = 'C:\peter_abaqus\Summer-Research-Project\meep\meep_out\';
    dist = (i-1)/10;
    name = strcat('cube_dis_', sprintf('%.1f',dist), '.bin');

    fid = fopen(strcat(dir, name, '.meta'),'r');
    space_dim = fread(fid,'double','ieee-le');
    fclose(fid);

    fid = fopen(strcat(dir, name),'r');
    whole_field = fread(fid,'double','ieee-le');
    fclose(fid);

    % fid = fopen('C:\peter_abaqus\Summer-Research-Project\working_with_meep\one_cube_3d.bin','r');
    % whole_field_2 = fread(fid,'double','ieee-le');
    % fclose(fid);

    % whole_field = whole_field -  whole_field_2;

    if length(space_dim) == 3
        whole_field = reshape(whole_field, space_dim(1), space_dim(2), length(whole_field)/(space_dim(1)*space_dim(2)));
    elseif length(space_dim) == 4 
        whole_field = reshape(whole_field, space_dim(1), space_dim(2), space_dim(3), length(whole_field)/(space_dim(1)*space_dim(2)*space_dim(3)));
    elseif length(space_dim) == 5
        whole_field = reshape(whole_field, space_dim(1), space_dim(2), space_dim(3),space_dim(4), length(whole_field)/(space_dim(1)*space_dim(2)*space_dim(3)*space_dim(4)));
    end
    arr_whole_field_rms(i, :, :, :) = squeeze(rms(whole_field));
end
% imshow(rescale(squeeze(whole_field(1,1,:,:))))

%% 
cube_size = 0.5;
cell_size = [2, 2, 2];

cube_points = [[-1, -1, -1]; [-1, -1, 1]; [-1, 1, -1]; [-1, 1, 1]; [1, -1, -1]; [1, -1, 1]; [1, 1, -1]; [1, 1, 1]];
%normalize the cube points to 1
cube_points = cube_size/cell_size(1) * cube_points;

s = num2cell([2, size(cube_points)]);
cubes = zeros(s{:});

range = space_dim(2);
roi = [0.1, 0.9];
len_roi = roi(2) - roi(1);
trans_roi = @(point, len_roi) ((point./cell_size + 1/2)/len_roi - (1/len_roi - 1)/2)*range*len_roi + 2;

plot_limit = roi(1)*range:roi(2)*range;

for j = 1:6
    subplot(2,3, j)
    dist = (j-1)/10;
    plot_whole_field_rms = squeeze(arr_whole_field_rms(j, plot_limit, plot_limit, plot_limit));
    
    cubes(1, :, :) = move_poly(cube_points, [-dist/2 - cube_size/2, 0, 0]);
    cubes(2, :, :) = move_poly(cube_points, [dist/2 + cube_size/2, 0, 0]);
    
    pc = pcolor(squeeze(plot_whole_field_rms(1:34, :, range/2)));
    hold on
    set(pc, 'EdgeColor', 'none');
    for i  = 1:size(cubes, 1)
        cube = squeeze(cubes(i, :, :));
        [k1,av1] = convhull(cube);
        for k = 1:length(k1)
            p = cube([int32(k1(k,:)), int32(k1(k, 1))], :);
            plot(trans_roi(p(:, 1), len_roi), trans_roi(p(:, 2), len_roi), 'r-')
            hold on
        end
    end
    title('RMS EM field strength')
    colorbar
end

    
