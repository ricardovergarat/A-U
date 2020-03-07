//---- Definicion de la clase persona (.h)
#ifndef PERSONA_H
#define PERSONA_H
#include <string>

class Persona
{
public:
	// Constructores sin y con argummentos, Destructor y metodos
	Persona();
	Persona(std::string Nombre,std::string Afiliacion, std::string Correo);
	~Persona();

	std::string getNombre();
	
private:
	// Atributos
	std::string nombre;
	std::string afiliacion;
	std::string correo; 
};
#endif