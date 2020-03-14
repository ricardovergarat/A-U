# include <iostream>

# include "persona.h"

using namespace std;

persona::persona(string _nombre, string _afiliacion, string _correo){
	nombre = _nombre;
	afiliacion = _afiliacion;
	correo = _correo;
}

void persona::mostrar_persona(){
	cout << "" << endl;
	cout << "Nombre: " << nombre << endl;
	cout << "Afiliacion: " << afiliacion << endl;
	cout << "Correo: " << correo << endl;
}

string persona::get_nombre(){
	return nombre;
}
