function s_new = histogram_match(pic)

if strcmp(type, 'cosine')
    if nargin~=4
        error('invalid nr of args');
    end
else 
    if (nargin~=3)&(nargin~=4)
        error('invalid nr of args');
    end
end

input_class = class(s_old);
s_old   = double(s_old);

dim = size(s_old);
switch length(dim)
case 2
    image_type = 'monochrome'
    s_mono  =s_old;
case 3 
    image_type = 'RGB'
    s_mono = sum(s_old, 3)/dim(3);
otherwise
    error('sold must be 2- or 3 dimentional')
end


I_max = max(I_vals);
if max(s_old(:)) > I_max
    fprintf(['Warning: the maximum image intensity is greather than ' ... 
    'the largest intesity in I_vals']);
end




h = hist(s_mono(:), I_vals);
f = h/length(s_mono(:));
F = cumsum(f);

switch type 
case 'uniform'
    T = Imax*F;
case 'linear'
    T = I_max * sqrt(F);
case 'sine'
    T = real(I_max*acos(1 - 2*F)/pi);
case 'cosine'
    A = params.A;
    phi = params.phi;
    x_hat = fsolve(...
    @(x) (F- x - (A/(2*pi))*(sin(2*pi*x + phi) - sin(phi))), ...
    zeros(size(F)));
    T = I_max*x_hat;
end


s_new = T(s_old - min(I_vals) + 1);
s_new = cast(s_new, input_class);

return;
