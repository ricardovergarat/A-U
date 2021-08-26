# include <iostream>
# include <fstream>
# include <string>
# include <vector>


using namespace std;

vector <string> abrir_archivo(string nombre_archivo){
	ifstream archivo;
    // debe darse el nombre como char
    char nombre_archivo_char[nombre_archivo.size()];
    for (int i = 0;i < nombre_archivo.size();i++){
        nombre_archivo_char[i] = nombre_archivo[i];
    }
    archivo.open(nombre_archivo_char,ios::in); // -> darse como CHAR
    vector <string> datos;
    string linea;
    while ( !archivo.eof() ){ // mientras no sea el final del archivo
    	getline(archivo,linea);
    	datos.push_back(linea);
    }
    archivo.close();
    return datos;
}

void escribir_archivo(string nombre_archivo, vector <string> datos){
    ofstream archivo;
    // debe darse el nombre como char
    char nombre_archivo_char[nombre_archivo.size()];
    for (int i = 0;i < nombre_archivo.size();i++){
        nombre_archivo_char[i] = nombre_archivo[i];
    }
    archivo.open(nombre_archivo_char,ios::out); // -> darse como CHAR
    for ( int i = 0; i < datos.size();i++){
        archivo << datos[i] << endl;
    }
    archivo.close();
}

