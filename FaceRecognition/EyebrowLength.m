function [thickness] = EyebrowLength (EyeBrowimg) 





eyebrow = rgb2gray(EyeBrowimg);
%eyebrow = histeq(eyebrow);
eyebrow2 = imbinarize(eyebrow, 'global');
BW2 = edge(eyebrow2,'Sobel');
corners = detectHarrisFeatures(BW2, 'MinQuality', 0.3);

xx = min(corners.Location(:,1));
yy = min(corners.Location(:,2));
xTemp = (find (corners.Location(:,1)== xx));
ymin = corners.Location(xTemp,2);

EyeBrowThickness = ymin - yy


figure
imshow(BW2); hold on;
plot(corners.selectStrongest(50));



end
