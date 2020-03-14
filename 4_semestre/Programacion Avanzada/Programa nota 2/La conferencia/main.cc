# include <iostream>
# include <vector>
# include <math.h> // para convertir a numero
# include <string.h> // para comparar string
# include <fstream> // para abrir archivos

# include "conferencia.h"
# include "chair.h"
# include "revisor.h"
# include "autor.h"
# include "articulo.h"

using namespace std;

bool es_numero(string dato){
	int x = 0;
	while (x < dato.size()) {
		if (isdigit(dato[x]) == 0) {
			return false;
		}
		x = x + 1;
	}
	return true;
}

int convertir_a_numero(string dato){ 
	int x = 0;
	int suma = 0;
	while (x < dato.size()) {
		int potencia = (dato.size() - 1) - x;
		switch (dato[x]) {
		case '0': suma = suma + 0 * pow(10, potencia); break;
		case '1': suma = suma + 1 * pow(10, potencia); break;
		case '2': suma = suma + 2 * pow(10, potencia); break;
		case '3': suma = suma + 3 * pow(10, potencia); break;
		case '4': suma = suma + 4 * pow(10, potencia); break;
		case '5': suma = suma + 5 * pow(10, potencia); break;
		case '6': suma = suma + 6 * pow(10, potencia); break;
		case '7': suma = suma + 7 * pow(10, potencia); break;
		case '8': suma = suma + 8 * pow(10, potencia); break;
		case '9': suma = suma + 9 * pow(10, potencia); break;
		}
		x = x + 1;
	}
	return suma;
}

int pedir_numero(int maximo){
	cout << "Ingrese alguna opcion" << endl;
	string opcion_string;
	getline(cin, opcion_string);
	bool numero = es_numero(opcion_string);
	if (numero == true) {
		int opcion = convertir_a_numero(opcion_string);
		if (1 <= opcion && opcion <= maximo) {
			return opcion;
		}
		else {
			system("cls");
			cout << "Ingreso una opcion que no existe" << endl;
			return -1;
		}
	}
	else {
		system("cls");
		cout << "Ingreso algo no valido" << endl;
		return -1;
	}
}

vector <string> comentarios_falsos(string comentario1, string comentario2, string comentario3){ // usaremos esta funcion para poner facilmente los comentarios en los articulos para la base de datos
	vector <string > comentarios;
	comentarios.push_back(comentario1);
	comentarios.push_back(comentario2);
	comentarios.push_back(comentario3);
	return comentarios;
}

vector <int> notas_falsas(int nota1, int nota2, int nota3){ // Usaremos esta funcion para poner las notas de los articulos mas facilmente
	vector <int> notas;
	notas.push_back(nota1);
	notas.push_back(nota2);
	notas.push_back(nota3);
	return notas;
}

