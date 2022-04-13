
class Persona():
    nome=''
    age=0
    cognome=''

    def __init__(self,age,nome,cognome) :
        self.age=age
        self.nome=nome
        self.cognome=cognome

    def __str__ (self):
     return 'MyClass(name=' + str(self.nome) + ' ,age=' + str(self.age) + ',cognome='+str(self.cognome)+')'


class Studente(Persona):
    studente=''

    def __init__(self,age,nome,cognome,percorso):
      super().__init__(age,nome,cognome)
      self.percorso=percorso

    def __str__(self):
        return 'mi chiamo ' + str(self.nome) + ' ,age=' + str(self.age) + ',cognome='+str(self.cognome)+' ed il mio percorso di studi è '+self.percorso+')'



class Lavoratore(Persona):

    lavoro=''

    def __init__(self,age,nome,cognome,lavoro):
      super().__init__(age,nome,cognome)
      self.lavoro=lavoro

    def __str__(self):
        return 'mi chiamo ' + str(self.nome) + ' ,age=' + str(self.age) + ',cognome='+str(self.cognome)+' ed il mio lavoro è'+self.lavoro+')'


class App(object):
    def __init__(self):
        __persona = Persona(12, 'leo', 'marchi')
        print(__persona)
        __lavoratore = Lavoratore(23,'UGo','delcolle','muratore')
        print(__lavoratore)
        __studente = Studente(23,'UGo','delcolle','matematico')
        print(__studente)
        

if __name__ == "__main__":
    app = App()