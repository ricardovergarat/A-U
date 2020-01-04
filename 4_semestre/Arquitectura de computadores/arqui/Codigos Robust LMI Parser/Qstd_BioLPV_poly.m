function [ output ] = Qstd_BioLPV_poly(A)

NV=size(A,2)
nx=size(A{1},1)
 Arolm= rolmipvar(A,'A',[NV],[1]);
 P11 = rolmipvar(nx,nx,'P11','symmetric',[NV],[0])

    LMIx=Arolm'*P11+P11*Arolm
    LMIs = [LMIx<0,P11>0];
    
sol = solvesdp(LMIs, [], sdpsettings('solver', 'sedumi', 'verbose', 0));

 output.cpusec = sol.solvertime;

output.p = min(checkset(LMIs))

output.cpusec = sol.solvertime;

output.p = min(checkset(LMIs));
% checkset(LMIs)

output.V = size(getvariables(LMIs),2);
output.L = 0;
for i=1:size(LMIs,1)
    output.L = output.L + size(LMIs{i},1);
end
output.feas = 0;

if(min(checkset(LMIs))>0)
output.W=double(P11)
output.feas = 1;
else
end
end

