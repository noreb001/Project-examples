function [img] = getFace(img)


im = imresize(img, [1000 1200]);


detector = vision.CascadeObjectDetector;
detector.MergeThreshold = 4;
bbox = detector(im);

if isempty(bbox) == 0
J = imcrop(im,bbox(1,:));

img = imresize(J, [420 450]);

else 
    img = zeros(420,450);
end
end

