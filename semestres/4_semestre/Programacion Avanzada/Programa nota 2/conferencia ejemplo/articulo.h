//---- Definicion de la clase articulo (.h)
#ifndef ARTICULO_H
#define ARTICULO_H
#include <string>
#include "autor.h"

class Articulo
{
public:
	// Constructor, Destructor y metodos
	Articulo(std::string Titulo,Autor aut);
	~Articulo();

	std::string getTitulo();
	Autor getAutor();

private:
	// Atributos 
	std::string estado;
	std::string fechaEnvio;
	std::string titulo;
	std::string resumen;
	std::string cuerpo;
	Autor autor;
};

#endif