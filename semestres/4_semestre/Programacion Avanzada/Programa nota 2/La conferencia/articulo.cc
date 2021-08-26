# include <iostream>
# include <vector>

# include "articulo.h"

using namespace std;

articulo::articulo(string _titulo, string _resumen, string _cuerpo, vector <string> _comentarios,vector <int> _notas, string _aprobado){
	titulo = _titulo;
	resumen = _resumen;
	cuerpo = _cuerpo;
	comentarios = _comentarios;
	notas = _notas;
	aprobado = _aprobado;
}

void articulo::mostrar_articulo(){
	cout << "Titulo: " << titulo << endl;
	cout << "Resumen: " << resumen << endl;
	cout << "Cuerpo: " << cuerpo << endl;
	int x = 0;
	while ( x < comentarios.size() ){
		cout << "Comentario " << x + 1 << ":" << endl;
		cout << comentarios[x] << endl;
		cout << "Nota " << x + 1 << ":" << notas[x] << endl;
		x = x + 1;
	}
	cout << "Nota promedio: " << ( ( notas[0] + notas[1] + notas[2] ) / 3 ) << endl;
	cout << "Aprobado: " << aprobado << endl;
}

void articulo::agregar_autor(autor un_autor){
	los_autores.push_back(un_autor);
}

void articulo::agregar_grupo_autores(autor a1, autor a2, autor a3){
	los_autores.push_back(a1);
	los_autores.push_back(a2);
	los_autores.push_back(a3);
}

void articulo::mostrar_autores(){
	int x = 0;
	while ( x < los_autores.size() ){
		cout << los_autores[x].get_nombre() << endl;
		x = x + 1;
	}
}

void articulo::mostrar_autor_principal(){
	cout << los_autores[0].get_nombre() << endl;
}

void articulo::version_final(string cuerpo_final){
	cuerpo = cuerpo_final;
}

string articulo::get_titulo() {
	return titulo;
}

