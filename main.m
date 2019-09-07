img = imread('/Users/apple/Desktop/IGEM/post/tracking/WormTrack/C.elegans_003323_0001.tif');
%Handling Background and Worms Localization
contrastAdjusted = BgNormal(img);
[imgx,imgy] = BgThresh(contrastAdjusted);