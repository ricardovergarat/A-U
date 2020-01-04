clc
clear

C9m=0.26
C9M=0.095
C10m=0.21
C10M=0.9
As{1} = [-0.7050 0.49 0 0; 0.6950 -2.4350 0.4 0.9;0 1.85 -0.91 0; 0 C9m  0 -C10m]
As{2} = [-0.7050 0.49 0 0; 0.6950 -2.4350 0.4 0.9;0 1.85 -0.91 0; 0 C9M  0 -C10m]
As{3} = [-0.7050 0.49 0 0; 0.6950 -2.4350 0.4 0.9;0 1.85 -0.91 0; 0 C9m  0 -C10M]
As{4} = [-0.7050 0.49 0 0; 0.6950 -2.4350 0.4 0.9;0 1.85 -0.91 0; 0 C9M  0 -C10M]

% 
% As{1} = [-0.7050 0.49 0 0; 0.6950 -2.4350 0.4 0.9;0 1.85 -0.91 0; 0 0.095 0 -0.21]
% As{2} = [-0.7050 0.49 0 0; 0.6950 -2.4350 0.4 0.9;0 1.85 -0.91 0; 0 0.095 0 -0.21]
% As{3} = [-0.7050 0.49 0 0; 0.6950 -2.4350 0.4 0.9;0 1.85 -0.91 0; 0 0.095 0 -0.21]
% As{4} = [-0.7050 0.49 0 0; 0.6950 -2.4350 0.4 0.9;0 1.85 -0.91 0; 0 0.095 0 -0.21]

 for i=1:4
    eig(As{i}) 
 end
 
 Arolm= rolmipvar(As,'A',4,1);

P11 = rolmipvar(4,4,'P11','symmetric',[4],[0])

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


% 
double(P11)
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





 