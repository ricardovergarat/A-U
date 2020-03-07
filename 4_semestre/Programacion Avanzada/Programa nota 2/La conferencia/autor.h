# ifndef AUTOR_H
# define AUTOR_H

# include <vector>

# include "persona.h"

using namespace std;
// el atributo notificaciones se fue usado por temas de tiempo, pero seria string diciendo si tal conferencia acepto o rechazo su articulo

class autor : public persona{
	private:
		vector <string> notificaciones;
	public:
		autor(string,string,string);
		vector <string> crear_articulo();
		void notificar(string,string);
		void mostrar_notificaciones();
		string convertir_a_final();
};

# endif
