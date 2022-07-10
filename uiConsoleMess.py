def printWelcome():
    print("""
╔═════════════════════════════════════════════════════════════════════════════════════╗
║       ╔═══╗     ╔╗  ╔═══╗  ╔╗          ╔═══╗           ╔═══╗                        ║
║       ║╔═╗║    ╔╝╚╗ ║╔══╝  ║║          ║╔══╝           ║╔═╗║                        ║
║       ║║ ╚╝╔══╗╚╗╔╝ ║╚══╗╔╗║║ ╔══╗╔══╗ ║╚══╗╔═╗╔══╗╔╗╔╗║║ ║║╔╗╔╗╔══╗╔═╗╔╗╔══╗╔══╗   ║
║       ║║╔═╗║╔╗║ ║║  ║╔══╝╠╣║║ ║╔╗║║══╣ ║╔══╝║╔╝║╔╗║║╚╝║║╚═╝║║╚╝║║╔╗║║╔╝╠╣║╔╗║║╔╗║   ║
║       ║╚╩═║║║═╣ ║╚╗╔╝╚╗  ║║║╚╗║║═╣╠══║╔╝╚╗  ║║ ║╚╝║║║║║║╔═╗║║║║║║║═╣║║ ║║║╚╝║║╚╝║   ║
║       ╚═══╝╚══╝ ╚═╝╚══╝  ╚╝╚═╝╚══╝╚══╝╚══╝  ╚╝ ╚══╝╚╩╩╝╚╝ ╚╝╚╩╩╝╚══╝╚╝ ╚╝╚═╗║╚══╝   ║
║                                                                          ╔═╝║       ║
╚═════════════════════════════════════════════════════════════════════════════════════╝                                                                      
""")

def workFinished():
    print("""
    ╔═════════════════════════════════════════════════════════════════════════════════╗
    ║                      Download terminato con successo.                           ║
    ║                       Premi un tasto per continuare                             ║
    ╚═════════════════════════════════════════════════════════════════════════════════╝
    """)

def ipErr():
    print("""
    ╔═════════════════════════════════════════════════════════════════════════════════╗
    ║         Ops! Qualcosa è andato storto. L'IP e' errato o la connessione          ║
    ║                          di Amerigo e' stata chiusa.                            ║
    ║        Se l'indirizzo inserito in precedenza e' corretto, riavviare l'          ║
    ║                     applicazione sul cellulare e riprovare.                     ║
    ║                        Premi un tasto per riprovare...                          ║
    ╚═════════════════════════════════════════════════════════════════════════════════╝
    """)
   

def downloadCaneled():
    print("""
    ╔═════════════════════════════════════════════════════════════════════════════════╗
    ║                      Download annullato con successo.                           ║
    ║                        Premi un tasto per chiudere...                           ║
    ╚═════════════════════════════════════════════════════════════════════════════════╝
    """)
    

def generalErr():
    print("""
    ╔═════════════════════════════════════════════════════════════════════════════════╗
    ║                          Ops! Qualcosa è andato storto.                         ║
    ║                                   Riavviare l'                                  ║
    ║                     applicazione sul cellulare e riprovare.                     ║
    ║                        Permi un tasto per chiudere l'app                        ║
    ╚═════════════════════════════════════════════════════════════════════════════════╝
    """)

def commandInvalid():
    print("""
    ╔═════════════════════════════════════════════════════════════════════════════════╗
    ║                     Ops! Il comando inserito è invalido                         ║
    ║                           ricontrollare la sintassi.                            ║ 
    ║                   Per informazioni sui comandi e sulla loro                     ║
    ║                   formattazione, eseguire il comando: /help.                    ║
    ╚═════════════════════════════════════════════════════════════════════════════════╝
    """)
    

def goodbye():
    print("""
    ╔═════════════════════════════════════════════════════════════════════════════════╗
    ║                                 Arrivederci!                                    ║
    ╚═════════════════════════════════════════════════════════════════════════════════╝
    """)
    

def help():
    print("""
    ╔═════════════════════════════════════════════════════════════════════════════════╗
    ║                      Informazioni relative ai comandi:                          ║
    ║                                                                                 ║
    ║          1) /help: Mostra la lista completa dei comandi eseguibili con una      ║
    ║                              piccola descrizione;                               ║
    ║                                                                                 ║
    ║        2) /nav: Permette di navigare nelle cartelle presenti sul dispositivo;   ║
    ║                                                                                 ║
    ║ 3) /download [nomefile]: Se il nome viene specificato, il programma scaricherà  ║
    ║                 esclusivamente il file con il nome specificato.                 ║
    ║          Se non viene specificato nessun nome, il programma scaricherà tutti    ║
    ║              i file contenuti nella cartella attualmente aperta.                ║
    ║                                                                                 ║
    ║            4) /back: Permette di tornare nella cartella più esterna.            ║
    ║                                                                                 ║
    ║                 5) /quit: Termina l'esecuzione del programma.                   ║
    ║                                                                                 ║
    ║                        Per chiudere la guida...                                 ║
    ╚═════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    

def contentPrinter(items, CHAR_TO_USE):
    i = 0
    for item in items:
        if i == 0:
            print("┌",CHAR_TO_USE, item[1:])
        elif i+1 == len(items):
            print("└",CHAR_TO_USE, item[1:])
        else:
            print("├",CHAR_TO_USE, item[1:])   
        i += 1
        