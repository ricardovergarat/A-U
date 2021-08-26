# include <iostream>
# include <math.h> // para convertir a numero

# include "revisor.h"
# include "articulo.h"

using namespace std;

bool es_numero2(string dato){ // esta funcion te dice si todo un string es un numero (aun no funciona para numeros negativos ni decimales)
	int x = 0;
	while (x < dato.size()) {
		if (isdigit(dato[x]) == 0) {
			return false;
		}
		x = x + 1;
	}
	return true;
}

int convertir_a_numero2(string dato){ // esta funcion convierte un string en numero (SIEMPRE que invoque esta funcion le daremos un numero, para asegurarnos de esto existe la funcion anteior)
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

int pedir_nota(){
	cout << "Ingrese alguna opcion" << endl;
	string opcion_string;
	getline(cin, opcion_string);
	bool numero = es_numero2(opcion_string);
	if (numero == true) {
		int opcion = convertir_a_numero2(opcion_string);
		if (1 <= opcion && opcion <= 5) {
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

revisor::revisor(string _nombre, string _afiliacion, string _correo) : persona(_nombre, _afiliacion, _correo){
	
}

void revisor::comentar(articulo un_articulo, int indice){
	string comentario;
	cout << "Ingrese el comentario" << endl;
	getline(cin,comentario);
	un_articulo.comentarios[indice] = comentario;
}

void revisor::evaluar(articulo un_articulo, int indice){
	string una_nota;
	int nota = 0;
	while ( nota < 1 ){
		cout << "Ingrese la nota (solo notas enteras entre 1 y 5)" << endl;
		nota = pedir_nota();
	}
	un_articulo.notas[indice] = nota;
}

