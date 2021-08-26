# include <iostream>
# include <vector>
# include <stdlib.h>
# include "archivos.h"
# include "indice_invertido.h"

using namespace std;

void mostrar_vector(vector <string> mi_vector){
    for (int i = 0; i < mi_vector.size();i++){
        cout << mi_vector[i] << endl;
    }
}

void separar_datos(vector <string> datos,vector <string> &nombres_archivos, vector <string> &frases, string &frase_consulta){
    for (int i = 1; i < datos.size() - 2;i = i + 3){
        string nombre_archivo = datos[i];
        string frase = datos[i + 2];
        nombres_archivos.push_back(nombre_archivo);
        frases.push_back(frase);
    }
    int ultimo_indice = datos.size() - 1;
    frase_consulta = datos[ultimo_indice];
}

vector <string> separar_frase(string frase){
    vector <string> frases_separadas;
    string sumatoria = "";
    for (int i = 0; i < frase.size();i++){
        if ( frase[i] == ' ' ){
            frases_separadas.push_back(sumatoria);
            sumatoria = "";
        }else{
        	sumatoria = sumatoria + frase[i];
		}
    }
    frases_separadas.push_back(sumatoria);
    return frases_separadas;
}

vector <indice_invertido> crear_indice(vector <string> nombres_archivos,vector <string> frases){
    vector <indice_invertido> base_datos;
    for (int i = 0; i < nombres_archivos.size();i++){
        vector <string> palabras = separar_frase(frases[i]);
        for (int j = 0; j < palabras.size();j++){
            bool existe = false;
            int indice;
            for (int k = 0; k < base_datos.size();k++){
                if (base_datos[k].coincide_clave(palabras[j]) == true){
                	existe = true;
                	indice = k;
                	break;
				}
            }
            if (existe == true){
                base_datos[indice].agregar_elemento(nombres_archivos[i]);
            }else{
                indice_invertido nuevo_indice(palabras[j]);
                nuevo_indice.agregar_elemento(nombres_archivos[i]);
                base_datos.push_back(nuevo_indice);
            }
        }
    }
    return base_datos;
}

vector <string> responder_consulta(string frase_consulta,vector <indice_invertido> base_datos){
	vector <string> palabras = separar_frase(frase_consulta);
	vector <string> respuestas;
	for (int i = 0; i < palabras.size();i++){
		bool existe = false;
		int indice;
		for (int j = 0; j < base_datos.size();j++){
			if ( base_datos[j].clave == palabras[i] ){
				existe = true;
				indice = j;
				break;
			}
		}
		string respuesta = "Resultados para '" + palabras[i] + "' : ";
		if (existe == true){
			respuesta = respuesta + base_datos[indice].recuperar_elementos();
		}else{
			respuesta = respuesta + "No hay resultados";
		}
		respuestas.push_back(respuesta);
	}
	return respuestas;
}

int main(){
	vector <string> datos = abrir_archivo("in.txt"); 
    vector <string> nombres_archivos,frases;
    string frase_consulta;
    separar_datos(datos,nombres_archivos,frases,frase_consulta);
    vector <indice_invertido> base_datos = crear_indice(nombres_archivos,frases);
    for (int i = 0;i < base_datos.size();i++){
        cout << base_datos[i].clave << " : " << base_datos[i].recuperar_elementos() << endl;
    }
    vector <string> respuestas = responder_consulta(frase_consulta,base_datos);
    mostrar_vector(respuestas);
    escribir_archivo("out.txt",respuestas);
	return 0;
}
