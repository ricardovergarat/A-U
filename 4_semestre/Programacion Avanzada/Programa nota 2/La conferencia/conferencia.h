# ifndef CONFERENCIA_H
# define CONFERENCIA_H

# include <vector>

# include "chair.h"
# include "revisor.h"
# include "autor.h"
# include "articulo.h"

using namespace std;

class conferencia{
	private:
		string nombre;
		string fecha_inicio;
		string fecha_termino;
		string pais;
		string ciudad;
	public:
		vector <chair> los_chair;
		vector <revisor> los_revisores;
		vector <articulo> articulos_resividos; // aqui estan todos los articulos que envien los autores
		vector <articulo> articulos_finales; // solo estan los articulos que fueron aprobados por UNO DE LOS CHAIR (no es nesesario que sean los dos)
	public:
		conferencia(vector <string>); // Lo hice asi para que fuera mas facil al momento de escribir el codigo
		void mostrar_conferencia();
		void agregar_chair(chair);
		void agregar_grupo_chair(chair,chair); // solo 2 porque asi esta en el enunciado
		void mostrar_sus_chair();
		void agregar_revisor(revisor);
		void agregar_grupo_revisores(revisor,revisor,revisor); // solo 3 porque asi esta en el enunciado
		void mostrar_sus_revisores();
		void agregar_articulo(articulo);
		void agregar_grupo_articulos(vector <articulo>,int,int,int,int,int); // solo 5 porque considere que era suficiente para la demostracion del programa
		void mostrar_articulos_resividos();
		void agregar_articulo_final(articulo);
		void agregar_grupo_articulos_finales(articulo,articulo); // solo 2 porque tambien considere que era suficiente para la demostracion del programa
		void mostrar_articulos_finales();
		string get_nombre();
	
};

# endif
