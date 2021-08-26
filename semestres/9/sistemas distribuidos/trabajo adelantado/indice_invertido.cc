# include <iostream>
# include <vector>

# include "indice_invertido.h"

using namespace std;

indice_invertido::indice_invertido(string _clave){
	clave = _clave;
}

bool indice_invertido::coincide_clave(string clave_comparativa){
	if ( clave == clave_comparativa ){
		return true;
	}
	return false;
}

void indice_invertido::agregar_elemento(string nuevo_elemento){
	elementos.push_back(nuevo_elemento);
}

string indice_invertido::recuperar_elementos(){
	string sumatoria = "";
	for (int i = 0;i < elementos.size();i++){
		sumatoria = sumatoria + elementos[i] + " ";
	}
	return sumatoria;
}
