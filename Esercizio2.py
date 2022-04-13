class File_utilities:

           
    def __stampa_medie_voto_e_risultati__(self):
         nome_file=input('inserire nome file')
         primo_esame=[]
         secondo_esame=[]
         nominativi=[]
         media_voti=[]
         
         try:
          with open(f'{nome_file}','r') as saluti:
            
           lst=(saluti.readlines())

         except:
             print('file errato')

         for e in lst:
               
             noNewLine = e.replace('\n','')
             primo_esame.append(noNewLine)
             secondo_esame.append(noNewLine)
             nominativi.append(noNewLine)
          
         del nominativi [1::3]
         del primo_esame[0::3]
         del nominativi[1::2] 
         del primo_esame[1::2]  
         del secondo_esame[0::3]
         del secondo_esame[0::2]

         for indice in primo_esame:
            media=(int(primo_esame[0+primo_esame.index(indice)])+int(secondo_esame[0+primo_esame.index(indice)]))/2
            media_voti.append(media)
        
         dizionario=dict(zip(nominativi,media_voti))
       

         for key,value in dizionario.items():
             if value>=18:
                 print(key,'esame superato con media:' + str(value))
             else:
                 print(key,'esame non superato ')
     
    
File_utilities.__stampa_medie_voto_e_risultati__('self')