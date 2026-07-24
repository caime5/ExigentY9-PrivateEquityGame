"""
This is the tui --single player offline experience--- of the game made for Exigent for summer 2026.
This is fully designed around one (set of) person(s) maximizing the profit that they earn, and not competing in groups against other groups.
All work done here, unless otherwise mentioned, is the thought-child of Carlos Mendoza.
All references to any person or company, living or deceased, are purely coincidential and are not malicious.
All comedic references, however, are intentional.
Funded partly by the sponsors at 5th Century Partners; Exigent sponsor.
Contact at carisamen157@gmail.com in case of either distribution, adaptation, or if a bug is seen. 
"""
from XGNPhysicalVsn3 import Complex, Stock
import time
from typing import Callable
import random as r
import json
import math
from numpy import random as ra

multiplyFlag = False #Extra day
baseFactorFlag = False #Birthday
shrinkCostFlag = False #cucumber
flattedRevFlag = False #pestilence
noDecayCVRFlag = False #arbiter
margin = 0.2

quiz:dict[int, list[str]] = {}
q: dict[int, str] = {}
quiz[0] = ["Look at coefficient of first term", "Use the equation to see how many can exist", "It is the largest exponent of the expression"]
q[0] = "How can we determine the maximum number of roots of any polynomial family in standard form?"
quiz[1] = ["1 if the largest power is even, 0 if odd", "0 if the largest power is even, 1 if odd", "1 regardless of even/odd parity", "0 regardless of even/odd parity"]
q[1] = "What is the minimum amounts of roots for any polynomial family?"
quiz[2] = ["f(Q) = lim x-> Q f(x)", "f(x) does not have any jumps, holes, asymptotes, or cusps at Q", "L = lim h->0 [f(Q+h)-f(Q)]/h exists"]
q[2] = "What is the definition of a function being differentiable at a point Q?"
quiz[3] = ["Yes, Yes", "Yes, No", "No, Yes", "No, No"]
q[3] = "Can a differentiable function not be continuous? Can a continuous function not be differentiable?"
quiz[4] = ["If you can draw the function near x=a, y=f(a) without needing to lift up a pen", "If the function has no jumps, holes or asymptotes near x=a", "If for all positive e values, there is some positive d value such that the following is true:'if 0<|x-a|<d, then |f(x)-f(a)|<e' ", "If for all positive d values, there is some positive e value such that the following is true:'if 0<|x-a|<d, then |f(x)-f(a)|<e' "]
q[4] = "What is the best definition of a function f being continuous at the point ( a,f(a) )?"
quiz[5] = ["If it does not oscillate when converging [is monotonic]", "If we are 100% sure that it converges to something.", "If the sum of the absolute values converge", "If the absolute values of the sum converge"]
q[5] = "What is the difference between a series converging and a series converging absolutely?"
quiz[6] = ["Fundamental Theorem of Calculus", "L'Hôpital's Theorem", "Cauchy's Integration Theorem", "Bolzano-Weierstrass Theorem"]
q[6] = "What is the name of the theorem that unites differentiation and integration?"
quiz[7] = ["Because complex thing* complex thing is a real thing", "Because math is then closed under its usual operations", "Because physicists are happy and can use it", "Because it actually makes math harder and mathematicians love harder versions of things they know."]
q[7] = "Why are complex numbers required for math to 'make sense' with itself?"
quiz[8] = ["If for any converging sequence in the set, that its limit point converges to a value in the set","If the set is not open", "If the set does not contain any isolated points (Such as [1,2]U{3} on the reals)", "If the set is equipped with a metric space."]
q[8] ="What is a closed set?"
quiz[9] = ["If it has a finite number of elements, then the set is compact","If it is both closed and bounded, then the set is compact.", "If for any collection of subsets of the set, if we can contain every element of the main set with a finite number of subsets; then the main set is compact."]
q[9] = "What makes any set compact? Choose the best defintion."
quiz[10] = ["Heine-Borel Theorem", "Liouville's Theorem", "Bolzano-Weierstrass Theorem", "Fermat's Little Theorem"]
q[10] = "What is the name of the theorem that states that any closed and bounded set in R^n (N-dimensional real space) is compact?"
quiz[11] = ['2', '3', '4', '5', '6', '1']
q[11] = "What is the highest degree of polynomial that is guaranteed to be able to find all of its roots algebraically?"
quiz[12] = ["Cauchy-Kovalevskaya theorem", "Cauchy-Peano theorem", "Cauchy interlacing theorem", "Cauchy's complex integral formula"]
q[12] = "Which theorem of Cauchy is most occasionally useful when integrating some real-valued functions?"
answer_key = [2, 1, 2, 2, 2, 2, 0, 1, 0, 2, 0, 2, 3]
SE:dict[str, Stock|dict[str,float]|float|int|bool] = {}
SE['Self']= [0, 0,{}, True, False, 0, 0, 0] #Capital, year, portfolio [ticker-> percent owned], if can be robbed, if has been robbed, how much has been taken, Exigent questions answered right, net worth
cgn = r.SystemRandom()
def pulseEvent(success_chance:float = 100)-> bool:
    rng = cgn.randint(1,10000)% 100
    return rng<=success_chance
def game(target, margin)-> bool:
    twinput = 'zzz'
    twinput = input("Press the Enter key to start ")
    while twinput != '':twinput = input("False start. Press the enter key to start.")
    start_time = time.time()
    print("Now, press Enter again to confirm your time.")
    input()
    dur = time.time() - start_time
    mT = target-margin
    MT = target + margin
    print(f"\nTime elapsed: {dur:.2f} seconds.")
    if mT <= dur <= MT:return True
    else:return False
def JaFirst():
    print('\n Date: January 1st. \n Your vice president walks into your office, saying')
    print('\n "Congrats on keeping this firm afloat this year, boss! Did you forget to save the presentation from yesterday?"')
    c = input('\n Save? (Y/N) \n')
    while c not in {'Y', 'N'}:
        print('\n Please only return capital Y for yes or capital N for no.')
        c = input('\n Save? (Y/N) \n')
    if c == 'Y': save()
def Wait():
    print("\n Your current amount of cash on hand is $"+str(SE['Self'][0])+'M; the current net worth of your firm is $'+str(SE['Self'][-1])+'M.')
    print("\n Press Enter Key to Proceed.")
    while input() != '': pass
