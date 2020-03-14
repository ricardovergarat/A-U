# include <iostream>
# include <vector>
# include <fstream> // para abrir archivos

# include "autor.h"

using namespace std;

bool existe_archivo(string nombre){
	char nombre_archivo[ nombre.size() ];
	int x = 0;
	while ( x < nombre.size() ){
		nombre_archivo[x] = nombre[x];
		x = x + 1;
	}
	ifstream archivo;
	archivo.open(nombre_archivo);
	if ( archivo.fail() ){
		system("cls");
		cout << "No se encontro el archivo" << endl;
		archivo.close();
		return false;
	}else{
		archivo.close();
		return true;
	}
}

string abrir_archivo(string nombre){
	char nombre_archivo[ nombre.size() ];
	int x = 0;
	while ( x < nombre.size() ){
		nombre_archivo[x] = nombre[x];
		x = x + 1;
	}
	ifstream archivo;
	archivo.open(nombre_archivo);
	string suma = "";
	string linea;
	while ( !archivo.eof() ){
		getline(archivo,linea);
		suma = suma + "\n" + linea;
	}
	archivo.close();
	return suma;
}

autor::autor(string _nombre, string _afiliacion, string _correo) : persona(_nombre,_afiliacion,_correo){
	
}

vector <string> autor::crear_articulo(){
	string titulo,resumen,cuerpo,nombre_archivo;
	cout << "Ingrese el nombre del articulo" << endl;
	getline(cin,titulo);
	cout << "Ingrese el resumen del articulo" << endl; // esto tambien podia ser con archivos pero consideraremos que el resumen no tiene mas de 4 lineas en la consola
	getline(cin,resumen);
	bool existe = false;
	while ( existe != true){ // mientras no ingrese el nombre del archivo no saldra de este ciclo (esto es por si escribe mal el nombre, no esta en el mismo directorio, etc)
		cout << "Ingrese el nombre del archivo 		ejemplo: 1.txt" << endl;
		getline(cin,nombre_archivo);
		existe = existe_archivo(nombre_archivo);
	}
	cuerpo = abrir_archivo(nombre_archivo);
	vector <string> un_articulo;
	un_articulo.push_back(titulo);
	un_articulo.push_back(resumen);
	un_articulo.push_back(cuerpo);
	return un_articulo;
}

void autor::agregar_notificacion(string notificacion){
	notificaciones.push_back(notificacion);
}

void autor::mostrar_notificaciones(){
	int x = 0;
	while ( x < notificaciones.size() ){
		cout << notificaciones[x] << endl;
		x = x + 1;
	}
	if (notificaciones.size() == 0) {
		cout << "Usted no tiene ninguna notificacion" << endl;
	}
}

string autor::convertir_a_final(){ // mientras no ingrese el nombre del archivo no saldra de este ciclo (esto es por si escribe mal el nombre, no esta en el mismo directorio, etc)
	string nombre_archivo,cuerpo;
	bool existe = false;
	while ( existe != true){
		cout << "Ingrese el nombre del archivo 		ejemplo: 1.txt" << endl;
		getline(cin,nombre_archivo);
		existe = existe_archivo(nombre_archivo);
	}
	cuerpo = abrir_archivo(nombre_archivo);
	return cuerpo;
}
