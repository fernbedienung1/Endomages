function  [f, F] = histogra (pic)
    f = 0;
    F = 0;
    %read picture and create average over all colors (greyscale histogram)
%    pic = imread(picture);
    s = sum(pic,3)/3;
    [N,M] = size(s);    % dimensions of the image

    % create basis for historgram axises
    I_max = max(max(s)); % through lines and columns % this takes forever in python
    I_vals = [0:1:I_max];


    %frequency histogram
    f = hist(reshape(s, N*M,1), I_vals)/(N*M);
    F = cumsum(f);    %F = filter(1, [1 -1], f); is equvivalent
    return;

    % Finally create the Plot

    % frequency
%    figure(1); clf;
%    bar(I_vals, f);
%    title("freq hist");
%    xlabel("intensity");
%    ylabel("frequency");
%    axis ([0 I_max 0 1.2*max(f)]);
%    % cumulative 
%    figure(2); clf;
%    plot(I_vals, F);
%    title("cumulative Freq hist");
%    xlabel("intensity");
%    ylabel("cumulative Freq");
%    axis ([0 I_max 0 1]);
%
    % check out how to save them

    % and now we can transform shit
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

end
