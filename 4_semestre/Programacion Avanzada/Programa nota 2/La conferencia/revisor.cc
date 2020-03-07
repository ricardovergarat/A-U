# include <iostream>
# include <math.h> // para convertir a numero

# include "revisor.h"
# include "articulo.h"

using namespace std;

bool es_numero(string dato){
	int x = 0;
	while ( x < dato.size() ){
		if ( isdigit(dato[x]) == 0 ){
			return false;
		}
		x = x + 1;
	}
	return true;
}

int convertir_a_numero(string dato){
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

revisor::revisor(string _nombre, string _afiliacion, string _correo) : persona(_nombre, _afiliacion, _correo){
	
}

string revisor::comentar(){
	string comentario;
	cout << "Ingrese el comentario" << endl;
	getline(cin,comentario);
	return comentario;
}


int revisor::evaluar(){
	string una_nota;
	int x = 0;
	while ( x < 1 ){
		cout << "Ingrese la nota (solo notas enteras entre 0 y 5)" << endl;
		getline(cin,una_nota);
		bool numero = es_numero(una_nota);
		if ( numero == true ){
			int nota = convertir_a_numero(una_nota);
			switch (nota){
				case 1: return 1;
				case 2: return 2;
				case 3: return 3;
				case 4: return 4;
				case 5: return 5;
				default: system("cls"); cout << "No se puede poner esa nota" << endl;
			}
		}else{
			system("cls");
			cout << "Ingreso algo no valido" << endl;
		}
	}
}