def yearlyEventChain(id=SE):
    if SE['Self'][1]==1:JaFirst()
    Wait()
    def JaTwentySeven():
        print("Date: January 27th. \n You follow up on your New Years Resolution, making good progress into it.")
        for key in SE['Self'][2]:
            SE[key][0].cvr += 0.02
    if pulseEvent(33):
        JaTwentySeven()
        Wait()
    def FEight():
        print('\n Date: February 8th. \n As you walk out of your office for lunch, a rural woman asks you to hold her crates of eggs for an hour.')
        c = input("\n Will you (return) her eggs properly or (cook) them for your staff? \n")
        while c not in {'return', 'cook'}:
            print('\n Please type either return or cook as your option.')
            c = input("\n Will you (return) her eggs properly or (cook) them for your staff? \n")
        if c == 'return':
            for key in id['Self'][2]:
                id[key][0].cvr += 0.01
            print('\n The woman came back and thanked you for your time; telling her neighbors later.')
        else:
            target = r.choice(list(id['Self'][2]))
            id[target][0].satisfaction+=0.1
            id[target][0].cvr=-1
            print('\n The woman came back and saw you crack the last of her eggs into a skillet. She lambasted you, with a reporter overhearing the commotion.')
            print('\n Your employees; however, were pleasantly suprised with your finnesse as you made them lunch.')
            #choose a random company in portfolio. 
            #Employee satisfaction increases by 5%, CVR = -1.
    if pulseEvent(25): 
        FEight()
        Wait()
    def FTwentyNine():
        print('\n Date: February 29th. \n Working an extra day makes your managers irate, irking your employees.')
        for key in SE['Self'][2]:SE[key][0].satisfaction-=0.02
    if pulseEvent(25):
        FTwentyNine()
        Wait()
    def MNine(id=SE):
        print('\n Date: March 9th. \n You tell your managers that your employees are able to take today off. \n')
        c = input("Were you being (honest) or (duplicitous)?\n")
        while c not in {'honest', 'duplicitous'}:
            print('Please respond with either honest or duplicitous. \n')
            c = input("Were you being (honest) or (duplicitous)?\n")
        if c == 'honest':
            print("The managers eagerly run out of the meeting room to evict their subordinates from the office.")
            for key in id['Self'][2]:id[key][0].satisfaction+=0.02
        else:
            print("The managers sigh, tired of your games as they return to work. \n")
            multiplyFlag = True
    if pulseEvent(20):
        MNine(id)
        Wait()
    def ATen():
        print('\n Date: April 10th. \n As you walk home, you pass a seedy alleyway. You only see a pair of green eyes as a voice calls out,')
        print('\n "Are you jealous of a certain company and their worth? I can fix that."')
        cOne = input("\n Do you approach the person(?)? [Y/N] \n")
        while cOne not in {'Y', 'N'}:
            print("\nPlease only type capital Y or capital N ")
            cOne = input("\n Do you approach the person(?)? [Y/N] \n")
        if cOne == 'Y':
            print('\n "I knew you were like me. Which one should I spite?"')
            cTwo = input("\nWhich Ticker will you spite? \n")
            while cTwo not in SE.keys():
                print("\n The ticker must be a valid ticker, such as A, Q, Z, ...")
                cTwo = input("\nWhich Ticker will you spite? \n")
            SE[cTwo][1]*=0.95
            target = r.choice(list(SE['Self'][2]))
            SE[target][1]*=0.95
            print('\n "I did as you asked, but it cost you something." You walk out of the alley to your home, but feel goosebumps even the day after.' )
        else:
            print('\n You walk pass the alleyway, only faintly able to overhear curses.')
    ATen()
    Wait()
    def MySixteen():
        if SE['Self'][3]:
            the = (cgn.randint(1,1000)%8 + 1)/100
            print('Date: May 16th. \n While slacking off at the office, you notice something at the edge of the security cameras.')
            print('There is a faint yellow color on the vault camera! \n You dash over, but only see an emptier vault.')
            SE['Self'][4] = True
            SE['Self'][5] += the
            SE['Self'][0] -= the
        else:
            print('Date: May 16th. \n While slacking off at the office, you recall catching the thief from a while ago.')
            print("You snicker and enjoy your afternoon.")
    if pulseEvent(35):
        MySixteen()
        Wait()
    def JFive():
        cringe = ['L','U','N','A','R','I','S']
        target = r.choice(cringe)
        print('\n Date: June 5th. \n You try to sleep, but are constantly awoken by a widow and her furious screaming at the moon.')
        print('\n Investors of '+target+ ' also cannot sleep, causing them to sell to lower buyers accidentally in the morning.')
        SE[target][1]*=0.95
    JFive()
    Wait()
    def JSeven():
        print('\n Date: June 7th. \n As you walk home, someone approaches you.')
        choice = input('\n"Good evening. Were you against the events of two nights ago?" [Y/N] \n')
        while choice not in["Y", "N"]:
            choice = input('\n Please input Y or N. \n')
        if choice == 'Y':
            print('\n "Then, do you have a more preferred target for where she yells tonight? She is doing it again today; I will change her mind from her usual routine though."')
            ctwo = input('Choose a company ticker. \n')
            if ctwo not in ['B', 'C', 'D', 'E','F','G','H','J','K','M','O','P','Q','T','V','W','X','Y','Z']or ctwo in ['L','U','N','A','R','I','S']:
                if ctwo in ['L','U','N','A','R','I','S']:
                    ctwo = input('\n"She could have done that one tonight. Quit messing around and tell me your real target." \n')
                else:
                    ctwo = input('\n"Even I know that that is not a company! Choose one." \n')
            print('\n After hearing you confirm your choice, the friend of the widow nods and walks away. You swear you hear faint screaming far off.')
            print('\n Investors of '+ctwo+ ' also cannot sleep, causing them to sell to lower buyers accidentally in the morning.')
        else:
            print('\n Great! She is doing it again today", is what the friend of the widow says before walking away.')
            ctwo = r.choice(['L','U','N','A','R','I','S'])
            print('\n Investors of '+ctwo+ ' also cannot sleep, causing them to sell to lower buyers accidentally in the morning.')
        SE[ctwo][1]*=0.95
    if pulseEvent(33):
        JSeven()
        Wait()
    def JuNine():
        choice = r.choice(list(SE['Self'][2]))
        print("Date: July 9th. \n While on break, you overhear an interview between the usual journalist and an eager child.")
        print('In a hurry, you only overhear one question and answer,\n "How do you feel about company '+choice+'?" \n "It is the strongest around!"')
        print('\n Motivated, you return to the office and try to prove the child correct.')
        SE[choice][0].cvr+= 0.03
        SE[choice][1]*=1.03
    if pulseEvent(11):
        JuNine()
        Wait()
    def JuFourteen():
        print("Date: July 14th. \n The usual reporter meanders through your offices, lookin for a scoop.")
        print("Irritated at their nothing-burger that they currently have, they step outside to find a coworker confessing to another using sunflowers.")
        print("This week's story is `SUNFLOWERS: EFFECTIVE OR JUST A WORSE, YELLOW ROSE?` ")
        print("Your employees find it slightly endearing that they are the focus instead of just you or your actions.")
        for stockStr in SE['Self'][2]:
            SE[stockStr][0].satisfaction+=0.03
    if pulseEvent(10):
        JuFourteen
        Wait()
    def JuFifteen():
        print("Date: July 15th. \n Looking for new interns, you find yourself near the University of Chicago campus.")
        print("Instead of finding someone, your shoulder is tapped from behind. You jump slightly at the unexpected contact as he asks,")
        print('"Hello, I could not help but notice how much you have been around here. Have you been enjoying your stay?"')
        c = input("Reply Yes or No. \n")
        while c not in ["Yes", "No"]:
            c = input("Please input the full word and match the capital letters. \n Yes or No? \n")
        if c=='Yes':
            print('Upon hearing your approval, he beams and replies, "I am glad that you are enjoring your stay! Please give good feedback on the game!"')
            baseFactorFlag = True
        else:
            print('Upon hearing your disapproval, he frowns briefly before recomposing himself, "At least give good feedback, okay?"')
    if SE['Self'][1]==7:
        JuFifteen()
        Wait()
    def JuTwentyThree():
        print('Date: July 23rd. \n While triple checking the accounting ledgers, you spot many compounding rounding errors adding up to 10 million dollars.')
        print('Just before that same journalist as usual could find out, you track the true cash left as capital rather than as expenses.')
        print('No money laundering charges!')
        SE['Self'][0]+=10
    if pulseEvent(20):
        JuTwentyThree
        Wait()
    def AuTwo():
        target = cgn.randint(1,5)
        margin = 0.2
        print("Date: August 8th. \n While walking around a festival's thoroughfare, you see an intriguing game stall.")
        print("Approaching, it is run by a veteran, with the following challenge:\n Cameras are focused on the front of the stall. You fire a BB rifle at a target, aiming to have fired within a certain tolerance of some elapsed time after cocking.")
        print('The vet describes the current parameters as such, "Good evening. Today, you will be aiming for '+str(target)+' seconds, with an error of +/-'+ str(margin)+ 's margin of error."')
        truth = game(target, margin)
        if truth:
            if margin<= 0.05: margin /=2
            else: margin -=0.05
            SE['Self'][0]+=2.89*(.75+0.05/margin)
            print("The vet lauds your efforts as you return home for the day. Tomorrow, he returns as an investor? Small world, am I right?")
        else: print("He shrugs, not having expected many people to succeed this year.")
    if pulseEvent(52):
        AuTwo()
        Wait()
    def AuSix():
        print("Date: August 6th \n Passing through a quaint neck of the woods, you overhear the typical reporter, desperate for information.")
        print("However, instead of asking you scathing questions, they are... divining them?")
        target = input("Which company do you hear them divining about? \n")
        while target not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("Please input a valid ticker symbol.")
            target = input("Which company? \n")
        comp = SE[target][0]
        prePro = comp.function(comp.start_year).hyperbolic_length()
        mp = round(prePro,2)
        hQ = round((((comp.predictedValue()*(1+comp.r_factor/100)**SE['Self'][1]) - (comp.predictedCost() - SE['Self'][1]*comp.m_factor))+mp)/2, 2)
        lQ = round((((comp.predictedValue()*(1-comp.r_factor/100)**SE['Self'][1]) - (comp.predictedCost() + SE['Self'][1]*comp.m_factor))+mp)/2, 2)
        print("The divnination is as follows: 'Company "+target+" has would have a base 25% chance to earn "+str(lQ)+" or lower, 50% to earn "+str(mp)+" or more, and 75% chance to earn "+ str(hQ)+" or less.")
        print("Satisfied, you sneak off before the reporter notices that you overheard the diviniation.")
    if pulseEvent(5):
        AuSix()
        Wait()
    def AuEight():
        print('Date: August 8th. \n You spend nearly an eternity staring at a large endangered butterfly. You find it to be a good omen.')
    if pulseEvent(88):
        AuEight()
        Wait()
    def AuTwenty():
        print('Date: August 20th \n During lunch break, you overhear that usual reporter asking your technicians about their favorite snack.')
        print('They are astonished when met with the answer of cucumbers, as are you. Curious, you buy then try some and feel invigorated.')
        shrinkCostFlag = True
    if pulseEvent(20):
        AuTwenty()
        Wait()
    def SSix():
        power = r.choice([2,2,2,3,3,4])
        target = cgn.randint(2, 10000)
        lb =target**(1/power)//1
        if target**(1/power) == target**(1/power)//1:ub = lb
        else:
            ub = lb + 1
        while lb == ub:
            target = cgn.randint(2, 10000)
            lb =target**(1/power)//1
            if target**(1/power) == target**(1/power)//1:ub = lb
            else:
                ub = lb + 1
        mp = lb+0.5
        point = target**(1/power)
        print('Date: September 6th \n You are testifying before Congress today. Not for racketeering, but because you could be deemed unfit to be in your post.')
        print('Your arbiter asks your question, "For the following number, please state whether the following expression is closest to '+str(lb)+', '+str(ub)+', or their midpoint." ')
        math = input(str(target)+" to the 1/"+str(power)+"th power. [LOW, MID, HIGH]")
        while math not in ["LOW", "MID", "HIGH"]:
            print('\n Please input LOW, MID, or HIGH .')
            math = input(str(target)+" to the 1/"+str(power)+"th power. [LOW, MID, HIGH] \n")
        win = ''
        print(point)
        if point>=mp:
            if point+.25<ub:
                win = 'MID'
            else:
                win = 'HIGH'
        else:
            if point -.25 > lb:
                win = 'MID'
            else:
                win = 'LOW'
        if win == math:
            print("Impressed by your mathematical prowess, the arbiter deems that you are fit in your position. \n The community has increased faith in your companies.")
            noDecayCVRFlag = True
        else:
            print("The arbiter lambasts your inept mathematical skills. However, the community thinks that your treatment was too harsh.")                
    if pulseEvent(50):
        SSix()
        Wait()
    def STwenty():
        if SE['Self'][5]>0:
            print("Date: September 20th. \n Just like a few months ago, you are relaxing in your office.")
            print("You notice the same yellow smudge on the cameras, but run over to your vault in time to catch the thief!")
            print("\n Also, you manage to extort the thief of all of your prior losses in exchange for not reporting them.")
            SE['Self'][3] = False
            SE['Self'][4] = False
            SE['Self'][0] += SE['Self'][5]
            SE['Self'][5] = 0
        else:
            pass
    if pulseEvent(4) and SE['Self'][4]:
        STwenty()
        Wait()
    def OTen():
        print("Date: October 10th. \n You walk into a school program that you are sponsoring. \n You overhear a wisened math teacher ask one of his students a question,")
        print(q[SE['Self'][6]])
        if len(quiz[SE['Self'][6]])==3:
            print(one+' '+quiz[SE['Self'][6]][0])
            print(two+' '+quiz[SE['Self'][6]][1])
            print(three+' '+quiz[SE['Self'][6]][2])
            pass
        elif len(quiz[SE['Self'][6]])==4:
            print(one+' '+quiz[SE['Self'][6]][0])
            print(two+' '+quiz[SE['Self'][6]][1])
            print(three+' '+quiz[SE['Self'][6]][2])
            print(four+' '+quiz[SE['Self'][6]][3])
        else:
            print(one+' '+quiz[SE['Self'][6]][0])
            print(two+' '+quiz[SE['Self'][6]][1])
            print(three+' '+quiz[SE['Self'][6]][2])
            print(four+' '+quiz[SE['Self'][6]][3])
            print(five+' '+quiz[SE['Self'][6]][4])
            print(six+' '+quiz[SE['Self'][6]][5])
        guess = input("Which option choice did the student think corresponds to the correct answer? [1,2,3,...] \n")
        try:
            guess = int(guess)
            if guess -1 == answer_key[SE['Self'][6]]:
                SE['Self'][6]+= 1
                print('You note the enthusiasm of his response as he replies with, "I knew you had it in you! Keep with it!"')
                print("You also manage to apply the results of your new knowledge to your investments, and find a return of 10 million dollars.")
                SE['Self'][0] += 10
            else:
                print('The teacher shakes his head but is not disheartened as he responds, "That is not the correct answer, but this is not the end! Try again next time!"')
                pass
        except:
            print('The teacher chides himself but earnestly responds, "Even if you wrote out the whole definition, the question was multiple choice. You technically get it wrong."')
        SE['Self'][6] = SE['Self'][6]%13
    OTen()
    Wait()
    def NEighteen():
        print("Date: November 18th, the last day before the crunch time of December truly starts. \n Groggily walking to your office, you pass by polar opposites:")
        print("One is a gaudy woman with jewelry seemingly spilling from her outfit; the other is a pauper with not much more than shabby attire.")
        bane = input('Together, they as you, "What would you rather have: [malicious], even pestilent investors or [austere], even poverty ridden customers?" \n')
        while bane not in ["malicious", "austere"]:
            print("Please input either malicious or austere .")
            bane = input('Together, they as you, "What would you rather have: [malicious], even pestilent investors or [austere], even poverty ridden customers?" \n')
        event = cgn.randint(1,8)
        happens = (event>=4 and event<=4)
        if happens:
            if bane == 'austere':
                SE['Self'][0] -= min(50, 0.3*SE['Self'][0])
            else:
                flattedRevFlag = True
        
        print("You shudder with your reply, feeling that not all is quite right as you run off.")
    if pulseEvent(50):
        NEighteen()
        Wait()
