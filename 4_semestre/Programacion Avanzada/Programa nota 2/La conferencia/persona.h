# ifndef PERSONA_H
# define PERSONA_H

# include <string>

using namespace std;

class persona{
	private:
		string nombre;
		string afiliacion;
		string correo;
	public:
		persona(string,string,string);
		void mostrar_persona();
		string get_nombre();
	
};

# endif
