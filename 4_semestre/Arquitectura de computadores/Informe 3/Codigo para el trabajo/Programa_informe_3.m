clc           %---------> esto limpia los mostrado por consola anteriormente
warning('off','YALMIP:strict');
load("Mi_base_de_datos")
orden = 10;
intentos = 1; %---------> poner el ultimo intento del archivo, si es el primero poner 1, esto solo se aplicara en los archivos .txt
cantidad = 100;  %---------> cuantas matrices quieres agregar al archivo, este programa esta hecho de tal forma que impleca que usted tiene 100 - cantidad  de matricez en el archivo 
Theta1m = 0.25;
Theta1M = 0.4;
Theta2m = 1;
Theta2M = 3;
string_orden = num2str(orden);
nombre_archivo = string_orden + ".txt";
x = 0;
while x < cantidad
   % creacion de las matrices aleatorias
   matrix_A0 = rand(orden); 
   matrix_A1 = rand(orden);
   matrix_A2 = rand(orden);
   
   su_matrix_simetrica = eye(orden); % por si no recuerdan la simetrica es cuando SOLO la diagional es 1
   A0= matrix_A0 - su_matrix_simetrica ;
   A1= matrix_A1 - su_matrix_simetrica ;
   A2= matrix_A2 - su_matrix_simetrica ;
   
   correcion = 0; %---------> la cantidad de veces que corejimos la matrix
   candidato = false;
   %-----------------------------
   % candidatos
   
   while (candidato ~= true )
      for i = 1:20
          for j = 1:20
      TETHA1= Theta1m + ((1-1)/19)*(Theta1M-Theta1m);
      TETHA2= Theta2m + ((j-1)/19)*(Theta2M-Theta2m);
       
      Axx= A0 +TETHA1*A1+TETHA2*A2;
      ReA_sys(i,j)=max(real(eig(Axx)));        
          end
      end
     
      if ReA_sys > 0
          if correcion == 3
              % la coregimos tres vez asi que mejor usaremos otra matrix 
              % aleatoria
              break;
          end
          %disp("No es candidato por ende usaremos proceso isaic ");
          % la idea de este proceso fue pedida a los siguientes estudiantes
          % diegos rojas 
          % isaic morales
          % si existe algun similitud en los resultados es debido a esto
          
          mega_maximo = max(max(ReA_sys));
          %%%disp("mega maximo: " + mega_maximo);
          A0 = A0 - su_matrix_simetrica * mega_maximo * 0.5 ;
          A1 = A1 - su_matrix_simetrica * mega_maximo * 0.5;
          A2 = A2 - su_matrix_simetrica * mega_maximo * 0.5;
          intentos = intentos + 1;
          correcion = correcion + 1;
      else
          %%% ahora es candidato
          candidato = true;
      end
      
   end
   
   if ReA_sys > 0
       %no logro ser candidato pesea a ser usado el proceso isaic tres vece
       intentos = intentos + 1;
   else
       %%% es candidato
       %-----------------------------
       
       %|||||||||||||||||||||||||||||
       % aqui trataremos de determinar la estabilidad del sistema
    
       An{1} = {[0 0],A0}; % exponente a cada alfa
       An{2} = {[1 0],A1};
       An{3} = {[0 1],A2};
       
       Arolm= rolmipvar(An,'A',[Theta1m Theta1M ; % creacion de caja con sus valores en los vertices
                            Theta2m Theta2M ]);
       P11 = rolmipvar(orden,orden,'P11','symmetric',[2 2],[0 0]);
       LMIx = Arolm'*P11+P11*Arolm;
               LMIs = [LMIx<0,P11>0];
       sol = solvesdp(LMIs, [], sdpsettings('solver', 'sedumi', 'verbose', 0));
       cpusec = sol.solvertime; % -------> esto se supone que es el tiempo
       p = min(checkset(LMIs)); % esto es lo bueno  si es positvo es estable
       V = size(getvariables(LMIs),2); % -------> registrar en resultados
       L = 0; % --------------------------------> registrar en resultados
       
       for i=1:size(LMIs,1)
           L = L + size(LMIs{i},1);
       end
       
       feas = 0;
       W=double(P11);
    
       %|||||||||||||||||||||||||||||
       
       if p > 0
           %%%disp("Es estable");
           %%%disp("Esta es la matrix: " + W);
           %%%disp("el sistema se demoro: " + cpusec);
           %%%disp("Estamos en el intento: " + intentos);
           
           %+++++++++++++++++++++++++++++++++++++++++++
           % recuperaremos los escrito en el archivo
           y = 0;
           archivo = fopen(nombre_archivo);
           texto_archivo = "";
           while y < ( (100 - cantidad) + x ) %------------------------> (100 - cantidad) es la cantidad de matrices que deberia tener en el archivo |||| + x es la cantidad de matrices agregadas en este proceso
               linea = fgetl(archivo);
               texto_archivo = texto_archivo  + linea + char(13);
               y = y + 1;
           end
           fclose(archivo);
           %+++++++++++++++++++++++++++++++++++++++++++
           
           string_matrix = mat2str(W);
           string_intento = num2str(intentos);
           string_tiempo = num2str(cpusec);
           nueva_linea = texto_archivo + "intento: " + string_intento + " " + "tiempo: " + string_tiempo + " " + string_matrix;
           archivo = fopen(nombre_archivo,"w");
           fprintf(archivo,'%s',nueva_linea);
           fclose(archivo);
           intentos = intentos + 1;
           if mod(x,5) == 0
               disp(x + " % completo");
           end
           % amadimos los valores a la base de datos
           base_de_datos{orden,x + 1}.A0 = A0;
           base_de_datos{orden,x + 1}.A1 = A1;
           base_de_datos{orden,x + 1}.A2 = A2;
           base_de_datos{orden,x + 1}.Theta1m = Theta1m;
           base_de_datos{orden,x + 1}.Theta1M = Theta1M;
           base_de_datos{orden,x + 1}.Theta2m = Theta2m;
           base_de_datos{orden,x + 1}.Theta2M = Theta2M;
           base_de_datos{orden,x + 1}.tiempo = cpusec;
           x = x + 1;
       else
           %%%disp("No es estable");
           intentos = intentos + 1;
       end
   end
end
save("Mi_base_de_datos","base_de_datos")
disp("100 %");