vector <articulo> articulos_falsos(vector <autor>& los_autores){ // crearemos todos los articulos falsos para poner en la base de datos
	// creamos 3 vectors, uno para almacenar todos los articulos y retornalos
	// uno para tener comentarios ya que supondremos que cada articulo tiene 3 comentarios al tener 3 revisores, es decir cada revisor puede comentar en el articulo
	// y uno mas para la misma logica pero para las notas del articulo
	vector <articulo> varios_articulos;
	vector <string> comentarios;
	vector <int> notas;

	// los cuerpo de los texto son cortos solo para tener algo en la base de datos, si creamos un articulo con el menu podemos obtener todo el texto de un archivo
	// agregaremos titulo,resumen,cuerpo,comentarios,notas y si fue aprobado o no 

	comentarios = comentarios_falsos("me gustan los piratas", "yo vi los piratas del caribe", "no entendi un carajo pero el autor me pago");
	notas = notas_falsas(3, 5, 3);
	articulo ar("piratas", "texto de piratas", "los piratas eran ladrones hace muchos años", comentarios, notas, "TRUE");
	ar.agregar_grupo_autores(los_autores[0], los_autores[1], los_autores[2]);
	varios_articulos.push_back(ar);

	comentarios = comentarios_falsos("solo me gusta dragon ball", "origen no muy bien explicado", "sus datos estan bien explicados");
	notas = notas_falsas(2, 5, 3);
	articulo ar1("anime", "series animadas", "forma de entretenimiento creada en japon", comentarios, notas, "TRUE");
	ar1.agregar_grupo_autores(los_autores[3], los_autores[5], los_autores[2]);
	varios_articulos.push_back(ar1);

	comentarios = comentarios_falsos("ahora entiendo las peliculas", "alfin entendi como sobrevir", "con razon todos siempre mueren");
	notas = notas_falsas(4, 2, 1);
	articulo ar2("zombies", "habla los tipos de zombies", "un tipo de mostruo dificil de matar", comentarios, notas, "FALSE");
	ar2.agregar_grupo_autores(los_autores[0], los_autores[2], los_autores[4]);
	varios_articulos.push_back(ar2);

	comentarios = comentarios_falsos("no puedo parglo", "es muy bueno", "falta ortografia");
	notas = notas_falsas(2, 5, 2);
	articulo ar3("netflix", "aplicacion para videos", "esta aplicaion tiene muchas pelicuas y series", comentarios, notas, "TRUE");
	ar3.agregar_grupo_autores(los_autores[1], los_autores[5], los_autores[0]);
	varios_articulos.push_back(ar3);

	comentarios = comentarios_falsos("es malo para los jovenes", "tiene muchos insultos", "los autores no saben escribir");
	notas = notas_falsas(3, 1, 1);
	articulo ar4("league of legends", "es un juego", "es juego creado en el 2010", comentarios, notas, "TRUE");
	ar4.agregar_grupo_autores(los_autores[2], los_autores[4], los_autores[5]);
	varios_articulos.push_back(ar4);

	comentarios = comentarios_falsos("no esta bien explicado", "no explica origen", "faltan imagenes");
	notas = notas_falsas(1, 5, 3);
	articulo ar5("idiomas", "la forma de comunicarse", "existe una infinidad de idiomas y se pueden crear", comentarios, notas, "TRUE");
	ar5.agregar_grupo_autores(los_autores[3], los_autores[1], los_autores[4]);
	varios_articulos.push_back(ar5);

	comentarios = comentarios_falsos("no queda claro el origen", "faltan referencias", "no explica como se crean");
	notas = notas_falsas(2, 3, 3);
	articulo ar6("peliculas", "videos de larga duracion", "video que cuentan historia por medio de imagenes", comentarios, notas, "TRUE");
	ar6.agregar_grupo_autores(los_autores[4], los_autores[1], los_autores[3]);
	varios_articulos.push_back(ar6);

	comentarios = comentarios_falsos("no explica que es", "no menciona referencias", "faltan ejemplos");
	notas = notas_falsas(1, 4, 5);
	articulo ar7("series", "video de duracion media", "cuentas una historia atravez de varios capitulos", comentarios, notas, "FALSE");
	ar7.agregar_grupo_autores(los_autores[5], los_autores[4], los_autores[3]);
	varios_articulos.push_back(ar7);

	comentarios = comentarios_falsos("no quedan claras las epocas", "no se extiende el capitulo 5", "faltan imagenes");
	notas = notas_falsas(2, 4, 5);
	articulo ar8("the big bang theory", "teoria del origen del universo", "teoria que propone una explosion a bilones de años", comentarios, notas, "TRUE");
	ar8.agregar_grupo_autores(los_autores[3], los_autores[4], los_autores[5]);
	varios_articulos.push_back(ar8);

	comentarios = comentarios_falsos("no menciona a los espartanos", "odio este articulo", "por estos articulos canlan la psu");
	notas = notas_falsas(1, 4, 4);
	articulo ar9("historia", "tiene la historia del mundo", "la historia comezo a ser reistrada en el año ...", comentarios, notas, "FALSE");
	ar9.agregar_grupo_autores(los_autores[5], los_autores[0], los_autores[3]);
	varios_articulos.push_back(ar9);

	comentarios = comentarios_falsos("explica bien los numeros", "es muy basico", "no explica los cardinales");
	notas = notas_falsas(1, 1, 1);
	articulo ar10("matematicas", "introduce a la matematica", "es el uso de numeros para resolver problemas", comentarios, notas, "TRUE");
	ar10.agregar_grupo_autores(los_autores[1], los_autores[3], los_autores[4]);
	varios_articulos.push_back(ar10);

	comentarios = comentarios_falsos("no meciona los idomas", "no explica origen idomas", "no explica importancia");
	notas = notas_falsas(4, 5, 3);
	articulo ar11("lenguas muertas", "historia idomas que ya no se hablan", "esto se debe a que quien conocen el idoma no pudieron eneñarlo", comentarios, notas, "TRUE");
	ar11.agregar_grupo_autores(los_autores[4], los_autores[0], los_autores[1]);
	varios_articulos.push_back(ar11);

	comentarios = comentarios_falsos("faltan dibijos", "abusa de los ejemplos", "no muy avanzado");
	notas = notas_falsas(3, 5, 1);
	articulo ar12("codigo binario", "explica funcionamiento de los bits", "los aparatos funcionan con ausencia o presencia de electricidad", comentarios, notas, "FALSE");
	ar12.agregar_grupo_autores(los_autores[2], los_autores[1], los_autores[4]);
	varios_articulos.push_back(ar12);

	comentarios = comentarios_falsos("falta mas teoria", "solo explica autos mecanicos", "no explica importancia");
	notas = notas_falsas(1, 5, 4);
	articulo ar13("cueso de conducion", "explica reglas para conducir", "este sistema fue creada para previnir las siguies situaciones", comentarios, notas, "TRUE");
	ar13.agregar_grupo_autores(los_autores[0], los_autores[5], los_autores[3]);
	varios_articulos.push_back(ar13);

	comentarios = comentarios_falsos("sub grupos no claros", "faltan estadisticas", "explica bien los porque");
	notas = notas_falsas(2, 5, 4);
	articulo ar14("tipos de aprendizaje", "explica forma de apreneder", "la capacidad de aprender se divide en grupo", comentarios, notas, "FALSE");
	ar14.agregar_grupo_autores(los_autores[5], los_autores[3], los_autores[0]);
	varios_articulos.push_back(ar14);

	comentarios = comentarios_falsos("hace buen uso de los ejemplos", "falta tecnicas", "es muy corto el articulo");
	notas = notas_falsas(2, 5, 2);
	articulo ar15("expresionn oral", "explica tecnicas de comunicacion", "la comunicacion tiene la finalidad de expresar", comentarios, notas, "TRUE");
	ar15.agregar_grupo_autores(los_autores[4], los_autores[0], los_autores[2]);
	varios_articulos.push_back(ar15);

	comentarios = comentarios_falsos("no hay ejemplos", "es muy avanzado para principiantes", "falta referencias");
	notas = notas_falsas(1, 3, 5);
	articulo ar16("paginas web", "mestra tecnicas de desarrolo web", "el desarrolo se basa en la ceracion de objetos en lenguajes", comentarios, notas, "FALSE");
	ar16.agregar_grupo_autores(los_autores[3], los_autores[2], los_autores[1]);
	varios_articulos.push_back(ar16);

	comentarios = comentarios_falsos("no entendi nada", "por esto estudie lenguaje", "apenas se entendio");
	notas = notas_falsas(2, 3, 4);
	articulo ar17("matrices", "introduce al algebra lineal", "son un conjunto de sistema de incognitas", comentarios, notas, "TRUE");
	ar17.agregar_grupo_autores(los_autores[5], los_autores[2], los_autores[3]);
	varios_articulos.push_back(ar17);

	comentarios = comentarios_falsos("tiene buenas imagens", "es muy largo", "no estan bien divididos los capitulos");
	notas = notas_falsas(3, 4, 3);
	articulo ar18("calculo diferencial", "introdice al calculo", "explicaremos primero el teorema fundamentas del calulo", comentarios, notas, "TRUE");
	ar18.agregar_grupo_autores(los_autores[0], los_autores[4], los_autores[1]);
	varios_articulos.push_back(ar18);

	// agregamos todos los datos del los articulo, entonces retornaremos el vector con todos estos articulos

	return varios_articulos;
}