def buyRoutine(mayBuy=3):
    print("Date: December 16th. \n You and your associates are looking into modifying your portfolio today.")
    x = mayBuy
    while x>0:
        choice = input("Will you [buy] or [sell] or [quit]? You have "+str(x)+" maximum things left to choose before forcefully quitting. \n")
        while choice not in ['buy', 'sell', 'quit']:
            print("Please enter either buy, sell, or quit.")
            choice = input("Will you [buy] or [sell] or [quit]? You have "+str(x)+" maximum things to do. \n")
        if choice == 'quit':
            x = 0
            pass
        elif choice == 'buy':
            target = input("Which ticker will you buy?\n")
            while target not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print("This is not a ticker. Please try again.")
                target = input("Which ticker will you buy?\n")
            if target in SE['Self'][2]:
                print("Buying more shares of a company that you own:")
                print("The maximum that you can own is "+str(SE[target][-1]*100)+'%; you own '+str(SE['Self'][2][target]*100+'%.'))
                amount = input("How much more stake would you wish to purchase? {Use decimal instead of percent.} \n")
                while type(amount)!= float:
                    try:
                        amount = float(amount)
                        if amount+SE['Self'][2][target]>SE[target][-1]:
                            amount = ''
                            print("This amount is not offered currently. You cannot acquire this much. Please retry.")
                        if amount != '':
                            print("This will cost $"+amount*SE[target][1]+'. Are you sure?')
                            verify = input("[Yes] or [No]? \n")
                            while verify not in ['Yes', 'No']:
                                verify = input("[Yes] or [No]? \n")
                            if verify == 'Yes':
                                SE['Self'][0] -= amount*SE[target][1]
                                SE['Self'][2][target] += amount
                                amount = 0
                            else: break
                    except:
                        amount = input("Please input a decimal number. \n")
            else: 
                rN = cgn.randint(7,30)/10
                priceTargetWhole = rN*SE[target][1]
                print("You are attempting to buy a majority stake in a new company.")
                print("The current net worth of this company is $"+str(SE[target][1])+"M; with a minimum ownership stake of "+str(SE[target][2])+', and a maximum of '+str(SE[target][3]))
                stake = input("In decimal notation, how much stake do you intend to buy? {Cancel w/entering 0}\n")
                while type(stake)==str:
                    try:
                        stake = float(stake)
                        if stake == 0: break
                        elif SE[target][2]>stake or SE[target][3]<stake:
                            print("You tried to purchase an invalid amount. Please try again.")
                            stake = input("In decimal notation, how much stake do you intend to buy? {Cancel w/entering 0}\n")
                    except:
                        print("There was an error in your prior entry. Please keep it like 0.74 or .56 as you try again")
                        stake = input("In decimal notation, how much stake do you intend to buy? {Cancel w/entering 0}\n")
                if stake !=0:
                    priceBid = input("How much will you bid for this amount? \n")
                    while type(priceBid) == str:
                        try:
                            priceBid = float(priceBid)
                            if priceBid >= priceTargetWhole*stake:
                                print("Your bid was accepted.")
                                SE['Self'][0] -= priceBid
                                SE['Self'][2][target]=stake
                            else: print("Your bid was not accepted.")
                        except:
                            print("Please input a number.")
                            priceBid = input("How much will you bid for this amount? \n")
        elif choice == 'sell':
            print("You are trying to sell a stock that you own.")
            print(SE['Self'][2])
            print("Above is the portfolio of your investment firm; the letter is the ticker, and the decimal next to it is how much stake you posess.")
            target = input("Which ticker will you sell?\n")
            while target not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or target not in SE['Self'][2]:
                print("This is not a valid ticker to sell. Please try again.")
                target = input("Which ticker will you sell?\n")
            rN = cgn.randint(7,20)/10
            priceTargetWhole = rN * SE[target][1]
            print("If trying to sell only a portion of your stake, you must still posess a majority in the company for it to be a valid transaction.")
            selloff = input("How much are you trying to sell off? Input [-1] for all of your stake, and any other number for that amount. \n")
            while type(selloff)!= float:
                try:
                    selloff = float(selloff)
                    if SE['Self'][2][target]-selloff<0.5:
                        print("This is not a valid transaction; you would not have a majority afterwards.")
                        selloff = input("How much are you trying to sell off? Input [-1] for all of your stake, and any other number for that amount. \n")
                    elif selloff == -1:print("You are selling off your entire stake.")
                    elif selloff > SE['Self'][2][target]:
                        print("You are trying to sell more stake than you own.")
                        selloff = input("How much are you trying to sell off? Input [-1] for all of your stake, and any other number for that amount. \n")
                except:
                    print("This was not a number. Please try again.")
                    selloff = input("How much are you trying to sell off? Input [-1] for all of your stake, and any other number for that amount. \n")
            if selloff != 0:
                if selloff == -1:
                    selloff = SE['Self'][2][target]
                    priceBid = input("Please submit your asking price in millions of dollars? {Divide your 'real' asking price by a million.} \n")
                    while type(priceBid)== str:
                        try:
                            priceBid = float(priceBid)
                        except:
                            print("This was not a number. Please try again.")
                            priceBid = input("Please submit your asking price in millions of dollars? {Divide your 'real' asking price by a million.} \n")
                    if priceBid<= priceTargetWhole*selloff:
                        print("Sale successful. This net you a profit of $"+str(priceBid)+'M.')
                        SE['Self'][0]+= priceBid
                        del SE['Self'][2][target]
                    else:print("No buyers took your offer on. No sale.")
                else:
                    SE['Self'][2][target] -= selloff
                    SE['Self'][0] += selloff*priceTargetWhole
                    print("The sale got you $"+str(selloff*priceTargetWhole)+'M.')
        x -= 1
