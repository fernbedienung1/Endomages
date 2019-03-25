function [adjusted] = histogramMatch(img, matchingFunc)
    %img = imread(imageName)
    [frq, cumFreq, I_vals] = histogram(img);
    %need to adjust matchingfunc (with F / I_max) before evaluating it?
    T = feval(matchingFunc, cumFreq);
    adjusted = T(img -min(I_vals) +1);