vector <string> abrir_archivo_vector(string nombre) { // esta funcion regresa cada linea de archivo como elemento en un vector
	char nombre_archivo[nombre.size()];
	int x = 0;
	while (x < nombre.size()) { // rellenamos el char 
		nombre_archivo[x] = nombre[x];
		x = x + 1;
	}
	ifstream archivo;
	//cout << "nombre string: " << nombre << " tamaño: " << nombre.size() << endl;
	//cout << "nombre char: " << nombre_archivo << endl;
	archivo.open(nombre_archivo); // debe ser pasado como char por eso el while anterior
	vector <string> texto;
	string linea;
	while (!archivo.eof()) {
		getline(archivo, linea);
		texto.push_back(linea); // agregamos la linea recuperada al vector
	}
	archivo.close();
	return texto; // retornamos el vector con cada linea del archivo
}

conferencia crear_conferencia_falsa(string nombre_archivo, vector <articulo>& los_articulos) { // esta funcion creara las conferencias que esten en archivo
	vector <string> datos_conferencia = abrir_archivo_vector(nombre_archivo);
	conferencia una_conferencia(datos_conferencia);
	chair un_chair_1(datos_conferencia[5], datos_conferencia[6], datos_conferencia[7]);
	chair un_chair_2(datos_conferencia[8], datos_conferencia[9], datos_conferencia[10]);
	revisor un_revisor_1(datos_conferencia[11], datos_conferencia[12], datos_conferencia[13]);
	revisor un_revisor_2(datos_conferencia[14], datos_conferencia[15], datos_conferencia[16]);
	revisor un_revisor_3(datos_conferencia[17], datos_conferencia[18], datos_conferencia[19]);
	una_conferencia.agregar_grupo_chair(un_chair_1, un_chair_2);
	una_conferencia.agregar_grupo_revisores(un_revisor_1, un_revisor_2, un_revisor_3);
	int a = convertir_a_numero(datos_conferencia[20]); // indice del primer articulo que se enviara a la conferencia
	int b = convertir_a_numero(datos_conferencia[21]); // indice del segundo articulo que se enviara a la conferencia
	int c = convertir_a_numero(datos_conferencia[22]); // indice del tercer articulo que se enviara a la conferencia
	int d = convertir_a_numero(datos_conferencia[23]); // indice del cuarto articulo que se enviara a la conferencia
	int e = convertir_a_numero(datos_conferencia[24]); // indice del quinto articulo que se enviara a la conferencia
	una_conferencia.agregar_grupo_articulos(los_articulos, a, b, c, d, e);
	int f = convertir_a_numero(datos_conferencia[25]); // indice del primer articulo final que se enviara a la conferencia
	int g = convertir_a_numero(datos_conferencia[26]); // indice del segundo articulo final que se enviara a la conferencia
	una_conferencia.agregar_grupo_articulos_finales(los_articulos[f], los_articulos[g]);
	return una_conferencia;
}

