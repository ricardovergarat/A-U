# include <iostream>
# include <vector>

# include "conferencia.h"
# include "chair.h"
# include "revisor.h"
# include "autor.h"
# include "articulo.h"

using namespace std;

conferencia::conferencia(vector <string> datos_conferencia) {
	nombre = datos_conferencia[0];
	fecha_inicio = datos_conferencia[1];
	fecha_termino = datos_conferencia[2];
	pais = datos_conferencia[3];
	ciudad = datos_conferencia[4];
}

void conferencia::mostrar_conferencia(){
	cout << "" << endl;
	cout << "Nombre: " << nombre << endl;
	cout << "Fecha de inicio: " << fecha_inicio << endl;
	cout << "Fecha de termino: " << fecha_termino << endl;
	cout << "Pais: " << pais << endl;
	cout << "Ciudad: " << ciudad << endl;
}

void conferencia::agregar_chair(chair un_chair){
	if ( los_chair.size() >= 2 ){
		cout << "La conferencia ya tiene a sus dos chair" << endl; // por que esta en el enunciado
	}else{
		los_chair.push_back(un_chair);
	}
}

void conferencia::agregar_grupo_chair(chair un_chair1, chair un_chair2){
	los_chair.push_back(un_chair1);
	los_chair.push_back(un_chair2);
}

void conferencia::mostrar_sus_chair(){
	int x = 0;
	while ( x < los_chair.size() ){
		cout << los_chair[x].get_nombre() << endl;
		x = x + 1;
	} 
}

void conferencia::agregar_revisor(revisor un_revisor){
	if ( los_revisores.size()  >= 3){
		cout << "La conferencia ya tiene a sus tres revisores" << endl; // por que esta en el enunciado
	}else{
		los_revisores.push_back(un_revisor);
	}
}

void conferencia::agregar_grupo_revisores(revisor un_revisor1, revisor un_revisor2, revisor un_revisor3){
	los_revisores.push_back(un_revisor1);
	los_revisores.push_back(un_revisor2);
	los_revisores.push_back(un_revisor3);
}

void conferencia::mostrar_sus_revisores(){
	int x = 0;
	while ( x < los_revisores.size() ){
		cout << los_revisores[x].get_nombre() << endl;
		x = x + 1;
	}
}

void conferencia::agregar_articulo(articulo un_articulo){
	articulos_resividos.push_back(un_articulo);
}

void conferencia::agregar_grupo_articulos(vector <articulo> varios_articulos, int a, int b, int c, int d, int e){
	articulos_resividos.push_back(varios_articulos[a]);
	articulos_resividos.push_back(varios_articulos[b]);
	articulos_resividos.push_back(varios_articulos[c]);
	articulos_resividos.push_back(varios_articulos[d]);
	articulos_resividos.push_back(varios_articulos[e]);
}

void conferencia::mostrar_articulos_resividos(){
	int x = 0;
	while ( x < articulos_resividos.size() ){
		articulos_resividos[x].mostrar_articulo();
		x = x + 1;
	}
}

void conferencia::agregar_articulo_final(articulo un_articulo){
	if ( un_articulo.aprobado == "FALSE" ){
		cout << "Este articulo aun no a sido aceptado en la conferencia: " << nombre << endl;
	}else{
		cout << "Su articlo a sido agregado exitosamente" << endl;
		articulos_finales.push_back(un_articulo);
	}
}

void conferencia::agregar_grupo_articulos_finales(articulo un_articulo1, articulo un_articulo2){
	articulos_finales.push_back(un_articulo1);
	articulos_finales.push_back(un_articulo2);
	// La variable "nombre" de las siguintes dos lineas son el nombre de la conferencia
	un_articulo1.los_autores[0].agregar_notificacion( "La conferencia: " + nombre + " a ACEPTADO su articulo: " + un_articulo1.get_titulo() );
	un_articulo2.los_autores[0].agregar_notificacion( "La conferencia: " + nombre + " a ACEPTADO su articulo: " + un_articulo2.get_titulo() );
}

void conferencia::mostrar_articulos_finales(){
	int x = 0;
	while ( x < articulos_finales.size() ){
		articulos_finales[x].mostrar_articulo();
		x = x + 1;
	}
}

string conferencia::get_nombre(){
	return nombre;
}