import commands
import generalDatas
import uiConsoleMess

uiConsoleMess.printWelcome()
print("Inserisci l'IP mostrato sullo smartphone! (tralasciare il :8080)")
generalDatas.setHomeUrl(input())

commands.navigateTo(generalDatas.getHomeUrl())


while True:
    print("»", end=" ")
    command = input()
    commands.checkCommand(command)