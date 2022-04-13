
from ClientiDAO import ClientiDAO


class App():
    caso = int(input('Inserisci un numero tra 1 o 2: '))
    

    if caso == 1:
        __clientidao = ClientiDAO()
        __clientidao.getNumClienti_byAgente()
    elif caso == 2:
        __clientidao = ClientiDAO()
        __clientidao.getClienti_byAgente()
    else:
        print('Funzione non valida: uscita in corso')

if __name__ == "__main__":
    app = App()