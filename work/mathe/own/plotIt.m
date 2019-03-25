%reading Images from pic folder
own = imread("../pic/own.jpg");
real = imread("../pic/real.jpg");

% get the histograms - just to show them nicely
%[own_f, own_F] = histogram(own);
%[real_f, real_F] = histogram(real);

% the matching function for both

g = @(x) x+0.2;
h = @(x) x.*1.1;
i = @(x) x.^2;

% create all the output images
adjusted_g_own = histogramMatch(own, g);
adjusted_h_own = histogramMatch(own, h);
adjusted_i_own = histogramMatch(own, i);

adjusted_g_real = histogramMatch(real, g);
adjusted_h_real = histogramMatch(real, h);
adjusted_i_real = histogramMatch(real, i);

% finaly display them
figure(1); clf;

subplot(2,2,1)
imshow(own)
title("original")

subplot(2,2,2)
imshow(adjusted_g_own)
title("adding Constant")

subplot(2,2,3)
imshow(adjusted_h_own)
title("multiplied Constant")


subplot(2,2,4)
imshow(adjusted_i_own)
title("squared")


figure(2); clf;

subplot(2,2,1)
imshow(real)
title("original")

subplot(2,2,2)
imshow(adjusted_g_real)
title("adding Constant")

subplot(2,2,3)
imshow(adjusted_h_real)
title("multiplied Constant")


subplot(2,2,4)
imshow(adjusted_i_real)
title("squared")