void agregar_conferencias_falsas(vector <conferencia>& lista){ // Agregaremos las conferencias del archivo en la base de datos

	// crear autores
	autor a("Python", "En .py", "python@gmail.com");
	autor a1("C", "En .C", "Mi_antecesor_es_B@gmail.com");
	autor a2("C++", "En .CPP", "evolucion@gmail.com");
	autor a3("C#", "En visual studio", "Muy_lento@gmail.com");
	autor a4("Java", "i dont know", "Proximamente@gmail.com");
	autor a5("Matlab", "En .mat", "Matematica@gmail.com");

	// pondremos los autores en un vector para agregarlos a los articulos que crearemos en las siguienes lineas
	vector <autor> los_autores;
	los_autores.push_back(a);
	los_autores.push_back(a1);
	los_autores.push_back(a2);
	los_autores.push_back(a3);
	los_autores.push_back(a4);
	los_autores.push_back(a5);

	vector <articulo> los_articulos;
	los_articulos = articulos_falsos(los_autores); // tendremos los articulos en este vector para hacer las cosas mas faciles

	vector <string> n_conferencias = abrir_archivo_vector("z.txt"); // por algun motivo no permite el nombre datos.txt (el codigo fue probado en el pc de un amigo y si lo permitio, si a usted no le funciona le sugiero descomentar la linas 225 y 226 para ver el problema y si le encontro el error debe ser facil su corecion)
	int x = 0;
	while ( x < n_conferencias.size() ){ // aqui agregamos todas las conferencias que esten en el archivo z.txt (este deberia ser datos.txt pero ya mencione el problema dos lineas atras)
		conferencia una_conferencia = crear_conferencia_falsa(n_conferencias[x], los_articulos);
		lista.push_back(una_conferencia);
		x = x + 1;
	}
}

vector <string> crear_usuario() {
	// esto simula cuando una persona ingresa una cuenta, pero en lugar de pedir nombre de usario y comtraseña pide nombre,afiliacion y correo
	string nombre, afiliacion, correo;
	cout << "Ingrese su nombre" << endl;
	getline(cin, nombre);
	cout << "Ingrese su afiliacion" << endl;
	getline(cin, afiliacion);
	cout << "Ingrese su correo" << endl;
	getline(cin, correo);
	vector <string> usuario;
	usuario.push_back(nombre);
	usuario.push_back(afiliacion);
	usuario.push_back(correo);
	return usuario;
}

