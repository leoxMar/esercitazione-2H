class File_utilities():

    def leggi(nome_file):
        voti=[]
        nominativi=[]
        with open(f'{nome_file}','r') as saluti:
            
          lst=(saluti.readlines())
       
          for e in lst:
               
                noNewLine = e.replace('\n','')
                voti.append(noNewLine)
                nominativi.append(noNewLine)
          
        del nominativi [1::3]
        del voti[0::3]
        del nominativi[1::2]   
       # media=voti[0:2:1]
        print(nominativi)
        print (voti)
        
            
    def media_voti(voti):
        with open('media_voti.txt','a') as media:
            media.writelines(f'\n{voti}')

File_utilities.leggi('test.text')