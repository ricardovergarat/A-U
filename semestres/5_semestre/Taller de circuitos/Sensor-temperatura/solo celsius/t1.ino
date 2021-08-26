#include <DallasTemperature.h>
#include <OneWire.h>



#define DATO 6

OneWire ourWire (DATO);
DallasTemperature sensors (&ourWire);

void setup (){
  Serial.begin (9600);
  Serial.println ("---------- REALIZADO POR ----------");
  Serial.println ("------ HTTPS://iTechWare.COM ------");
  Serial.println ("-- VISITALO PARA MAS INFORMACION --");
  delay (1500);
  sensors.begin ();
}

void loop (){
  sensors.requestTemperatures ();
  Serial.print (sensors.getTempCByIndex (0));
  Serial.println (" Grados Centigrados");
////////////////////////////////////////////////
//Recomiendo ver el tutorial para que veas como usar este codigo.
////////////////////////////////////////////////
  delay (1000);
}
