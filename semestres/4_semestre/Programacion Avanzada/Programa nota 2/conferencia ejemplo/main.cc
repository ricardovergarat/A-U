//---- Archivo principal
#include <iostream>
#include "conferencia.h"


int main(int argc, char const *argv[])
{
	//Creamos una instancia de la clase Conferencia con su nombre y otros atributos
	Conferencia conf1("International Science Computing","20.02.2020","28.02.2020");
	// Agregamos articulos a la conferencia con su titulo y autor y otros atributos
	conf1.agregarArticulo(" Genetic Algorithm in TSP",Autor("Pedro","UCM","pedro@gmail.com","Mg"));
	conf1.agregarArticulo(" Neural Network Applied in Medicine",Autor("Marcelo","UCM","marcelo@gmail.com","PhD"));
	conf1.agregarArticulo(" Image Recognition agro industrial",Autor("Natalia","UCM","nata@gmail.com","Mg"));
	conf1.listarArticulos();
	return 0;
}