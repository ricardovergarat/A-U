# include <iostream>
# include <vector>
# include <math.h> // para convertir a numero

# include "chair.h"
# include "autor.h"
# include "articulo.h"

using namespace std;

bool es_numero1(string dato){ // esta funcion te dice si todo un string es un numero (aun no funciona para numeros negativos ni decimales)
	int x = 0;
	while (x < dato.size()) {
		if (isdigit(dato[x]) == 0) {
			return false;
		}
		x = x + 1;
	}
	return true;
}

int convertir_a_numero1(string dato){ // esta funcion convierte un string en numero (SIEMPRE que invoque esta funcion le daremos un numero, para asegurarnos de esto existe la funcion anteior)
	int x = 0;
	int suma = 0;
	while (x < dato.size()) {
		int potencia = (dato.size() - 1) - x;
		switch (dato[x]) {
		case '0': suma = suma + 0 * pow(10, potencia); break;
		case '1': suma = suma + 1 * pow(10, potencia); break;
		case '2': suma = suma + 2 * pow(10, potencia); break;
		case '3': suma = suma + 3 * pow(10, potencia); break;
		case '4': suma = suma + 4 * pow(10, potencia); break;
		case '5': suma = suma + 5 * pow(10, potencia); break;
		case '6': suma = suma + 6 * pow(10, potencia); break;
		case '7': suma = suma + 7 * pow(10, potencia); break;
		case '8': suma = suma + 8 * pow(10, potencia); break;
		case '9': suma = suma + 9 * pow(10, potencia); break;
		}
		x = x + 1;
	}
	return suma;
}

int pedir_numero1(int maximo){
	cout << "Ingrese alguna opcion" << endl;
	string opcion_string;
	getline(cin, opcion_string);
	bool numero = es_numero1(opcion_string);
	if (numero == true) {
		int opcion = convertir_a_numero1(opcion_string);
		if (1 <= opcion && opcion <= maximo) {
			return opcion;
		}
		else {
			system("cls");
			cout << "No se puede poner esa nota" << endl;
			return -1;
		}
	}
	else {
		system("cls");
		cout << "Ingreso algo no valido" << endl;
		return -1;
	}
}

chair::chair(string _nombre, string _afiliacion, string _correo) : persona(_nombre,_afiliacion,_correo){
	
}

vector <string> chair::crear_conferencia(){
	string nombre,fecha_inicio,fecha_termino,pais,ciudad,nombre_revisor;
	cout << "Ingrese el nombre de la conferencia" << endl;
	getline(cin,nombre);
	cout << "Ingrese la fecha de inicio 	ejemplo: 23-03-2020" << endl;
	getline(cin,fecha_inicio);
	cout << "Ingrese la fecha de termino 	ejemplo:29-03-2020" << endl;
	getline(cin,fecha_termino);
	cout << "Ingrese el pais" << endl;
	getline(cin,pais);
	cout << "Ingrese la ciudad" << endl;
	getline(cin,ciudad);
	cout << "Ingrese el nombre de un revisor" << endl;
	getline(cin,nombre_revisor);
	vector <string> una_conferencia;
	una_conferencia.push_back(nombre);
	una_conferencia.push_back(fecha_inicio);
	una_conferencia.push_back(fecha_termino);
	una_conferencia.push_back(pais);
	una_conferencia.push_back(ciudad);
	una_conferencia.push_back(nombre_revisor);
	return una_conferencia;
}

void chair::aceptar_o_rechazar(articulo un_articulo,string nombre_conferencia){
	bool numero;
	int opcion = 0;
	while ( opcion < 1 ){
		cout << "1- Aceptar articulo" << endl;
		cout << "2- Rechazar articulo" << endl;
		opcion = pedir_numero1(2);
	}
	if (opcion == 1) {
		un_articulo.aprobado = "FALSE";
		un_articulo.los_autores[0].agregar_notificacion( "La conferencia: " + nombre_conferencia + " a RECHAZADO su articulo: " + un_articulo.get_titulo() ); // aqui notificamos al autor principal
	}
	else {
		un_articulo.aprobado = "TRUE";
		un_articulo.los_autores[0].agregar_notificacion("La conferencia: " + nombre_conferencia + " a ACEPTADO su articulo: " + un_articulo.get_titulo()); // aqui notificamos al autor principal
	}
}
