clc 
clear all 
close all

%% Modelo Salmones
%% PARÂMETROS
% número máximo de salmones
k1=100;
% tasa de crecimiento de salmones
c1=1/3;
% tasa de mortalidad de salmones debido a la contaminación
c2=0.01/2;
% tasa de crecimiento de la contaminación debido a la población de salmones
c3=0.015;
% tasa de decrecimiento de la contaminación por limpieza natural del agua
c4=0.15/3;
% tasa de decrecimiento de la población de salmones debido a la aparición de algas
c5=15/300;
% tasa de crecimiento de la contaminación debido a la aparición de algas
c6=(1/3)*c5;
%% Condiciones iniciales
S=70;
P=10;

%% switch para activar algas (es solo comentar)
% con algas key = 1
key=1;
% sin algas
%key=0;

% Tempo
t=1:0.1:200;
sigma=10;  % controla el ancho del fenómeno del niño
mu=110;    % controla el tiempo en que aparece el peak del fenomeno del niño

%% SISTEMA APROXIMADO
% % Solucoes aproximadas das EDOs:
 fg=@(t,y) ...
[c1*y(1)*(1-(y(1)/k1))-c2*y(1)*y(2)-key*c5*(100*exp(-(t-mu).^2/sigma^2));...
c3*y(1)-c4*y(2)+key*c6*100*exp(-(t-mu).^2/sigma^2)];

%% Gráficos (dependientes de key)
 % solve EDO desde f, dominio e cond inicial
 if key==0
  [t,y]=ode45(fg,t,[S P]);
   %% Gráficos
   figure;
   hold on
   grid on
   plot(t,y(:,1),'b','Linewidth',1.5)
   plot(t,y(:,2),'g','Linewidth',1.5) 
   legend('Salmones','Contaminación')
 else
   omega=100*exp(-(t-mu).^2/sigma^2);
  [t,y]=ode45(fg,t,[S P]);
   %% Gráficos
   figure;
   hold on
   grid on
   plot(t,y(:,1),'b','Linewidth',1.5)
   plot(t,omega,'g','Linewidth',1.5)
   plot(t,y(:,2),'k','Linewidth',1.5)    
   legend('Salmones','Algas','Contaminación')
 end
%% Puntos de Equilibrio (Solo para confirmar)
clear
clc

c5=5/300
 GG=  1  %3.4795
 k1=100
 
C1M =  0.03        ;
C1Mx=   0.036667   ;
C1Mx-C1M

C2M = 0.0003	    ;
C2Mx= 0.000367	    ;
C2Mx-C2M

C3M =0.000333   ;
C3Mx=0.000407   ;
C3Mx-C3M



C4M =   0.003	   ;
C4Mx=   0.003667   ;
C4Mx-C4M

C5M =   0.004286	   ;
C5Mx=   0.005238       ;
C5Mx-C5M

C6M =   0.000612	   ;
C6Mx=   0.000748  ;
C6Mx-C6M

warning('off','YALMIP:strict') 
Buffer=[]
BufferH2=[]

BufferPB=[]
BufferSB=[]

Inter=3
    for j=1:Inter+1
        for i=1:Inter+1
            for U=1:Inter+1
                for E=1:Inter+1
                                    for TT=1:Inter+1

                                    for JJ=1:Inter+1

    c1=  C1M + (j-1)*(C1Mx-C1M)/Inter;
    c2=  C2M + (i-1)*(C2Mx-C2M)/Inter;
    c3=  C3M + (U-1)*(C3Mx-C3M)/Inter;
    c4=  C4M + (E-1)*(C4Mx-C4M)/Inter;
  c5=  C5M + (TT-1)*(C5Mx-C5M)/Inter;
    c6=  C6M + (JJ-1)*(C6Mx-C6M)/Inter;

    %
%     Xc2(i)=c2 ; 
%     Xc3(U)=c3 ; 
%     %
%     C22(U,i)=c2;
%     C33(U,1)=c3;

Sbarra=(c1*c4)/((c1*c4/k1)+c2*c3);
Pbarra=(c1)/(((c1*c4)/(c3*k1))+c2);




 EPT=c2*Pbarra;
 EST=c2*Sbarra;
 
 A= [(c1 - 2*c1*Sbarra/k1  -EPT) -EST; c3 -c4];
 B=[-c5 ; c6]*100 ;

AuV=max(real(eig(A))) ;
Vs=[AuV c1 c2 c3 c4]' ;
Buffer= [Buffer  Vs ];
BufferPB=[BufferPB Pbarra];
BufferSB=[BufferSB Sbarra];



NormH2 = norm(ss( A, B,eye(2),0),2) ;
Vh2=[NormH2 c1 c2 c3 c4 c5 c6]' ;
BufferH2= [BufferH2  Vh2 ];
end 
end 
        end

            end
        [j i]
        end
 %   j
    end
% figure 
% mesh(Xc3,Xc2,Norm,'DisplayName','H_2')

% figure 
% mesh(Xc3,Xc2,EUT,'DisplayName','Max Auto Valor')
% 
% figure 
% mesh(Xc3,Xc2,Sbarra,'DisplayName','Sbarra')
% 
% figure 
% mesh(Xc3,Xc2,Pbarra,'DisplayName','Pbarra')

A0=[0 0 ;0 0];
A1=[0 -1; 0 0];
A2=[-1 0; 0 0];
A3=[-2/k1 0;0 0];
A4=[0 0; 1 0];
A5=[1 0; 0 0];
A6=[0 0; 0 -1];






 An{1} = {[0 0 0 0 0 0],A0};
 An{2} = {[1 0 1 0 0 0],A1};
 An{3} = {[0 1 1 0 0 0],A2};
 An{4} = {[1 0 0 0 1 0],A3};
 An{5} = {[0 0 0 1 0 0],A4};
 An{6} = {[0 0 0 0 1 0],A5};
 An{7} = {[0 0 0 0 0 1],A6};
 
 Arolm= rolmipvar(An,'A',[  (min(BufferSB)) (max(BufferSB)) ;
                            (min(BufferPB)) (max(BufferPB)) ;
                           C2M C2Mx  ;
                           C3M C3Mx  ;
                           C1M C1Mx  ;
                           C4M C4Mx   ]);


%  P11 = rolmipvar(2,2,'P11','symmetric',[Sbarra(1) Sbarra(100);Pbarra(1) Pbarra(100); C22(1) C22(100)],[0 0 0]);
% 
%  P11 = rolmipvar(2,2,'P11','symmetric',[Sbarra(1) Sbarra(100)],[Pbarra(1) Pbarra(100)],[ C22(1) C22(100)]);


P11 = rolmipvar(2,2,'P11','symmetric',[2 2 2 2 2 2],[0  0 0 0 0 0])

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



double(P11)

 Arolm= rolmipvar(An,'A',[  (min(BufferSB)) (max(BufferSB)) ;
                            (min(BufferPB)) (max(BufferPB)) ;
                           C2M C2Mx  ;
                           C3M C3Mx  ;
                           C1M C1Mx  ;
                           C4M C4Mx   ]);
                       
                       
MSbarra=(C1M*C4M)/((C1M*C4M/k1)+C2M*C3M);
MPbarra=(C1M)/(((C1M*C4M)/(C3M*k1))+C2M);
 Am= [(C1M - 2*C1M*(MSbarra) /k1  -C2M*(MPbarra)) -C1M*(MSbarra); C3M -C4M]

Qm=Am'*double(P11) + double(P11)*Am

eig(Qm)





 