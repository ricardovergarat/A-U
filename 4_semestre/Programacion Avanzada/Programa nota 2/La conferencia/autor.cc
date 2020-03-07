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
	cout << "Ingrese el resumen del articulo" << endl;
	getline(cin,resumen);
	bool existe = false;
	while ( existe != true){
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

void autor::notificar(string nombre_conferencia,string desicion){
	if ( desicion == "RECHAZADO"){
		string mensaje = "La conferencia " + nombre_conferencia + " a RECHAZADO su articulo";
		notificaciones.push_back(mensaje);
	}else{
		string mensaje = "La conferencia " + nombre_conferencia + " a ACEPTADO su articulo";
		notificaciones.push_back(mensaje);
	}
}

void autor::mostrar_notificaciones(){
	int x = 0;
	while ( x < notificaciones.size() ){
		cout << notificaciones[x] << endl;
		x = x + 1;
	}
}

string autor::convertir_a_final(){
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
