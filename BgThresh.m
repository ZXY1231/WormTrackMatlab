function [imgx,imgy] = BgThresh(img)
%img = imread('/Users/apple/Desktop/IGEM/post/tracking/WormTrack/contrastAdjusted.tif');
%img = img(600:end-600,600:end-600);
%max(img)
%min(img)
%imgbw = imbinarize(img,0.2);
%imgbw = rangefilt(img);
imgbwthresh = imbinarize(img,0.2);
%imgbw = multithresh(img,2);
%max(imgbw)
%min(imgbw)
%size(img)
%figure(1)
%imshow(imgbw)
%figure(2)
%imshow(imgbwthresh)
%surf(img)

imgremovesmall = bwareaopen(imgbwthresh,100);%remove regions with less than 100 pixels
imgremoved = RemoveBigArea(imgremovesmall,600);%remove regions with more than 600 pixels
CC = bwconncomp(imgremoved,8);%default is 8,16, 28  are also OK
%centroids = CC.PixelIdxList;
%centroids = cellfun(@numel,CC.PixelIdxList)
%max(centroids)
%min(centroids)
%[biggest,idx] = max(centroids)
numel(CC.PixelIdxList);
%CC.PixelIdxList{idx};%cellµÄÓÃ·¨is {}
centroids = cellfun(@LocateWormCentre,CC.PixelIdxList);
s = size(imgremoved);
[x,y] = ind2sub(s,centroids);
imgx = y;
imgy = x;
%class(imgremoved)
%centroids = regionprops(imgremoved,'centroid');
%centroids = cat(1,centroids.Centroid);
%plot(centroids(:,1),centroids(:,2),'*')
%imgremoved = imrotate(imgremove,180);
figure(3) 
imshow(imgremoved)
hold on
plot(imgx,imgy,'r*','MarkerSize',1)
%hold on
%plot(987,500,'*','MarkerSize',10)
%hold on
%plot(1198,500,'*','MarkerSize',10)
hold off