def finAdvancement():
    print("Date: December 1st. \n It is time to review the investments made into your companies this year.")
    print("For each of the following, can you tell me how many millions you have invested into ammenities, advertising, and growth this year?")
    print("The example format is 3,4,5 for 3 into ammenities, 4 into ads, and 5 into growth")
    #Make the input a try/except to avoid failed inputs
    investmentSheet:list[str|float]=[]
    for ticker in SE['Self'][2]:
        investmentSheet += [SE[ticker][0].name]
        newData = []
        x = 0
        while x == 0:
            try:
                newData += [float(num) for num in input("How much are you investing into company? \n"+SE[ticker][0].name+'?\n').split(",")]
                while sum(newData)>= SE['Self'][0]:
                    print("You cannot invest more than you currently have in capital. Please try again.")
                    newData = []
                    newData += [float(num) for num in input("How much are you investing into company? \n"+SE[ticker][0].name+'?\n').split(",")]
                SE['Self'][0] -= sum(newData)
                x = 1
            except Exception as e:
                print(e)
                print("Please try again, there appeared to be a flaw in your form.")
        investmentSheet += newData
    print("Date: December 2nd. \n Your investments have been submitted. The following week is when the reports start to enter your office.")
    eoySheet:list[float|str]= [] #store profit of each company & its ticker
    print("Date: December 9th. \n Drowning in paperwork, you manage to spot your end of year reports.")
    i = 0
    while i < len(investmentSheet):
        stock = SE[investmentSheet[i]][0]
        stock.start_year = SE['Self'][1]
        print("Paperwork for Company "+investmentSheet[i]+', Year '+str(stock.start_year)+': \n')

        Satis = max(0, investmentSheet[i+1])
        Commun = max(0, investmentSheet[i+2])
        growth = max(0, investmentSheet[i+3])

        pVal = round(stock.predictedValue(), 2)
        pCost = round(stock.predictedCost(), 2)
        print("Your predicted cost was "+ str(pCost) + 'M, and your predicted revenue was '+str(pVal)+'M.\n')
        minVal = pVal*(1-stock.r_factor/100)**stock.start_year
        maxVal = pVal*(1+stock.r_factor/100)**stock.start_year
        minCost = pCost - stock.start_year*stock.m_factor
        maxCost = pCost + stock.start_year*stock.m_factor
        if flattedRevFlag:maxVal = max(0.7*maxVal, pVal)
        hardmode = False
        if SE['Self'][-1]>=1000:hardmode = True
        if hardmode:
            stock.satisfaction, satisFlag = satis_Impact_Recession(stock.satisfaction, Satis)
            stock.cvr, commFlag = commun_Impact_Recession(stock.cvr, Commun)
        else:
            stock.satisfaction, satisFlag = satis_Impact(stock.satisfaction, Satis)
            stock.cvr, commFlag = commun_Impact(stock.cvr, Commun)
        try:
            y = 1/(1+1/stock.satisfaction) - 3/7
        except:
            y = 4/7
        skew_factor = 1.7*y+0.15
        try:
            x = math.atan(stock.cvr)*1/(math.cos(stock.cvr))**2
        except:
            x = 0
        if x<0:
            revenue_translate = 2-math.e**(-x)
        else:
            revenue_translate =math.e**(x**0.5)
        stock.growth = growth_Impact(stock.growth, growth)
        fnDHO:Callable[[float, float], float] = lambda x,max : -1.2* math.e**(-4*x/(max+0.0000000000001)/5)*math.cos(1.7*x/(max+0.0000000000001) + 1)+1
        if hardmode:
            foci = lambda x: 1/(4*math.pi*math.e*(0.09*(x-8)))
            foe = foci(stock.start_year)
            z = stock.start_year - 8
            fnDHO = lambda x, p: .25 +0.5*math.e**(-math.e*p*x)*math.cos(p*x)+ 2.4581*math.e**(-x*p)*(math.sin(2*x*p))**2
            multiply_revenue = fnDHO(stock.growth, foe)
        else:
            z = r.randint(1,6*stock.start_year)
            multiply_revenue = fnDHO(stock.growth, growth)
        cRv = r.uniform(0,1)
        if baseFactorFlag:
            if cRv + skew_factor >= 7/15:trueCost = r.uniform(minCost, pCost)
            else: trueCost = r.uniform(pCost, maxCost)
        else:
            if cRv + skew_factor >=0.5: trueCost = r.uniform(minCost, pCost)
            else: trueCost = r.uniform(pCost, maxCost)
        if hardmode:trueCost *= 1.2
        trueCost = round(trueCost, 2)
        trueValue = r.uniform(minVal, maxVal)*multiply_revenue+revenue_translate
        trueValue = round(trueValue, 2)
        if shrinkCostFlag:trueCost *=0.95
        if multiplyFlag: trueVal *= 1.01

        print("The revenue generated this year was $"+str(trueValue)+'M, but the cost incurred was $'+str(trueCost)+'M.')
        stock.satisfaction *= 0.9
        stock.satisfaction = round(stock.satisfaction, 2)

        pulseEvent = r.uniform(0,1)
        if pulseEvent >0.98:
            stock.cvr = 0.9
            print("Excellent marketing year. Beneficial results.")
        elif pulseEvent < 0.02:
            stock.cvr = -.9
            print("Horrible marketing year. Putrid results.")
        elif pulseEvent >0.9:
            stock.cvr = .5
            print("Good marketing year. Favorable results.")
        elif pulseEvent <0.1:
            stock.cvr = -.5
            print("Bad marketing year. Improvable results.")
        elif not noDecayCVRFlag:
            stock.cvr *=4/5
            stock.cvr = round(stock.cvr, 2)
            print("Typical marketing year. Average results.")

        if satisFlag: print("Over-invested into facilities. Employees slacked off.")
        if commFlag: print("Over-invested into marketing. Advertisements skipped.")

        if stock.start_year%2==0:
            stock.growth *=2/3
            if hardmode:stock.growth *=3/4
            stock.growth = round(stock.growth, 2)
            print("Your investments have decayed in value.")
        elif z< stock.growth:
            if stock.growth - z > z and stock.start_year<= 10:
                if z == 1:stock.growth = 0
                else:stock.growth = 1
                print("Rival firms noticed how much you spent and successfully stole good expansion targets. A lot of money has been wasted.")
            elif stock.start_year>10:
                if multiply_revenue < 0.75:
                    stock.growth = round(stock.growth*3/4, 2)
                    print("Rival firms noticed how much you spent and successfully stole good expansion targets. A lot of money has been wasted.")
                else:
                    stock.growth = round(stock.growth*7/8, 2)
                    print("A rival firm noticed how much you spent and successfully stole some expansion targets. A portion of money has been wasted.")
            else:
                stock.growth = round(z-(stock.growth-z), 2)
                print("A rival firm noticed how much you spent and successfully stole some expansion targets. A portion of money has been wasted.")
        if multiply_revenue >= 1.4:print("Your firm was able to scale its operations exceedingly better than its peers. growth is high.")
        profit = trueValue - trueCost
        eoySheet.append(profit)
        #print("Debug: Percent owned:"+str(SE['Self'][2][stock.name]))
        #print("Debug: Old Stock Price"+str(SE[stock.name][1]))
        SE[stock.name][1] += round(SE['Self'][2][stock.name]/10*profit,2)
        #print("Debug: New Stock Price"+str(SE[stock.name][1]))
        i += 4
        Wait()
    for stock in stockExchange:
        if stock.start_year!= SE['Self'][1]:
            jitterSatis = cgn.randint(-4,4)/10
            jitterCVR = cgn.randint(-3,3)/10
            jitterNWMultiplier = 1+ra.normal()
            jitterNWMultiplier = min(0.85, jitterNWMultiplier)
            jitterNWMultiplier = max(1.15, jitterNWMultiplier)
            stock.cvr += jitterCVR
            stock.satisfaction += jitterSatis
            SE[stock.name][1]*=jitterNWMultiplier
    if 75>= (cgn.randint(1,100000)%100):buyRoutine()
    
    print("Date: December 25th. \n The interest from the money you have not spent has been calculated and returned as new capital.")
    print("This is to the amount of:")

    if SE['Self'][-1]>=1000:
        print('$'+str(SE['Self'][0]*0.045)+'M')
        SE['Self'][0]*=1.045
    else:
        print('$'+str(SE['Self'][0]*0.03)+'M')
        SE['Self'][0]*=1.03
    Wait()
    print("Date: December 30th. \n The money from throughout your year finally comes in. ")
    SE['Self'][0] += sum(eoySheet)
    print("Your new amount of capital is $"+str(SE["Self"][0])+'M.')
    for stock in SE['Self'][2]:
        SE['Self'][-1]+= SE[stock][1]*SE['Self'][2][stock]
    SE['Self'][-1]+= SE['Self'][0]
    print("Your firm's new net worth is $"+str(SE['Self'][-1])+'M.')
    Wait()