void actualizar_usuario(vector <conferencia>& lista, int tipo_usuario, vector <string> usuario) {
	// esta funcion esta por que para AGREGAR chair,revisor o autor solo pide nombre, entonces si el usuario que ingresa fue puesto en alguna conferencia se le 
	// ACTUALIZARAN sus datos, es decir su afiliacion y correo, este sistema se hizo asi por lo otros usuarios no nesesariamente saben su afiliacion y correo
	// tambien si el usario cambio su afiliacion o correo esta funcion actualizara los daots en todas las conferencias en las que participe
	int x = 0;
	while (x < lista.size()) {
		if (tipo_usuario == 1) {
			int y = 0;
			while (y < lista[x].los_chair.size()) {
				if (usuario[0] == lista[x].los_chair[y].get_nombre()) {
					chair nuevo_chair(usuario[0], usuario[1], usuario[2]);
					lista[x].los_chair[y] = nuevo_chair;
					break;
				}
				y = y + 1;
			}
		}
		if (tipo_usuario == 2) {
			int y = 0;
			while (y < lista[x].los_revisores.size()) {
				if (usuario[0] == lista[x].los_revisores[y].get_nombre()) {
					revisor nuevo_revisor(usuario[0], usuario[1], usuario[2]);
					lista[x].los_revisores[y] = nuevo_revisor;
					break;
				}
				y = y + 1;
			}
		}
		if (tipo_usuario == 3) {
			int y = 0;
			while (y < lista[x].articulos_resividos.size()) {
				int z = 0;
				while (z < lista[x].articulos_resividos[y].los_autores.size()) {
					if (usuario[0] == lista[x].articulos_resividos[y].los_autores[z].get_nombre()) {
						autor nuevo_autor(usuario[0], usuario[1], usuario[2]);
						lista[x].articulos_resividos[y].los_autores[z] = nuevo_autor;
						break;
					}
					z = z + 1;
				}
				y = y + 1;
			}
		}

		x = x + 1;
	}
}

bool pertenece_conferencia(conferencia una_conferencia, int tipo_usuario, string nombre) { // permite determinar si un usario pertenece a una conferencias expesifica
	// 1 para chair
	// 2 para revisor
	// 3 para autor
	if (tipo_usuario == 1) {
		int x = 0;
		while (x < una_conferencia.los_chair.size()) {
			if (nombre.compare(una_conferencia.los_chair[x].get_nombre()) == 0) {
				return true;
			}
			x = x + 1;
		}
		return false;
	}
	if (tipo_usuario == 2) {
		int x = 0;
		while (x < una_conferencia.los_revisores.size()) {
			if (nombre.compare(una_conferencia.los_revisores[x].get_nombre()) == 0) {
				return true;
			}
			x = x + 1;
		}
		return false;
	}
	if (tipo_usuario == 3) {
		int x = 0;
		while (x < una_conferencia.articulos_finales.size()) {
			int y = 0;
			while (y < una_conferencia.articulos_finales[x].los_autores.size()) {
				if (nombre.compare(una_conferencia.articulos_finales[x].los_autores[y].get_nombre()) == 0) {
					return true;
				}
				y = y + 1;
			}
			x = x + 1;
		}
		return false;
	}
}

void mostrar_todas_las_conferencias(vector <conferencia>& lista) {
	int x = 0;
	while (x < lista.size()) {
		cout << endl;
		lista[x].mostrar_conferencia();
		x = x + 1;
	}
}

void mostrar_mis_conferencias(vector <conferencia>& lista, int tipo_usuario, string nombre) {
	// mostrara las conferencias dependiendo del tipo de usuario, y se mostrara si el NOMBRE aparece en una conferencia 
	// 1 para chair
	// 2 para revisor
	// 3 para autor
	int x = 0;
	while (x < lista.size()) {
		bool pertenece = pertenece_conferencia(lista[x], tipo_usuario, nombre);
		if (pertenece == true) {
			cout << lista[x].get_nombre() << endl;
		}
		x = x + 1;
	}
}

int selecion_conferencia(vector <conferencia>& lista, string nombre, int tipo_usuario, bool restringido) {
	cout << "Selecione una conferencia" << endl;
	if (restringido == true) {
		// se entra aqui si selecionaremos una conferencia en la que si o si PARTICIPAMOS
		int opcion = -1;
		vector <int> indices;
		while (opcion < 0) {
			int x = 0;
			int proyecion = 1;
			vector <int> los_indices;
			while (x < lista.size()) {
				bool pertenece = pertenece_conferencia(lista[x], tipo_usuario, nombre);
				if (pertenece == true) {
					cout << proyecion << "- " << lista[x].get_nombre() << endl;
					proyecion = proyecion + 1;
					los_indices.push_back(x);
				}
				x = x + 1;
			}
			if (proyecion == 1) {
				// implica que no tuvo ninguna conferencia
				// entonces retornaremos un -1 para que la siguien funcion (existe_errores) diga que hubo un error
				cout << "Usted no pertenece a ninguna conferencia" << endl;
				return -1;
			}
			// implica que tiene 1 o mas conferencias
			opcion = pedir_numero(los_indices.size());
			opcion = opcion - 1;
			indices = los_indices;
		}
		return indices[opcion];
	}
	else {
		// aqui el usuario puede selecionar cualquier conferencias es decir, no esta RESTRINGIDO que conferencias mostrar
		// sera usada para cuando un auto quiere enviar un articulo, es decir puede enviar un articulo a cualquier conferencia
		int opcion = -1;
		while (opcion < 0) {
			int x = 0;
			while (x < lista.size()) {
				cout << x + 1 << "- " << lista[x].get_nombre() << endl;
				x = x + 1;
			}
			opcion = pedir_numero(lista.size());
		}
		return opcion - 1;
	}
}

