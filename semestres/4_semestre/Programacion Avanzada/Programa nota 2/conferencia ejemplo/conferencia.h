//---- Definicion de la estructura de la clase conferencia (.h)
#ifndef CONFERENCIA_H
#define CONFERENCIA_H
#include <string>
#include "articulo.h"
#include <vector>
#include <iostream>

class Conferencia
{		
public:
	// Constructores, Destructor y metodos
	Conferencia(std::string Nombre,std::string FechaInicio,std::string FechaFin);
	~Conferencia();

	void agregarArticulo(std::string Titulo,Autor aut);
	void listarArticulos();

private:
	// Atributos 
	std::string nombre;
	std::string fechaInicio;
	std::string fechaFin;
	std::string ciudad;
	std::string pais;
	std::string fechaEnvio;
	std::string fechaRevision;
	std::string fechaFinal; 
	std::vector<Articulo> articulos;
};

#endif