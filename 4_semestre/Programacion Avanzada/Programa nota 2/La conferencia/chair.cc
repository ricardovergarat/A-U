# include <iostream>
# include <vector>
# include <math.h> // para convertir a numero

# include "chair.h"

using namespace std;

bool es_numero2(string dato){
	int x = 0;
	while ( x < dato.size() ){
		if ( isdigit(dato[x]) == 0 ){
			return false;
		}
		x = x + 1;
	}
	return true;
}

int convertir_a_numero2(string dato){
	int x = 0;
	int suma = 0;
	while ( x < dato.size() ){
		int potencia = ( dato.size() - 1 ) - x;
		switch (dato[x]){
			case '0': suma = suma + 0 * pow(10,potencia); break;
			case '1': suma = suma + 1 * pow(10,potencia); break;
			case '2': suma = suma + 2 * pow(10,potencia); break;
			case '3': suma = suma + 3 * pow(10,potencia); break;
			case '4': suma = suma + 4 * pow(10,potencia); break;
			case '5': suma = suma + 5 * pow(10,potencia); break;
			case '6': suma = suma + 6 * pow(10,potencia); break;
			case '7': suma = suma + 7 * pow(10,potencia); break;
			case '8': suma = suma + 8 * pow(10,potencia); break;
			case '9': suma = suma + 9 * pow(10,potencia); break;
		}
		x = x + 1;
	}
	int numero = suma;
	return numero;
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

string chair::aceptar_o_rechazar(){
	string opcion;
	bool numero;
	int x = 0;
	while ( x < 1 ){
		cout << "1- Aceptar articulo" << endl;
		cout << "2- Rechazar articulo" << endl;
		getline(cin,opcion);
		numero = es_numero2(opcion);
		if ( numero == true ){
			int elegido = convertir_a_numero2(opcion);
			switch (elegido){
				case 1: return "TRUE";
				case 2: return "FALSE";
				default: system("cls"); cout << "Esa opcion no existe" << endl;
			}
		}else{
			system("cls");
			cout << "Ingreso algo no valido" << endl;
		}
	}
}