newline:str = ' '
one:str = '1)'
two:str = '2)'
three:str = '3)'
four:str = '4)'
five:str = '5)'
six:str = '6)'
seven:str = '7)'
eight:str = '8)'
nine:str = '9)'
#Dict of all companies & User's Data
##Required: Company Stock {Check StockGamev3.py for a sample of what this means.}
##Make own data into dict: Capital available, year, stocks owned w/ % owned,##If can stolen from, if stolen from so far in game, amount stolen, questions correct, net worth.
A = Stock("A", lambda t: Complex(0.1*(t-7.6)**3-1.2*(t-7.6)**2+140, 0.4*(t-5.9)**2+80.6), 0, 0.85, -0.85, 0, 1.75,2)
SE["A"] = [A, 75, .55, .75]
B = Stock("B", lambda t: Complex(17*math.sqrt(2*t-2)+20, 0.8*t+4.8**(0.1*t)+51), 0, 0.68, -0.25, 0, 1.75,1)
SE["B"] = [B, 90, .51, .62]
C = Stock("C", lambda t: Complex(30*(t-5)/(0.1*(t-5)**2+1)+80, 15*math.sqrt(t)+24), 0, 0.75,  0.15, 0, 1.5,1)
SE["C"] = [C, 120, .51, .55]
D = Stock("D", lambda t: Complex(.03*(t-12)**3+50, 0.75*t+22), 0, 0.78,  0.45, 0, .5,.5)
SE["D"] = [D, 110, .51, .88]
E = Stock("E", lambda t: Complex(80-2.2*math.e**(4-t), 12*math.sqrt(t)+15), 0, 0.92,  0.68, 0, .5,.5)
SE["E"] = [E, 62, 0.53, .79]
F = Stock("F", lambda t: Complex(105-.2*(t-16)**2, 10+.15*(t+6)**2), 0, 0.84,  0.25, 0, 1.8,1)
SE["F"] = [F, 28, 0.61, 0.9]
G = Stock("G", lambda t: Complex(35+4*t+16*math.sin(.5*t), 76-0.1*(t-5)**2), 0, 0.89, -0.08, 0, 1.25,.75)
SE["G"] = [G, 41,.7, .92]
H = Stock("H", lambda t: Complex(4*t+.1*math.e**(t/2-5)+20, 40+.5*(t-11)**2), 0, 0.73,  0.34, 0, 1.75,1.5)
SE["H"] = [H, 85,.66,.86]
I = Stock("I", lambda t: Complex(0.02*(t-11.7)**3+80, 2*t+35), 0, 0.62, -0.21, 0, 1,1.5)
SE["I"] = [I, 74, .63, 0.71]
J = Stock("J", lambda t: Complex(10*math.sqrt(0.8*(t-1))+90, 54/(.5*(t-6.6)**2+1)+83), 0, 0.61, -0.37, 0, .2,.5)
SE["J"] = [J, 68, .52, 0.76]
K = Stock("K", lambda t: Complex(40+2.4*t+.75*t*math.sin(t), .01*(t-12)**3+45), 0, 0.67, -0.62, 0, .75,.75)
SE["K"] = [K, 79, .59,.72]
L = Stock("L", lambda t: Complex(0.002*(t-13.7)**4-0.002*(t-13.7)**2+3.6*t+20, 16*math.sqrt(t)), 0, 0.58, -0.81, 0, 1,1.75)
SE["L"] = [L, 46, .51, .65]
M = Stock("M", lambda t: Complex(-0.005*(t-18.4)**3+0.005*(t-18.4)**2+3.6*t+64, 16.5*math.sqrt(t)+.5*(t-11)+39), 0, 0.90,  0.91, 0, 1,1)
SE["M"] = [M, 53, 0.57, 0.79]
N = Stock("N", lambda t: Complex(0.008*(t-11.1)**3-.15*(t-11.1)**2+.15*t+115, 2*t*math.sin(2*t)+t+80), 0, 0.77,  0.49, 0, .3,1.5)
SE["N"] = [N, 88, .55, .88]
O = Stock("O", lambda t: Complex(-24*math.sin(2*t)/t+2*t+100, .1*(t-10)**2+93), 0, 0.87,  0.46, 0, .2,.75)
SE["O"] = [O, 97, .51, .78]
P = Stock("P", lambda t: Complex(15/(2.75*math.sin(3*t/4)+3.5)+3.5*t+100, t+math.e**(t-21)+120), 0, 0.76,  0.12, 0, .75,.75)
SE["P"] = [P, 142, .51,.89]
Q = Stock("Q", lambda t: Complex(2*t+30+38*(t-6.9)/(1+(t-6.9)**2), 27+t/2-27.5*(t-4.5)/(1+(t-4.5)**2)), 0, 0.67, -0.29, 0, 1,1)
SE["Q"] = [Q, 57, 0.51,  0.55]
R = Stock("R", lambda t: Complex(2*math.sin(t)+10*math.sqrt(t)+35, 2*t+21-75*(t-11.5)/(1+(t-11)**2)), 0, 0.83,  0.74, 0, 1,.1)
SE["R"] = [R, 66, 0.51, 0.72]
S = Stock("S", lambda t: Complex(5+2*t+abs(-23+.5*(t-11)**2), 21+.1*(t-11)**2), 0, 0.62, -0.67, 0, .65,1)
SE["S"] = [S, 32, 0.51, 0.60]
T = Stock("T", lambda t: Complex(10*math.cbrt(7*t-100)+80, 20+2*t+35/(1+.5*(t-12)**2)), 0, 0.94,  0.85, 0, 2,.2)
SE["T"] = [T, 81, 0.51, 0.81]
U = Stock("U", lambda t: Complex(3*math.sqrt(8*math.sin(t)+20)+40+2.5*t, 37+1.5*t+35/(1+.5*(t-3)**2)), 0, 0.59, -0.78, 0, .5,.5)
SE["U"] = [U, 59, .51, 0.66]
V = Stock("V", lambda t: Complex(3*t*math.sin(1.2*t)+100, 67+1.5*t+35/(1+10*(t-1)**2)), 0, 0.94,  0.78, 0, 2.5,.5)
SE["V"] = [V, 95, .56, .82]
W = Stock("W", lambda t: Complex(95+20*math.sin(math.sqrt(20*t)), 71/t+1.5*t+50), 0, 0.65,  0.18, 0, 1.8,.25)
SE["W"] = [W, 100,.63,.88]
X = Stock("X", lambda t: Complex(7*math.sqrt(7*math.sin(t)+7)+t+70, 61+t+5*math.sin(math.sqrt(10*t))), 0, 0.88,  0.97, 0, 1.2,1.6)
SE["X"] = [X, 43, .57,.93]
Y = Stock("Y", lambda t: Complex(80/(1+.1*(t-7)**2)+25-t/3, 20+.8*math.e**(5-t/2)), 0, 0.57, -0.56, 0, 4,.4)
SE["Y"] = [Y, 72, 0.51, 0.63]
Z = Stock("Z", lambda t: Complex(10*math.sin(.07*(t-5)**2)+.15*(t-1)**2+50, math.e**(.2*t+math.sin(t/2))/2+45), 0, 0.93,  0.22, 0, .3,1.5)
SE["Z"] = [Z, 61, .59, .85]
stockExchange = {A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z}#Company index order: company Stock, market cap, min ownable, max ownable.
def save()->None:
    dicion = {}
    for stock in stockExchange:dicion[stock.name] = [stock.start_year, stock.satisfaction, stock.cvr, stock.growth, stock.r_factor, stock.m_factor, SE[stock.name][1]]
    dicion['Self']=SE['Self']
    filename = 'XGNTUISavev1.3.json'
    with open(filename, 'w') as f:json.dump(dicion, f, indent=4)
    print("Successfully saved to "+filename)
