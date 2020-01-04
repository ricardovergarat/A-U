function c = coefs(X)
%  Retrieve the coefficients of the polynomial struct
%  to get more flexibility.
%
    if isa(X, 'rolmipvar')
        for i = 1:length(X.data)
            c{i} = X.data(i).value;
        end
    else
        c = {X};
    end
end