bool existe_errores(int n) {
	if (n == -1) {
		// implica que hubo un error
		cout << "Usted no pertenece a ninguna conferencia" << endl;
		return true;
		if (n == -2) {
			// implica que no es un autor principal
			cout << "Usted no es el autor principal de ningun articulo" << endl;
		}
	}
	else {
		return false;
	}
}

int obtener_indice_revisor(conferencia una_conferencia, string nombre) {
	// nesesitamos esta funcion por que nesesitamos el indice para evaluar o comentar en un articulo
	int x = 0;
	while (x < una_conferencia.los_revisores.size()) {
		if (nombre.compare(una_conferencia.los_revisores[x].get_nombre()) == 0) {
			return x;
		}
		x = x + 1;
	}
}

int selecionar_articulo(conferencia una_conferencia, int tipo_usuario, string nombre) {
	cout << "Selecione un articulo" << endl;
	if (tipo_usuario == 1 || tipo_usuario == 2) {
		int opcion = -1;
		while (opcion < 0) {
			int x = 0;
			while (x < una_conferencia.articulos_resividos.size()) {
				cout << x + 1 << "- " << una_conferencia.articulos_resividos[x].get_titulo() << endl;
				x = x + 1;
			}
			opcion = pedir_numero(una_conferencia.articulos_resividos.size());
		}
	}
	else {
		// aqui seleciona un autor, y solo puede selecionar si es que es el autor principal es decir en un articulo ---> los_autores[0] == nombre del autor
		int opcion = -1;
		while (opcion < 0) {
			int x = 0;
			int proyecion = 1;
			while (x < una_conferencia.articulos_resividos.size()) {
				if (nombre.compare(una_conferencia.articulos_resividos[x].los_autores[0].get_nombre()) == 0) {
					cout << proyecion << "- " << una_conferencia.articulos_resividos[x].get_titulo() << endl;
					proyecion = proyecion + 1;
				}
				x = x + 1;
			}
			if (proyecion == 1) {
				// implica que no es el autor principal de ningun articulo de la conferencia
				return -2;
			}
			opcion = pedir_numero(proyecion - 1);
			opcion = opcion - 1;
		}
		return opcion;
	}
}

