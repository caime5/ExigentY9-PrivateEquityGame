"""
This is the tui --single player experience--- of the game made for Exigent for summer 2026.
This is fully designed around one (set of) person(s) maximizing the profit that they earn, and not competing groups.
All work done here, unless otherwise mentioned, is the thought-child of Carlos Mendoza.
All references to any person or company, living or deceased, are purely coincidential and are not malicious.
All comedic references, however, are intentional.
Funded partly by the sponsors at 5th Century Partners
Contact at carisamen157@gmail.com in case of either distribution, adaptation, or if a bug is seen. 
"""
import XGNGame as S

newline:str = ' '
one:str = '①'
two:str = '②'
three:str = '③'
four:str = '④'
five:str = '⑤'
seven:str = '⑦'
nine:str = '⑨'

#Dict of all companies
SE:dict[str, list[Callable[[int, float, float, float, float, float],Complex]|float|int|set[str]]]={}
##Required: Callables, Satis, cvr, growth, r,m factors, % max ownable, % owned, market cap
##Make own data into dict: Capital available, year, stocks owned.
SE['Self'] = [0,0,set()]
def play()->None:
    for i in range(4):
        print('Loading'+'.'*i+'\n')
    print("Welcome. All inputs will be done by keyboard, and all outputs will be shown here.")
    print("Also, there is no autosave feature; furthermore, only one 'saveslot' at most can exist at once.")
    status:str = ''
    quitFlag:bool = False
    while True:
        status = input(one+': New Game\n'+four+': Load Save\n' + nine+': Quit\n')
        if status == '9':
            quitFlag = True
            break #End program. Add Print, but not much else
        elif status == '4':
            break #Load prior save into data. Play on like new game
        elif status == '1':
            break #Actually do nothing. Treat newgame like a transient save unless saved.
    if not quitFlag:
        pass
        #Print message confirming year.
        if SE['Self'] == 0 :
            cgn = r.SystemRandom()
            seed = cgn.randint(1,10000)
            random.seed(seed)
            SE['Self'][0] = 250.0
            options = random.sample(list(SE.keys()), k=5)
            nineFlag:bool = False
            status = ''
            while nineFlag is False:
                if status == '' or status == '9':
                    status = input(one+': Stock 1\n'+two+': Stock 2\n'+three+': Stock 3\n'+four+': Stock 4\n'+five+': Stock 5' + seven+': Move to Purchase\n')
                elif status =='1':
                    pass #Show option entry 1's details. Make
                elif status == '2':
                    pass #Option 2
                elif status == '3':
                    pass #Option 3
                elif status == '4':
                    pass #option 4
                elif status == '5':
                    pass #Option 5
                elif status == '7':
                    nineFlag = True
                #Show 5 stocks. For all 5, detail the following:
                ## Cap price, % up for sale, formulae, cvr, sat.
            buyFlag = True
            while buyFlag:
                break #Not doing the buy option rn. Tired af. 
        
        #For each company, advance their prices based at most on the money they have
        #Then, once all have advanced, proceed with the following:
        ## Update cash on hand
        ## Tell them satis, cvr, current capital.
        ## Predicted vs actual returns for each stock they own.
        ## Let them buy more of the companies they own
        ## Or, let them sell shares to either still above 50% or all to 0. If to 0, remove from list
        ## Give them a random company to potentially add to portfolio
        ## Advance year.

        # Then, let them save & quit, save & continue, or continue.
        #Forcibly eject if they ever end up with <0 capital {Ignore capital. They dumb.}









#NO TOUCHY. HOW TS ACTUALLY WORKS
def run()-> None:
    play()
if __name__ == '__main__':
    run()
