# ifndef AUTOR_H
# define AUTOR_H

# include <vector>

# include "persona.h"

using namespace std;
// Esta clase se hiso asi para evitar dependencia ciclica (no teniamos un vector con los articulos del autor ni retornar un articulo con el cuerpo final por dicho problema)

class autor : public persona{
	private:
		vector <string> notificaciones; // la idea no se pudo lograr para la base de datos creada en el main, es decir funciona solo en ciertas condiciones por temas de memoria
	public:
		autor(string,string,string);
		vector <string> crear_articulo();
		void agregar_notificacion(string);
		void mostrar_notificaciones();
		string convertir_a_final();
};

# endif
