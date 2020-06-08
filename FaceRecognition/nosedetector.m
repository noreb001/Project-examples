function [nose] = nosedetector(img)

noseDetector = vision.CascadeObjectDetector('ClassificationModel','nose');

noseDetector.MergeThreshold = 5;
noseBbox = noseDetector(img);

if isempty(noseBbox) == 0 
j = imcrop(img,noseBbox(1,:));
nose = imresize(j, [420 250]);

else 
    
nose = zeros([420 250]);
end



%IFaces = insertObjectAnnotation(j,'rectangle',mouthBbox,'nose');   
%imshow(nose)
end
