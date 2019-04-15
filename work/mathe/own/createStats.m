%reading Images from pic folder
own = imread("../pic/example_pic_0.jpg");
%real = imread("../pic/real.jpg");
[own_f, own_F] = histogram(own);
%[real_f, real_F] = histogram(real);

% Matching Functions as handles
g = @(x) sqrt(x);
h = @(x) x.^2;
%g = @(x) x.^3

% create all the output images
adjusted_g_own = histogramMatch(own, g);
adjusted_h_own = histogramMatch(own, h);
% super stupid workaround - TODO: remove before you show this to anyone -.-
mkdir("out");
imwrite(adjusted_g_own, "out/adjusted_g_own.jpg");
imwrite(adjusted_h_own, "out/adjusted_h_own.jpg");
adjusted_g_own = imread("out/adjusted_g_own.jpg");
adjusted_h_own = imread("out/adjusted_h_own.jpg");

[own_g_f, own_g_F] = histogram(adjusted_g_own);
[own_h_f, own_h_F] = histogram(adjusted_h_own);


% finaly display them
fig1 = figure(1); clf;
title("Original Image")

subplot(3,3,1)
imshow(own)
title("Input")

subplot(3,3,2)
plot(own_f)
title("frequency Histogram")

subplot(3,3,3)
plot(own_F)
title("cumulated Freq Hist")
%------------------------------------------------------------------------------

subplot(3,3,4)
imshow(adjusted_g_own)
title("squareRoot filter")

subplot(3,3,5)
plot(own_g_f)
title("frequency Histogram")

subplot(3,3,6)
plot(own_g_F)
title("cumulated Freq Hist")
%------------------------------------------------------------------------------

subplot(3,3,7)
imshow(adjusted_h_own)
title("squared filter")

subplot(3,3,8)
plot(own_h_f)
title("frequency Histogram")

subplot(3,3,9)
plot(own_h_F)
title("cumulated Freq Hist")

%------------------------------------------------------------------------------
%------------------------------------------------------------------------------

%fig2 = figure(2); clf;
%title("Original Image")

%subplot(3,3,1)
%imshow(real)
%title("Input")

%subplot(3,3,2)
%plot(real_f)
%title("frequency Histogram")
%
%subplot(3,3,3)
%plot(real_F)
%title("cumulated Freq Hist")
%%------------------------------------------------------------------------------
%
%subplot(3,3,4)
%imshow(adjusted_g_real)
%title("squareRoot filter")
%
%subplot(3,3,5)
%plot(real_g_f)
%title("frequency Histogram")
%
%subplot(3,3,6)
%plot(real_g_F)
%title("cumulated Freq Hist")
%%------------------------------------------------------------------------------
%
%subplot(3,3,7)
%imshow(adjusted_h_real)
%title("squared filter")
%
%subplot(3,3,8)
%plot(real_h_f)
%title("frequency Histogram")
%
%subplot(3,3,9)
%plot(real_h_F)
%title("cumulated Freq Hist")
pause;
