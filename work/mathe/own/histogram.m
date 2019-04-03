function [f,F,I_vals] = histogram(img)
    % get dimension
    dim = size(img);
    % create monochrome Picture by average colors
    mono = sum(img,3)/dim(3);
    % get maximum intensity of monochrome image
    % create scale (all intesities)
    I_vals = [1:1:255];

    % create histogram
    h = hist(mono(:), I_vals);
    f = h/length(mono(:));
    F = cumsum(f);      % cumulated sum over f
