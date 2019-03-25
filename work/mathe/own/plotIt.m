%reading Images from pic folder
own = imread("../pic/own.jpg");
%own = imread("../pic/real.jpg");
%real = imread(../pic/real.jpg);

% get the histograms - just to show them nicely
%[own_f, own_F] = histogram(own);
%[real_f, real_F] = histogram(real);

% the matching function for both

g = @(x) x+0.2;
h = @(x) x.*1.1;
i = @(x) x.^2;

% create all the output images
adjusted_g = histogramMatch(own, g);
adjusted_h = histogramMatch(own, h);
adjusted_i = histogramMatch(own, i);

% finaly display them
figure(1); clf;

subplot(2,2,1)
imshow(own)
title("original")

subplot(2,2,2)
imshow(adjusted_g)
title("adding Constant")

subplot(2,2,3)
imshow(adjusted_h)
title("multiplied Constant")


subplot(2,2,4)
imshow(adjusted_i)
title("squared")
