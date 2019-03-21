s = imread(image);

[r,g,b] = histogramRGB(s);

figure(1)
%%Red
title("Red Channel")
subplot(3,3,1)
imshow(s(:,:,1))
subplot(3,3,2)
hist(r(:,1))
subplot(3,3,3)
plot(r(:,2))

%%Green
title("Green Channel")
subplot(3,3,4)
imshow(s(:,:,2))
subplot(3,3,5)
hist(g(:,1))
subplot(3,3,6)
plot(g(:,2))

%%Blue
title("Blue Channel")
subplot(3,3,7)
imshow(s(:,:,3))
subplot(3,3,8)
hist(b(:,1))
subplot(3,3,9)
plot(b(:,2))

pause;
close all;