void menu_chair(vector <conferencia>& lista) {
	vector <string> usuario = crear_usuario();
	chair un_chair(usuario[0], usuario[1], usuario[2]);
	actualizar_usuario(lista, 1, usuario);
	system("cls");
	int opcion = 0;
	while (opcion != -1) {
		cout << endl;
		cout << "Bienvenido chair" << endl;
		cout << "¿Quq quiere hacer?" << endl;
		cout << "1- Crear conferencia" << endl;
		cout << "2- Mostrar todas las conferencias" << endl;
		cout << "3- Mostrar mis conferencias" << endl;
		cout << "4- Agregar chair" << endl;
		cout << "5- Agregar revisor" << endl;
		cout << "6- Aceptar o rechazar un articulo" << endl;
		cout << "7- Salir de la cuenta" << endl;
		opcion = pedir_numero(7);
		switch (opcion) {
		case -1: opcion = 0; break; // entra aqui si al pedir no ingresa un numero o ingreso una opcion que no existe
		case 1: {
			cout << "crear conferencia" << endl;
			vector <string> una_conferencia = un_chair.crear_conferencia();
			conferencia nueva_conferencia(una_conferencia);
			revisor un_revisor(una_conferencia[5], "", "");
			nueva_conferencia.agregar_chair(un_chair);
			nueva_conferencia.agregar_revisor(un_revisor);
			lista.push_back(nueva_conferencia);
			break;
		}
		case 2: mostrar_todas_las_conferencias(lista); break;
		case 3: mostrar_mis_conferencias(lista, 1, usuario[0]); break;
		case 4: {
			int indice_conferencia = selecion_conferencia(lista, usuario[0], 1, true);
			bool error = existe_errores(indice_conferencia);
			if (error == true) {
				cout << "Hubo un error" << endl;
			}
			else {
				cout << "Ingrese el nombre del nuevo chair" << endl;
				string nombre;
				getline(cin, nombre);
				chair un_chair(nombre, "", "");
				lista[indice_conferencia].agregar_chair(un_chair);
			}
			break;
		}
		case 5: {
			int indice_conferencia = selecion_conferencia(lista, usuario[0], 1, true);
			bool error = existe_errores(indice_conferencia);
			if (error == true) {
				cout << "Hubo un error" << endl;
			}
			else {
				cout << "Ingrese el nombre del nuevo revisor" << endl;
				string nombre;
				getline(cin, nombre);
				revisor un_revisor(nombre, "", "");
				lista[indice_conferencia].agregar_revisor(un_revisor);
			}
			break;
		}
		case 6: {
			int indice_conferencia = selecion_conferencia(lista, usuario[0], 1, true);
			bool error = existe_errores(indice_conferencia);
			if (error == true) {
				cout << "Hubo un error" << endl;
			}
			else {
				int indice_articulo = selecionar_articulo(lista[indice_conferencia], 1, usuario[0]);
				bool error2 = existe_errores(indice_articulo);
				if (error2 == true) {
					cout << "Hubo un error" << endl;
				}
				else {
					un_chair.aceptar_o_rechazar(lista[indice_conferencia].articulos_resividos[indice_articulo], lista[indice_conferencia].get_nombre());
					lista[indice_conferencia].agregar_articulo_final(lista[indice_conferencia].articulos_resividos[indice_articulo]);
				}
			}
			break;
		}
		case 7: opcion = -1; system("cls"); break;
		}
	}
}

void menu_revisor(vector <conferencia>& lista) {
	vector <string> usuario;
	usuario = crear_usuario();
	revisor un_revisor(usuario[0], usuario[1], usuario[2]);
	system("cls");
	int opcion = 0;
	while (opcion != -1) {
		cout << endl;
		cout << "Bienvenido revisor" << endl;
		cout << "¿Que quiere hacer?" << endl;
		cout << "1- Mostrar todas las conferencias" << endl;
		cout << "2- Mostrar mis conferencias" << endl;
		cout << "3- Comentar un articulo" << endl;
		cout << "4- Evaluar un articulo" << endl;
		cout << "5- salir de la cuenta" << endl;
		opcion = pedir_numero(5);
		switch (opcion) {
		case -1: opcion = 0; break; // entra aqui si al pedir no ingresa un numero o ingreso una opcion que no existe
		case 1: mostrar_todas_las_conferencias(lista); break;
		case 2: mostrar_mis_conferencias(lista, 2, usuario[0]); break;
		case 3: {
			int indice_conferencia = selecion_conferencia(lista, usuario[0], 2, true);
			bool error = existe_errores(indice_conferencia);
			if (error == true) {
				cout << "Hubo un error" << endl;
			}
			else {
				int indice_articulo = selecionar_articulo(lista[indice_conferencia], 2, usuario[0]);
				bool error2 = existe_errores(indice_articulo);
				if (error2 == true) {
					cout << "Hubo un error" << endl;
				}
				else {
					int indice_revisor = obtener_indice_revisor(lista[indice_conferencia], usuario[0]);
					un_revisor.comentar(lista[indice_conferencia].articulos_resividos[indice_articulo], indice_revisor);
				}
			}
			break;
		}
		case 4: {
			int indice_conferencia = selecion_conferencia(lista, usuario[0], 2, true);
			bool error = existe_errores(indice_conferencia);
			if (error == true) {
				cout << "Hubo un error" << endl;
			}
			else {
				int indice_articulo = selecionar_articulo(lista[indice_conferencia], 2, usuario[0]);
				bool error2 = existe_errores(indice_articulo);
				if (error2 == true) {
					cout << "Hubo un error" << endl;
				}
				else {
					int indice_revisor = obtener_indice_revisor(lista[indice_conferencia], usuario[0]);
					un_revisor.evaluar(lista[indice_conferencia].articulos_resividos[indice_articulo], indice_revisor);
				}
			}
			break;
		}
		case 5: opcion = -1; system("cls"); break;
		}
	}
}

