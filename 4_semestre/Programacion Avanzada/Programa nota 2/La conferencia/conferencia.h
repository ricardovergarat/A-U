# ifndef CONFERENCIA_H
# define CONFERENCIA_H

# include <vector>

# include "chair.h"
# include "revisor.h"
# include "autor.h"
# include "articulo.h"

using namespace std;
// creo que todos los atributos puede ser privados debido a el nuevo sistema implementado, pero se dejo en publico para eviat algunos cambio en el codigo principal

class conferencia{
	public:
		string nombre;
		string fecha_inicio;
		string fecha_termino;
		string pais;
		string ciudad;
		vector <chair> los_chair;
		vector <revisor> los_revisores;
		vector <articulo> articulos_resividos;
		vector <articulo> articulos_finales;
	public:
		conferencia(string,string,string,string,string);
		void mostrar_conferencia();
		void agregar_chair(chair);
		void agregar_grupo_chair(chair,chair);
		void mostrar_sus_chair();
		void agregar_revisor(revisor);
		void agregar_grupo_revisores(revisor,revisor,revisor);
		void mostrar_sus_revisores();
		void agregar_articulo(articulo);
		void agregar_grupo_articulos(vector <articulo>,int,int,int,int,int);
		void mostrar_articulos_resividos();
		void agregar_articulo_final(articulo);
		void agregar_grupo_articulos_finales(articulo,articulo);
		void mostrar_articulos_finales();
	
};

# endif
