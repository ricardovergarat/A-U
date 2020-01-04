clc 
clear all 
close all

 Gmma=10
 Gmma2=0.3
C1M =  0.65    ;
C1Mx=   0.65    ;
C1Mx-C1M

C2M = 0.3	    ;
C2Mx= 0.31	    ;
C2Mx-C2M

C3M =  0.33   ;
C3Mx=  0.33    ;
C3Mx-C3M

C4M =  0.4769   ;
C4Mx=  0.4769    ;
C4Mx-C3M

C5M =   0.2697  ;
C5Mx=  0.2697   ;
C5Mx-C3M

A0=[-1 0 0 ;
    1 0 0;
    0 0 0];
A1=[0 -1 0 ;
    0  1 0 ;
    0  0 0 ];
A2=[0 0 0 ;
    0 -1 0;
    0 1 0];
A3=[0 0 1 ;0 0 0; 0 0 -1];









 An{1} = {[1 0 0 0 1],A0};
 An{2} = {[1 0 0 1 0],A1};
 An{3} = {[0 1 0 0 0],A2};
 An{4} = {[0 0 1 0 0],A3};

 
 Arolm= rolmipvar(An,'A',[ C1M C1Mx  ;
                           C2M C2Mx  ;
                           C3M C3Mx  ;
                           C4M C4Mx  ;
                           C5M C5Mx ]);


%  P11 = rolmipvar(2,2,'P11','symmetric',[Sbarra(1) Sbarra(100);Pbarra(1) Pbarra(100); C22(1) C22(100)],[0 0 0]);
% 
%  P11 = rolmipvar(2,2,'P11','symmetric',[Sbarra(1) Sbarra(100)],[Pbarra(1) Pbarra(100)],[ C22(1) C22(100)]);


P11 = rolmipvar(3,3,'P11','symmetric',[2 2 2 2 2],[0  0  0 0 0])

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





 