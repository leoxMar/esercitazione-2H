from Dbhelper import DbHelper


class ClientiDAO(object):
    __db = None

    def __init__(self):
        self.__db = DbHelper()
    
    def getNumClienti_byAgente(self):
        try:
            res = self.__db.query('select count(*) as num_clienti, agente from clienti group by agente').fetchall()
        except Exception as e:
            print(f'Error: {e}')
        finally:
            for tup in res:
                print(f"L'agente #{tup[1]} ha {tup[0]} cliente/i")
    
    def getClienti_byAgente(self):
        agente = int(input('Inserire il codice agente: '))
        listaNomi = []

        try:
            agenti = self.__db.query('select agente from clienti group by agente').fetchall()
            check = any([agente in tup for tup in agenti])
            if check is False: 
                print(f'Agente numero {agente} non trovato')
            else:
                nomi = self.__db.query(f'select nome from clienti where agente = {agente}').fetchall()
        except Exception as e:
            print(f'Error: {e}')
        finally:
            for tup in nomi:
                listaNomi.append(tup[0])
            print(f"L'agente #{agente} gestisce i seguenti clienti:\n{listaNomi}")