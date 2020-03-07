# ifndef REVISOR_H
# define REVISOR_H

# include <vector>

# include "persona.h"
# include "articulo.h"

using namespace std;

class revisor : public persona{
	public:
		revisor(string,string,string);
		string comentar();
		int evaluar();
};

# endif
