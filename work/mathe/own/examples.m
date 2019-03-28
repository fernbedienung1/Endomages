%reading Images from pic folder
own = imread("../pic/example_pic_0.jpg");
% the matching function for both

g = @(x) x + x.*1.1; % Helligkeits anpassung
h = @(x) x.*1.1;    % Gamma Adjustment
i = @(x) x ./ (1 + e .^ -1.1);     %sigmoid function /contrast

% create all the output images
adjusted_g_own = histogramMatch(own, g);
adjusted_h_own = histogramMatch(own, h);
adjusted_i_own = histogramMatch(own, i);

% finaly display them
figure(1); clf;

subplot(4,1,1)
imshow(own)
title("Original")

subplot(4,1,2)
imshow(adjusted_g_own)
title("Brightness")

subplot(4,1,3)
imshow(adjusted_h_own)
title("Gamma")

subplot(4,1,4)
imshow(adjusted_i_own)
title("Contrast")


imwrite(adjusted_g_own, "out/brightness.jpg")
imwrite(adjusted_h_own, "out/gamma.jpg")
imwrite(adjusted_i_own, "out/sigmoid.jpg")
