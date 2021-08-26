//---- Definicion de la clase autor (.h) 
//---- Clase hija de la clase Persona
#ifndef AUTOR_H
#define AUTOR_H
#include <string>
#include "persona.h"

class Autor : public Persona   // Se usa Herencia
{
public:
	// Constructores sin y con argumentos, Destructor y metodos.
	Autor();
	Autor(std::string Nombre,std::string Afiliacion,std::string Correo,std::string Grado);
	~Autor();

	std::string getGrado();

private:
	// Atributos
	std::string grado;
};
#endif