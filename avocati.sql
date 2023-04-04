

--Script pentru crearea si intretinerea bazei de date Avocati

--Create database
--TODO: Check if database already exists and DO NOT CREATE if so
CREATE DATABASE IF NOT EXISTS Avocati;

--Avocati
CREATE TABLE IF NOT EXISTS Avocati (
    ID_Avocat int PRIMARY KEY, 
    Nume varchar(50) not null, Prenume varchar(50), 
    Telefon varchar(15), 
    Email varchar(50),
);

--Clienti
CREATE TABLE IF NOT EXISTS Clienti (
    CNP varchar(13) int PRIMARY KEY, 
    Nume varchar(50) not null, Prenume varchar(50), 
    Adresa varchar(255))
);

--Contracte
CREATE TABLE IF NOT EXISTS Contracte (
    ID varchar (25) int PRIMARY KEY,
    Numar varchar(20),
    Data_Start varchar (20),
    Data_Sfarsit varchar (20),
    ID_Avocat int,
	CNP int,
    Tip_contract varchar (20),
	Stadiu varchar (20)
		FOREIGN KEY (ID_Avocat)
			REFERENCES Avocat (ID_Avocat)
		FOREIGN KEY (CNP)
			REFERENCES Clienti (CNP)
);


--Facturare
CREATE TABLE IF NOT EXISTS Facturare (
    Facturare int PRIMARY KEY,
    ID_Factura varchar(25),
    ID_Contract varchar(25),
    NR_Ore varchar (10),
    Pret_ora decimal (10,2),
    FOREIGN KEY (ID_Avocat)
        REFERENCES Avocati(ID_Avocat),
    FOREIGN KEY (CNP)
        REFERENCES Clienti(CNP)
);


