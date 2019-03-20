%image = '~/Pictures/Rick.jpg';
%image = '~/Desktop/test/con0.jpg'
image = '~/Desktop/schmauch/Schmauchordner/s1.jpg'
s = imread(image);
I_vals = [0:1:2^8-1];        % this looks like some kind of datatype..

figure(1); clf;
set(gcf, 'units', 'normalized', ...
        'position', [.1 .2 .7 .7], ...
        'color', 'w');


[f, F] = histogra(sum(s,3)/3, I_vals);
subplot(2,3,[1 2 4 5]);
imshow(s); axis image; axis off;
subplot(2, 3, 3);
bar(f);
axis([min(I_vals) max(I_vals) 0 1.2*max(f)]);
pause;

%Linear Matching
s_new = histogram_match(s, I_vals, 'linear');
[f, F] = histogra(sum(s_new,3)/3, I_vals);
subplot(2,3,[1 2 4 5]);
imshow(s_new); axis image; axis off;
subplot(2, 3, 3);
bar(f)
axis([min(I_vals) max(I_vals) 0 1.2*max(f)]);
pause;


%uniform Matching
s_new = histogram_match(s, I_vals, 'uniform');
[f, F] = histogra(sum(s_new,3)/3, I_vals);
subplot(2,3,[1 2 4 5]);
imshow(s_new); axis image; axis off;
subplot(2, 3, 3);
bar(f)
axis([min(I_vals) max(I_vals) 0 1.2*max(f)]);
pause;

%sine wave Matching
s_new = histogram_match(s, I_vals, 'sine');
[f, F] = histogra(sum(s_new,3)/3, I_vals);
subplot(2,3,[1 2 4 5]);
imshow(s_new); axis image; axis off;
subplot(2, 3, 3);
bar(f)
axis([min(I_vals) max(I_vals) 0 1.2*max(f)]);
pause;

%cosine matching
params.A = 0.9;
params.phi = pi/2;
s_new = histogram_match(s, I_vals, 'cosine');
[f, F] = histogra(sum(s_new,3)/3, I_vals);
subplot(2,3,[1 2 4 5]);
imshow(s_new); axis image; axis off;
subplot(2, 3, 3);
bar(f)
axis([min(I_vals) max(I_vals) 0 1.2*max(f)]);
pause;
close;
