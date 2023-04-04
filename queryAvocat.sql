-- Active: 1677605495494@@127.0.0.1@3306@avocati
CREATE TABLE IF NOT EXISTS Avocati (
    ID_Avocat int PRIMARY KEY, 
    Nume varchar(50) not null, 
    Prenume varchar(50), 
    Telefon varchar(15), 
    Email varchar(50),
    isAvocat bit
);

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