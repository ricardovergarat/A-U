CREATE TABLE Pasajero(
    Rut int NOT NULL,
    Nombre VARCHAR(50)
);
ALTER TABLE Pasajero ADD CONSTRAINT PK_Pasajero PRIMARY KEY (Rut);

CREATE TABLE Crucero(
    Nombre VARCHAR(50) NOT NULL,
    Tiempo_viaje int,
    Longuitud FLOAT,
    Numero_puertos INT
);
ALTER TABLE Crucero ADD CONSTRAINT PK_Crucero PRIMARY KEY (Nombre);

CREATE TABLE Cabina(
    Nombre_crucero VARCHAR(50) NOT NULL,
    Numero_clase INT NOT NULL
);
ALTER TABLE Cabina ADD CONSTRAINT PK_Cabina PRIMARY KEY (Nombre_crucero,Numero_clase);
ALTER TABLE Cabina ADD CONSTRAINT FK_Cabina_Crucero FOREIGN KEY (Nombre_crucero) REFERENCES Crucero(Nombre);

CREATE TABLE Puerto(
    Nombre VARCHAR(50) NOT NULL,
    Nombre_pais VARCHAR(50)
);
ALTER TABLE Puerto ADD CONSTRAINT PK_Puerto PRIMARY KEY (Nombre);

CREATE TABLE Pais(
    Nombre VARCHAR(50) NOT NULL,
    Continente VARCHAR(50)
);
ALTER TABLE Pais ADD CONSTRAINT PK_Pais PRIMARY KEY (Nombre);

CREATE TABLE Barco(
    Nombre VARCHAR(50) NOT NULL,
    Capacidad_pasajeros int
);
ALTER TABLE Barco ADD CONSTRAINT Pk_Barco PRIMARY KEY (Nombre);

CREATE TABLE Registra(
    Nombre_crucero VARCHAR(50) NOT NULL,
    Numero_cabina INT NOT NULL,
    Rut_pasajero INT NOT NULL,
    Precio INT
);
ALTER TABLE Registra ADD CONSTRAINT PK_Registra PRIMARY KEY (Nombre_crucero,Numero_cabina,Rut_pasajero);
ALTER TABLE Registra ADD CONSTRAINT FK_Registra_Crucero FOREIGN KEY (Nombre_crucero) REFERENCES Crucero(Nombre);
ALTER TABLE Registra ADD CONSTRAINT FK_Registra_Cabina FOREIGN KEY (Numero_cabina) REFERENCES Cabina(Numero_clase);
ALTER TABLE Registra ADD CONSTRAINT FK_Registra_Pasajero FOREIGN KEY (Rut_pasajero) REFERENCES Pasajero(Rut);

CREATE TABLE Esta(
    Nombre_crucero VARCHAR(50) NOT NULL,
    Nombre_pais VARCHAR(50) NOT NULL
);
ALTER TABLE Esta ADD CONSTRAINT PK_Esta PRIMARY KEY (Nombre_crucero,Nombre_pais);
ALTER TABLE Esta ADD CONSTRAINT FK_Esta_Crucero FOREIGN KEY (Nombre_crucero) REFERENCES Crucero(Nombre);
ALTER TABLE Esta ADD CONSTRAINT FK_Esta_Pais FOREIGN KEY (Nombre_pais) REFERENCES Pais(Nombre);

CREATE TABLE Amarra(
    Nombre_crucero VARCHAR(50) NOT NULL,
    Nombre_puerto VARCHAR(50) NOT NULL,
    Tiempo INT,
    Fecha VARCHAR(50)
);
ALTER TABLE Amarra ADD CONSTRAINT PK_Amarra PRIMARY KEY (Nombre_crucero,Nombre_puerto);
ALTER TABLE Amarra ADD CONSTRAINT FK_Amarra_Crucero FOREIGN KEY (Nombre_crucero) REFERENCES Crucero(Nombre);
ALTER TABLE Amarra ADD CONSTRAINT FK_Amarra_Puerto FOREIGN KEY (Nombre_puerto) REFERENCES Puerto(Nombre);

CREATE TABLE Lleva(
    Nombre_crucero VARCHAR(50) NOT NULL,
    Nombre_barco VARCHAR(50) NOT NULL
);
ALTER TABLE Lleva ADD CONSTRAINT PK_Lleva PRIMARY KEY (Nombre_crucero,Nombre_barco);
ALTER TABLE Lleva ADD CONSTRAINT FK_Lleva_Crucero FOREIGN KEY (Nombre_crucero) REFERENCES Crucero(Nombre);
ALTER TABLE Lleva ADD CONSTRAINT FK_Lleva_barco FOREIGN KEY (Nombre_barco) REFERENCES Barco(Nombre);


INSERT INTO Pasajero(Rut,Nombre) VALUES (143848878,'Juan Carlos Bodoque');
INSERT INTO Pasajero(Rut,Nombre) VALUES (203061274,'Calsetin con rombos-man');
INSERT INTO Crucero(Nombre,Tiempo_viaje,Longuitud,Numero_puertos) VALUES ('titanic',3,15.6,1);
INSERT INTO Crucero(Nombre,Tiempo_viaje,Longuitud,Numero_puertos) VALUES ('dyatlov',7,23.6,3);
INSERT INTO Cabina(Nombre_crucero,Numero_clase) VALUES ('dyatlov',2);
INSERT INTO Cabina(Nombre_crucero,Numero_clase) VALUES ('titanic',3);
INSERT INTO Puerto(Nombre,Nombre_pais) VALUES ('Ángeles','EEUU');
INSERT INTO Puerto(Nombre,Nombre_pais) VALUES ('Miami','IN CSI Miami');
INSERT INTO Pais(Nombre,Continente) VALUES ('EEUU','America');
INSERT INTO Pais(Nombre,Continente) VALUES ('Mexico','America');
INSERT INTO Barco(Nombre,Capacidad_pasajeros) VALUES ('El perla negra',20);
INSERT INTO Barco(Nombre,Capacidad_pasajeros) VALUES ('El holandes errante',35);
INSERT INTO Registra(Nombre_crucero,Numero_cabina,Rut_pasajero,Precio) VALUES ('dyatlov',2,203061274,30000);
INSERT INTO Registra(Nombre_crucero,Numero_cabina,Rut_pasajero,Precio) VALUES ('titanic',3,143848878,500000);
INSERT INTO Esta(Nombre_crucero,Nombre_pais) VALUES ('titanic','EEUU');
INSERT INTO Esta(Nombre_crucero,Nombre_pais) VALUES ('dyatlov','Russia');
INSERT INTO Amarra(Nombre_crucero,Nombre_puerto,Tiempo,Fecha) VALUES ('titanic','Miami',4342,'27/06/2020');
INSERT INTO Amarra(Nombre_crucero,Nombre_puerto,Tiempo,Fecha) VALUES ('dyatlov','Ángeles',16547654654,'23/01/1959');
INSERT INTO Lleva(Nombre_crucero,Nombre_barco) VALUES ('titanic','El holandes errante');
INSERT INTO Lleva(Nombre_crucero,Nombre_barco) VALUES ('dyatlov','El perla negra');


SELECT * FROM Pasajero;
SELECT * FROM Crucero;
SELECT * FROM Cabina;
SELECT * FROM Puerto;
SELECT * FROM Pais;
SELECT * FROM Barco;
SELECT * FROM Registra;
SELECT * FROM Esta;
SELECT * FROM Amarra;
SELECT * FROM Lleva;









