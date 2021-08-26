//---- Implementacion de la clase articulo (.cc)
#include "articulo.h"
// Constructor 
Articulo::Articulo(std::string Titulo,Autor aut){
	titulo=Titulo;
	autor=aut;
}
// Destructor
Articulo::~Articulo(){
	
}
// Metodo que retorna el titulo de un articulo
std::string Articulo::getTitulo(){
	return titulo;
}
// Metodo que retorna el autor de una articulo
Autor Articulo::getAutor(){
	return autor;
}