function [adjusted] = histogramMatch(img, matchingFunc)
    %img = imread(imageName)
    %input_class = class(img);
    [frq, cumFreq, I_vals] = histogram(img);
    %need to adjust matchingfunc (with F / I_max) before evaluating it?
    T = feval(matchingFunc, cumFreq);
    %T = fsolve(matchingFunc, cumFreq);
    adjusted = T(img -min(I_vals) +1);
    %adjusted = cast(adjusted, input_class);
