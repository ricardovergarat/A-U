# ifndef CHAIR_H
# define CHAIR_H

# include <vector>

# include "persona.h"
# include "articulo.h"

using namespace std;

// Esta clase se hiso asi para evitar dependencia ciclica (no podiamos retorna un dato de tipo conferencia por dicho problema)

class chair : public persona{
	public:
		chair(string,string,string);
		vector <string> crear_conferencia();
		void aceptar_o_rechazar(articulo,string);
};

# endif
