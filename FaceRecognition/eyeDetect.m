function [eyebrow, eye] = eyeDetect(img)


eyeDetector = vision.CascadeObjectDetector('ClassificationModel','EyePairBig');

eyeDetector.MergeThreshold = 7;
eyeBbox = eyeDetector(img);

if isempty(eyeBbox) == 0 

x = eyeBbox(1,1);
y = eyeBbox(1,2)-40;
length = eyeBbox(1,3);
height = eyeBbox(1,4);
eyebrow = imcrop(img,[x,y,length,height]);
eyebrow = imresize(eyebrow, [100 420]);


j = imcrop(img,eyeBbox(1,:));
eye = imresize(j, [250 480]);

else
    eye = zeros([250 480]);
eyebrow = zeros([100 420]);


end

end