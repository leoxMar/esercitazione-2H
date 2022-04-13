
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

      def main(self):
        return 'si sono un studente e sono '+str(self.nome)


class Lavoratore(Persona):

    def main(self):
        return 'si sono un lavoratore e sono '+str(self.nome)

io=Lavoratore(10,'leo','mark')
print(io.main())