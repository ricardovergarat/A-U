clc
clear
% warning('off','YALMIP:strict') 
B= 0.5
Y= 0.3

Theta1m= 0.25
Theta1M= 0.4

Theta2m = 1
Theta2M = 3

A0=[0 1;-0.5 -0.3];

A1=[0 -1; 0 0];
A2=[-0.01 0 ; 0.01 0];



 An{1} = {[0 0],A0};
 An{2} = {[1 0],A1};
 An{3} = {[0 1],A2};
 
 Arolm= rolmipvar(An,'A',[Theta1m Theta1M ;
                          Theta2m Theta2M ]);
% size(A1,1)
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


%%%%%%%%%%%%

clc
clear

Theta1m= 0.1
Theta1M= 0.4
Theta2m = -0.03
Theta2M = 0.02
A0=[0 1;-0.5 -0.3];
A1=[0 -1; 0 5];
A2=[-3 0 ; 6 0];

for i=1:20
    for j=1:20
TETHA1= Theta1m + ((1-1)/19)*(Theta1M-Theta1m)
TETHA2= Theta2m + ((j-1)/19)*(Theta2M-Theta2m)
        
Axx= A0 +TETHA1*A1+TETHA2*A2

Re_sys(i,j)=max(abs(eig(Axx)))

    end
end

mesh(Re_sys)
















 