def load(filename = 'XGNTUISavev1.3.json'):
    with open(filename, 'r') as f:return json.load(f)
def loadFile(filename = 'XGNTUISavev1.3.json')-> None:
    data = load(filename)
    for key, val in data.items():
        if key == 'Self':
            SE[key] = val
        else:
            stock = SE[key]
            stock[1] = val[-1]
            stock[0].start_year = val[0]
            stock[0].satisfaction = val[1]
            stock[0].cvr = val[2]
            stock[0].growth = val[3]
            stock[0].r_factor = val[4]
            stock[0].m_factor = val[5]
    print("Loaded prior data.")
def resultsSummary():
    print("You lasted until year "+str(SE['Self'][1])+", has a portfolio that included companies "+ str(SE["Self"][2])+", and ended with a net worth of "+str(SE['Self'][-1]))
    if SE['Self'][1]==25:print("You lasted until the end! Thank you for playing all 25 years! Go for a higher net worth!")
def checkEnd():
    if SE['Self'][-1]<0:return True
    return False
def play()->None:  
    for i in range(4):
        print('Loading'+'.'*i+'\n')
    print("Welcome. All inputs will be done by keyboard, and all outputs will be shown here.")
    print("Also, there is no autosave feature; furthermore, only one 'saveslot' at most can exist at once.")
    status:str = ''
    quitFlag:bool = False
    runFlag:bool = True
    while runFlag:
        status = input(one+': New Game\n'+four+': Load Save\n' + nine+': Quit\n')
        if status == '9':
            quitFlag = True
            runFlag = False
            print("Quitting the game.")
            #End program.

        elif status == '4': 
            runFlag = False
            loadFile()
        #Load prior save into data. Play on like new game

        elif status == '1': 
            runFlag = False
            #Actually do nothing. Treat newgame like a transient save unless saved.
    if not quitFlag:
        print("Starting from year "+str(SE['Self'][1]))
        if SE['Self'][1]!=0:print("Your stock portfolio/ownership stake is "+ str(SE['Self'][2]))
        if SE['Self'][0] == 0 :
            cgn = r.SystemRandom()
            seed = cgn.randint(1,10000)
            r.seed(seed+2)
            SE['Self'][0] = 200.0
            options = r.sample(list(set(SE.keys())-{'Self'}), k=5)
            nineFlag:bool = False
            status = ''
            while not nineFlag:
                if status == '' or status == '9':
                    status = input('\n'+one+': Stock 1:' + SE[options[0]][0].name +'\n'+two+': Stock 2:'+ SE[options[1]][0].name +'\n'+three+
                        ': Stock 3:'+ SE[options[2]][0].name+ '\n'+four+': Stock 4:'+SE[options[3]][0].name+'\n'+five+': Stock 5:'+SE[options[4]][0].name+'\n' + seven +': Move to Purchase\n')
                elif status in ['1', '2', '3', '4', '5']:
                    arg = int(status)-1
                    print('\n')
                    print("This company's current Employee Satisfaction is "+ str(100*SE[options[arg]][0].satisfaction)+'%.')
                    print("This company;s current Community Value Rating [CVR] is "+ str(SE[options[arg]][0].cvr)+'.')
                    #print cvr, satisfaction
                    print("Market cap = $"+str(SE[options[arg]][1])+"M")
                    print("Minimum percent to buy is "+str(SE[options[arg]][2]))
                    print("Maximum percent to buy is "+str(SE[options[arg]][3]))
                    while status != '9':
                        status = input(nine+': Return to previous screen. \n') 
                elif status == '7':
                    nineFlag = True
                    print("Moving to purchase round.")
                else: pass
                    
                #Show 5 stocks. For all 5, detail the following:
                ## Cap price, % up for sale, formulae, cvr, sat.
            buyFlag = True
            print("The buying of companies may now proceed.")
            while buyFlag:
                print(options, "are the tickers you may buy, and you have a "+str(SE['Self'][0])+"M balance")
                cart = input("Which company ticker would you add to your cart? Carts may only have one entry at a time. Stop shopping with EXIT. \n")
                if cart == 'EXIT':buyFlag = False
                elif cart not in options: print("Please retry entry. It is, for instance, A, and not 'A' or a.")
                else:
                    while True:
                        percent = input("How much of this company would you wish to buy? Use decimal parts (like 51 for 51%) for stake; and 0 to cancel. \n")
                        try:
                            percent = float(percent)
                        except:
                            print("Please give a number.")
                            percent = -1
                        if percent == 0:
                            break
                        elif percent == -1:
                            pass
                        elif percent>SE[cart][-1] or percent < SE[cart][-2]:
                            print("This is not a valid amount for this company. Its max is "+str(SE[cart][-1])+", and its min is "+str(SE[cart][-2]))
                        elif percent*SE[cart][-3]>SE['Self'][0]:
                            print("You are too broke to afford this amount. Please try a different amount.")
                        else:
                            price = percent*SE[cart][-3]
                            price = ((price*100)//1)/100
                            price = round(price,3)
                            SE['Self'][0] -= price
                            SE['Self'][2][cart] = percent
                            options.remove(cart)
                            print("This company was bought for "+ str(price)+ ' M. \n')
                            break
        while SE['Self'][1]<=24:
            SE['Self'][1] += 1
            yearlyEventChain(SE)
            finAdvancement()
            if checkEnd():
                print("Date: December 31st. \n Despite your best efforts, your firm has become insolvent. You have been fired without compensation.")
                break
            else:JaFirst()
    resultsSummary()
def growth_Impact(score:float, investAmount:float)-> float:
    return score + investAmount
def satis_Impact(score:float, investAmount):
    """Update employee satisfaction based on amount invested."""
    flag = False
    if investAmount >3: 
        flag = True
        investAmount = 3
    while investAmount >0:
        if score <=.5 and investAmount >= 1 : 
            investAmount -= 1
            score += .10
        elif score <= .75 and investAmount >= 1.4: 
            score += .05
            investAmount -= 1.4
        elif score <= .90 and investAmount >= 1.5: 
            score += .025
            investAmount -= 1.5
        elif score >.90 and investAmount >= 1.5:
            score += (1.00-score)/2
            investAmount -= 1.5
        else: investAmount = 0
    return (score, flag)
def satis_Impact_Recession(score:float, investAmount):
    flag2 = False
    if investAmount >3: 
        flag2 = True
        investAmount = 1.5
    while investAmount >0 :
        if score <=.5 and investAmount >= 1 :
            investAmount -= 1
            score += .10
        elif score <= .75 and investAmount >= 1.4:
            score += .05
            investAmount -= 1.4
        elif score <= .90 and investAmount >= 1.5: 
            score += .025
            investAmount -= 1.5
        elif score >.90 and investAmount >= 1.5:
            score += (1.00-score)/2
            investAmount -= 1.5
        else: investAmount = 0
    return (score, flag2)
def commun_Impact(score:float, investAmount):
    """Update CVR based on amount invested."""
    flag = False
    if investAmount >5: 
        flag = True
        investAmount = 5
    while investAmount > 0:
        if score <= -.50 and investAmount >= 1.75:
            score += .1
            investAmount -= 1.75
        elif -.5<=score <= +.25 and investAmount >= .9:
            score += .1
            investAmount -= .9
        elif .25<=score <= .75 and investAmount >= 0.8:
            score +=0.075
            investAmount -= 0.8
        elif investAmount >= math.e/2 and score>=0.75:
            investAmount -= math.e/2
            score += math.e/100 
        else: investAmount = 0
    if score >= 1: score = 1
    return (score, flag)
def commun_Impact_Recession(score:float, investAmount):
    flag = False
    if investAmount >5: 
        flag = True
        investAmount = 2.5
    while investAmount > 0:
        if score <= -.50 and investAmount >= 1.75:
            score += .1
            investAmount -= 1.75
        elif -.5<=score <= +.25 and investAmount >= .9:
            score += .1
            investAmount -= .9
        elif .25<=score <= .75 and investAmount >= 0.8:
            score +=0.075
            investAmount -= 0.8
        elif investAmount >= math.e/2 and score>=0.75:
            investAmount -= math.e/2
            score += math.e/100 
        else: investAmount = 0 
    if score >= 1: score = 1
    return (score, flag)
def run()-> None:
    play()
if __name__ == '__main__':
    run()
#NO TOUCHY. HOW THIS ACTUALLY WORKS
