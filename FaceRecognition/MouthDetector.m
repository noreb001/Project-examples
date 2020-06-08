function [mouth] = MouthDetecor(img)


mouthDetector = vision.CascadeObjectDetector('ClassificationModel','mouth');

mouthDetector.MergeThreshold = 80;

mouthBbox = mouthDetector(img);


if isempty(mouthBbox) == 0 
j = imcrop(img,mouthBbox(1,:));
mouth = imresize(j, [250 450]);

else 
    
mouth = zeros([250 420]);
end



%IFaces = insertObjectAnnotation(j,'rectangle',mouthBbox,'nose');   
%imshow(nose)
end
