# ifndef CHAIR_H
# define CHAIR_H

# include <vector>

# include "persona.h"

using namespace std;

class chair : public persona{
	public:
		chair(string,string,string);
		vector <string> crear_conferencia();
		string aceptar_o_rechazar();
};

# endif
