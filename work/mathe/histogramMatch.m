function [adjusted] = histogramMatch(imageName, matchingFunc)
    %img = imread(imageName)
    [frq, cumFreq] = histogram(imageName);
    printf("dicho y hecho! \n")
    whos
    feval(matchingFunc, )
    % called via defining function handle
    % and then call histogramMatch("imname", handle)
