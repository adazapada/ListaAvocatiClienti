class User:
    def __init__(self,ID_Adm,Nume,Prenume,email,parola,isAdmin):
        self.ID_Adm = ID_Adm
        self.Nume = Nume
        self.Prenume = Prenume
        self.email = email
        self.parol = parola
        self.isAdmin = isAdmin
        
class Avocati:
    def __init__(self,ID_Avocat,Nume,Prenume,Telefon, Email):
        self.ID_Avocat = ID_Avocat
        self.Nume = Nume
        self.Prenume = Prenume
        self.Telefon = Telefon
        self.Email = Email
        
class Clienti:
    def __init__(self,CNP,Nume,Prenume,Adresa):
        self.CNP = CNP 
        self.Nume = Nume
        self.Prenume = Prenume
        self.Adresa = Adresa
        
class Contracte:
    def __init__(self, ID, NR, DATA_Start, DATA_Sfarsit, CNP, ID_Avocat, Tip_contract, Status):
        self.ID = ID 
        self.NR = NR 
        self.DATA_Start = DATA_Start
        self.DATA_Sfarsit = DATA_Sfarsit
        self.CNP = CNP 
        self.ID_Avocat = ID_Avocat 
        self.Tip_contract = Tip_contract
        self.Status = Status
    
class Facturare:
    def __init__(self, ID_FF, ID_Contract, NR_ore, Pret_ora, ID_Avocat, CNP, ACHITAT, DATA_Emitere, DATA_Incasare):
        self.ID_FF = ID_FF
        self.ID_Contract = ID_Contract
        self.NR_ore = NR_ore
        self.Pret_ora = Pret_ora
        self.ID_Avocat = ID_Avocat
        self.CNP = CNP
        self.ACHITAT = ACHITAT
        self.DATA_Emitere = DATA_Emitere
        self.DATA_Incasare = DATA_Incasare
    
import mysql.connector

def insert_data():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mateiandrei23!",
    database="avocati"
    )