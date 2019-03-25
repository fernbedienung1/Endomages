function [f,F,I_vals] = histogram(img)
%    img = imread(imageName);
    % get dimension
    dim = size(img);
    % create monochrome Picture by average colors
    mono = sum(img,3)/dim(3);
    % get maximum intensity of monochrome image
%    I_max = max(max(mono));
    % create scale (all intesities)
    I_vals = [1:1:255];

    % Here happens the action

    % create histogram
    h = hist(mono(:), I_vals);
    f = h/length(mono(:));
    F = cumsum(f);      % hihihihi cumsum 
