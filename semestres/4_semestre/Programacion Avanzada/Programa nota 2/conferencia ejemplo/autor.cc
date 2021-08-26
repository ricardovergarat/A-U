//---- Implementacion de la clase autor (.cc)
#include "autor.h"
// Constructor sin argumentos 
Autor::Autor(){

}
// Cnstructor con argumentos
Autor::Autor(std::string Nombre,std::string Afiliacion,std::string Correo,std::string Grado) : Persona(Nombre,Afiliacion,Correo){
	grado=Grado;
}
// Destructor 
Autor::~Autor(){

}

// Metodo que devuelve el grado
std::string Autor::getGrado(){
	return grado;
}