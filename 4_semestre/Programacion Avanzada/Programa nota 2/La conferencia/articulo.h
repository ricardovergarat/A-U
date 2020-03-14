# ifndef ARTICULO_H
# define ARTICULO_H

# include <vector>

# include "autor.h"

using namespace std;
// la fecha de entrega no fue incluida por que fue dificil recuperar la fecha desde el sistema operativo, se dificulto debido al hacerlo en multiples sistemas operativos

class articulo{
	private:
		string titulo;
		string resumen;
		string cuerpo;
	public:
		vector <string> comentarios; // en publico para cuando comentemos
		vector <int> notas; // en para cuando evaluemos
		string aprobado;   // Este atributo tomas false o true y dice si se APROBO este articulo  // en publico porque queda mas corto el codigo simplemente
		vector <autor> los_autores; // en public porque nesesitaremos aceder constantemnte a este atributo   // consideraremos SIEMPRE que el autor en indice 0 es el autor principal (cuando un autor crea un articulo es agregado instantaneamente como autor principal)  
	public:
		articulo(string,string,string,vector <string>,vector <int>,string);
		void mostrar_articulo();
		void agregar_autor(autor);
		void agregar_grupo_autores(autor,autor,autor);
		void mostrar_autores();
		void mostrar_autor_principal();
		void version_final(string); // esto conviente el atributo cuerpo a el cuerpo completo, es decir el articulo final
		string get_titulo();
		
};

# endif
