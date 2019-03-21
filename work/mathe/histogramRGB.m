function [r, g, b] = histogramRGB (img) 
    r = [0 0];
    g = [0 0];
    b = [0 0];

    %create one Vektor with all colors
    [img_x , img_y, img_z] = size(img);
    colorsO= reshape(img, img_x* img_y, img_z); % one long Vek with all colors

    %scaling for colorvals (create 1-255 scale)
    %red
    Intensity_maxR = max(colorsO(:,1));
    Intensity_valsR = [0:1:Intensity_maxR];
    %green
    Intensity_maxG = max(colorsO(:,2));
    Intensity_valsG = [0:1:Intensity_maxG];
    %blue
    Intensity_maxB = max(colorsO(:,3));
    Intensity_valsB = [0:1:Intensity_maxB];

    %create the histograms 
    %red
    freqHist_R = hist(colorsO(:,1),Intensity_valsR)/(img_x*img_y);
    cumFreqHist_R = cumsum(freqHist_R);
    %green
    freqHist_G = hist(colorsO(:,2),Intensity_valsG)/(img_x*img_y);
    cumFreqHist_G = cumsum(freqHist_G);
    %blue
    freqHist_B = hist(colorsO(:,3),Intensity_valsB)/(img_x*img_y);
    cumFreqHist_B = cumsum(freqHist_B);

    %create returnvals
    r = [freqHist_R, cumFreqHist_R];
    g = [freqHist_G, cumFreqHist_G];
    b = [freqHist_B, cumFreqHist_B];
    return 
%
%    % create something with subplots here
%    figure(1); clf;
%    bar(Intensity_valsR, freqHist_R, ...
%        "facecolor", "r")
%    figure(2); clf;
%    plot(Intensity_valsR, cumFreqHist_R, ...
%        "color", "r");
%    pause;
%    close all;
