# ifndef INDICE_INVERTIDO
# define INDICE_INVERTIDO

# include <vector>
# include <string>

using namespace std;

class indice_invertido{
	public:
		string clave;
		vector <string> elementos;
	public:
		indice_invertido(string);
		bool coincide_clave(string);
		void agregar_elemento(string);
		string recuperar_elementos();		
};

# endif

