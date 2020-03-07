load("Mi_base_de_datos")
clc
orden = 3;
x = 0;
disp(3^4);
while x < 8
   y = 0;
   suma = 0;
   while y < 100
      suma = suma + base_de_datos{x + 3,y + 1}.tiempo;
      y =  y + 1; 
   end
   disp("promedio de: " + (x + 3) + " es: " + suma/100);
   p = suma/100 ;
   y = 0;
   suma2 = 0;
   while y < 100
       suma2 = suma2 + ( base_de_datos{x + 3,y + 1}.tiempo  - p)^2;
       y = y + 1;
   end
   disp("su desviacion de: " + (x + 3) + " es: " + suma2/99);
   disp("superior de: " + (x + 3) + " es: " + (p + suma2/99));
   disp("minimo de: " + (x + 3) + " es: " + (p - suma2/99));
   x = x + 1; 
end
