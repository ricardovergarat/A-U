clc
clear

B= 0.5
Y= 0.3

Vmin= 0.25
Vmax= 0.4
N=1

EIG_a  = []
Ibarra = []
for vv=Vmin:0.01:Vmax
 Ibarra=[Ibarra (N-(vv/B))/(vv+Y)]
% EIG_a=[EIG_a ; real(eig([-B*Y -Y ;0 0]+ vv*[0 -1; 0 0]+ Ibarra*[-B 0 ; B 0] ) )]
end

Imin = min(Ibarra)
Imax = max(Ibarra)

A0=[-B*Y -Y ;0 0];
A1=[0 -1; 0 0];
A2=[-B 0 ; B 0];



 An{1} = {[0 0],A0};
 An{2} = {[1 0],A1};
 An{3} = {[0 1],A2};
 
 Arolm= rolmipvar(An,'A',[Vmin Vmax ;
                          Imin Imax ]);

P11 = rolmipvar(2,2,'P11','symmetric',[2 2],[0 0])

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

W=double(P11)
% 
% double(P11)
% 
%  Arolm= rolmipvar(An,'A',[  (min(BufferSB)) (max(BufferSB)) ;
%                             (min(BufferPB)) (max(BufferPB)) ;
%                            C2M C2Mx  ;
%                            C3M C3Mx  ;
%                            C1M C1Mx  ;
%                            C4M C4Mx   ]);
%                        
%                        
% MSbarra=(C1M*C4M)/((C1M*C4M/k1)+C2M*C3M);
% MPbarra=(C1M)/(((C1M*C4M)/(C3M*k1))+C2M);
%  Am= [(C1M - 2*C1M*(MSbarra) /k1  -C2M*(MPbarra)) -C1M*(MSbarra); C3M -C4M]
% 
% Qm=Am'*double(P11) + double(P11)*Am
% 
% eig(Qm)





 