imgLocation = "../pic/smoke.jpg";
img = imread(imgLocation);
f = @(x) x.^0.3;
g = @(x) x.^1;
h = @(x) x.^3;

darker = histogramMatch(img, f);
normal =  histogramMatch(img, g);
lighter = histogramMatch(img, h);

figure(1); clf;
title("Gamma Adjustments")
subplot(1,3,1)
title("gamma = 0.3")
imshow(darker)

subplot(1,3,2)
title("gamma = 1")
imshow(normal)

subplot(1,3,3)
title("gamma = 3")
imshow(lighter)

pause;
