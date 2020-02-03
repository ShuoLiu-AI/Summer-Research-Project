P = [0 0 0; 1 1 2; 1.5 0.5 1; 1.5 -0.5 3; 1.25 0.3 -1; 1 0 2; 1.25 -0.3 -1; 1 -1 3];
[k,av] = convhull(P);
x = P(:,1);
y = P(:,2);
z = P(:,3);

trisurf(k,x,y,z,'FaceColor','cyan')

csvwrite('polygon1.csv',P)
csvwrite('polygon1-hull.csv',k)
