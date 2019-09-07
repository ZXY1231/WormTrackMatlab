%{
a =[1,0,0,1];
b = [0,1,1,0];
ball = [0,1,0;1,0,1;0,1,0]
balllinearindex = {2,4,6,8}
img = imread('sphere.tif');
CC = bwconncomp(img,8)
centroids = cellfun(@LocateWormCentre,CC.PixelIdxList)
[x,y] = ind2sub([3,3],centroids)
%centroids = regionprops(ball,'centroid');
%centroids.Centroid;
%LocateWormCentre(balllinearindex)
mod(1059203.2170999998,976)
%}
a = [1,2,3;1,2,3]
sum(a)
sum(a')