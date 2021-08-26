# ifndef REVISOR_H
# define REVISOR_H

# include <vector>

# include "persona.h"
# include "articulo.h"

using namespace std;

class revisor : public persona{
	public:
		revisor(string,string,string);
		void comentar(articulo,int);
		void evaluar(articulo,int);
};

# endif