void menu_autor(vector <conferencia>& lista) {
	vector <string> usuario;
	usuario = crear_usuario();
	autor un_autor(usuario[0], usuario[1], usuario[2]);
	system("cls");
	int opcion = 0;
	while (opcion != -1) {
		cout << endl;
		cout << "Bienvenido autor" << endl;
		cout << "¿Que quiere hacer?" << endl;
		cout << "1- Mostrar todas las conferencias" << endl;
		cout << "2- Mostrar mis conferencias" << endl;
		cout << "3- Crear articulo" << endl;
		cout << "4- Enviar articulo final" << endl;
		cout << "5- Ver chairs de una conferencia" << endl;
		cout << "6- Ver revisores de una conferencia" << endl;
		cout << "7- salir de la cuenta" << endl;
		opcion = pedir_numero(7);
		switch (opcion) {
		case -1: opcion = 0; break; // entra aqui si al pedir no ingresa un numero o ingreso una opcion que no existe
		case 1: mostrar_todas_las_conferencias(lista); break;
		case 2: mostrar_mis_conferencias(lista, 3, usuario[0]); break;
		case 3: {
			vector <string> datos_nuevo_articulo = un_autor.crear_articulo();
			vector <string> comentarios = comentarios_falsos("", "", "");
			vector <int> notas = notas_falsas(0, 0, 0);
			articulo nuevo_articulo(datos_nuevo_articulo[0], datos_nuevo_articulo[1], datos_nuevo_articulo[2], comentarios, notas, "FALSE");
			nuevo_articulo.agregar_autor(un_autor);
			int indice_conferencia = selecion_conferencia(lista, usuario[0], 3, false);
			cout << indice_conferencia << endl;
			bool error = existe_errores(indice_conferencia);
			if (error == true) {
				cout << "Hubo un error" << endl;
			}
			else {
				lista[indice_conferencia].agregar_articulo(nuevo_articulo);
				cout << "Se envio el articulo exitosamente" << endl;
			}
			break;
		} cout << "crear articulo" << endl; break;
		case 4: {
			int indice_conferencia = selecion_conferencia(lista, usuario[0], 3, true);
			bool error = existe_errores(indice_conferencia);
			if (error == true) {
				cout << "Hubo un error" << endl;
			}
			else {
				int indice_articulo = selecionar_articulo(lista[indice_conferencia], 3, usuario[0]);
				bool error2 = existe_errores(indice_articulo);
				if (error2 == true) {
					cout << "Hubo un error" << endl;
				}
				else {
					string cuerpo_final = un_autor.convertir_a_final();
					lista[indice_conferencia].articulos_resividos[indice_articulo].version_final(cuerpo_final);
					lista[indice_conferencia].agregar_articulo_final(lista[indice_conferencia].articulos_resividos[indice_articulo]);
				}
			}
			break;
		}
		case 5: {
			int indice_conferencia = selecion_conferencia(lista, usuario[0], 3, false);
			bool error = existe_errores(indice_conferencia);
			if (error == true) {
				cout << "Hubo un error" << endl;
			}
			else {
				lista[indice_conferencia].mostrar_sus_chair();
			}
			break;
		}
		case 6: {
			int indice_conferencia = selecion_conferencia(lista, usuario[0], 3, false);
			bool error = existe_errores(indice_conferencia);
			if (error == true) {
				cout << "Hubo un error" << endl;
			}
			else {
				lista[indice_conferencia].mostrar_sus_revisores();
			}
			break;
		}
		case 7: opcion = -1; system("cls"); break;
		}

	}
}

void menu_usuarios(int opcion, vector <conferencia>& lista) {
	switch (opcion) {
	case 1: system("cls"); menu_chair(lista); break;
	case 2: system("cls"); menu_revisor(lista); break;
	case 3: system("cls"); menu_autor(lista); break;
	case 4: system("cls"); break;
	}
}

int pedir_tipo_usuario(vector <conferencia>& lista) {
	cout << "Ingrese que tipo de usario es usted" << endl;
	cout << "1- chair" << endl;
	cout << "2- revisor" << endl;
	cout << "3- autor" << endl;
	cout << "4- salir del programa" << endl;
	int opcion = pedir_numero(4);
	menu_usuarios(opcion, lista);
	return opcion;
}

void menu(vector <conferencia>& lista) {
	int tipo_usuario = 0;
	while (tipo_usuario != 4) { // distinto de 4 porque la opcion 4 es para salir del programa
		tipo_usuario = pedir_tipo_usuario(lista);
	}
}

int main(){
	
	vector <conferencia> las_conferencias;
	agregar_conferencias_falsas(las_conferencias);
	menu(las_conferencias);
	cout << "El programa a terminado" << endl;
	
	return 0;
}
