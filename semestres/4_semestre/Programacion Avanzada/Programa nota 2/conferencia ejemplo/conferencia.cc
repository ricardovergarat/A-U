//---- Implementacion de la clase conferencia (.cc)
#include "conferencia.h"
#include "autor.h"

// Constructor de la clase Conferencia
Conferencia::Conferencia(std::string Nombre,std::string FechaInicio,std::string FechaFin){
	nombre=Nombre;
}
// Destructor de la clase conferencia
Conferencia::~Conferencia(){

}
// Metodo que agrega articulos a una conferencia con el titulo y un autor
void Conferencia::agregarArticulo(std::string Titulo,Autor aut){
	
	articulos.push_back(Articulo(Titulo,aut));
}
// Metodo que lista los articulos (Titulo y autor y su grado)
void Conferencia::listarArticulos(){
	std::cout<<"-------- Lista de articulos  ----------"<<"\n";
	for (int i = 0; i < articulos.size(); ++i)
	{
		std::cout<<i<<" - "<<articulos[i].getTitulo();
		std::cout<<", "<<articulos[i].getAutor().getNombre();
		std::cout<<", "<<articulos[i].getAutor().getGrado()<<"\n";
	}
}