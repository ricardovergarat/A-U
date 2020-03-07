target.exe : obj/main.o obj/autor.o obj/persona.o obj/articulo.o obj/conferencia.o
	g++ -o target.exe obj/main.o obj/autor.o obj/persona.o obj/articulo.o obj/conferencia.o
obj/main.o : main.cc obj/autor.o obj/persona.o obj/articulo.o obj/conferencia.o
	g++ main.cc -c -o obj/main.o
obj/autor.o : autor.cc autor.h
	g++ autor.cc -c -o obj/autor.o
obj/persona.o : persona.cc persona.h
	g++ persona.cc -c -o obj/persona.o
obj/articulo.o : articulo.cc articulo.h
	g++ articulo.cc -c -o obj/articulo.o
obj/conferencia.o : conferencia.cc conferencia.h
	g++ conferencia.cc -c -o obj/conferencia.o 