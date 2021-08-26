//---- Implementacion de la clase persona (.cc)
#include "persona.h"

// Constructor sin argumentos
Persona::Persona(){

}
// Constructor con argumentos
Persona::Persona(std::string Nombre,std::string Afiliacion, std::string Correo){
	nombre=Nombre;
	afiliacion=Afiliacion;
	correo=Correo;
}

// Destructor
Persona::~Persona(){

}
// Metodo que devuelve el nombre de la persona
std::string Persona::getNombre(){
	return nombre;
}
