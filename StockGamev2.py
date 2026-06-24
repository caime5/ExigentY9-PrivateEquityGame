import random as r
from typing import Self, Callable
import math
import json
class Complex:
    def __init__(self, real:float=0, im:float=0):
        self.real=real
        self.imaginary=im
    def __repr__(self):
        return f"{self.real} + {self.imaginary}i"
    def Re(self)->float:
        return self.real
    def Im(self)->float:
        return self.imaginary
    def __add__(self, other:Self)-> Self:
        return(Complex(self.Re()+other.Re(), self.Im()+ other.Im()))
    def hyperbolic_length(self)->float:
        return self.real-self.imaginary

#Step 1: Given equation w/out factoring in investments, update the price. DONE
#Step 1.5: Store equation as lambda-function tied to the ticker of each company. DONE FOR NOW
#Step 2: Incorporate dealing with the investments. DONE
#Step 3: Deal with save/load schenanigans. DONE
#Step 4 (EXTRA): Make into a TUI game. Adapt as well as possible.
"""
Stocks: Dictionary of str to list[Callable(int#Year)->float#Cost, Revenue[0]|int#year[1]|float#Stais[2] (raw percent), 
#Commun[3] (from -1 to 1),, #Growth[4], #r_factor[5], #m_factor[6]]
Represent current value of the parameter, not the modifier nor how much was just invested.
"""

### Formula for stock dicts: Ticker = {Ticker:The callable complex fn, year, Satis, Commun, growth, r, m factors.}
                                   #Yr->Rev-cost
stockList:dict[str, list[Callable[[int],Complex]|int|float]] = {}

stockList["ZRO"] = [lambda t: Complex(0,0), 0, 0, 0, 0, 1.2, 2] #Placeholder/OtherExample/Cardboard Cutout
stockList["A"] = [lambda t: Complex(0.1*(t-7.6)**3-1.2*(t-7.6)**2+140, 0.4*(t-5.9)**2+80.6), 0, 0.85, -0.85, 0, 1.75,2]
stockList["B"] = [lambda t: Complex(17*math.sqrt(2*t-2)+20, 0.8*t+4.8**(0.1*t)+51), 0, 0.68, -0.25, 0, 1.75,1]
stockList["C"] = [lambda t: Complex(30*(t-5)/(0.1*(t-5)**2+1)+80, 15*math.sqrt(t)+24), 0, 0.75,  0.15, 0, 1.5,1]
stockList["D"] = [lambda t: Complex(.03*(t-12)**3+50, 0.75*t+22), 0, 0.78,  0.45, 0, .5,.5]
stockList["E"] = [lambda t: Complex(80-2.2*math.e**(4-t), 12*math.sqrt(t)+15), 0, 0.92,  0.68, 0, .5,.5]
stockList["F"] = [lambda t: Complex(105-.2*(t-16)**2, 10+.15*(t+6)**2), 0, 0.84,  0.25, 0, 1.8,1]
stockList["G"] = [lambda t: Complex(35+4*t+16*math.sin(.5*t), 76-0.1*(t-5)**2), 0, 0.89, -0.08, 0, 1.25,.75]
stockList["H"] = [lambda t: Complex(4*t+.1*math.e**(t/2-5)+20, 40+.5*(t-11)**2), 0, 0.73,  0.34, 0, 1.75,1.5]
stockList["I"] = [lambda t: Complex(0.02*(t-11.7)**3+80, 2*t+35), 0, 0.62, -0.21, 0, 1,1.5]
stockList["J"] = [lambda t: Complex(10*math.sqrt(0.8*(t-1))+90, 54/(.5*(t-6.6)**2+1)+83), 0, 0.61, -0.37, 0, .2,.5]
stockList["K"] = [lambda t: Complex(40+2.4*t+.75*t*math.sin(t), .01*(t-12)**3+45), 0, 0.67, -0.62, 0, .75,.75]
stockList["L"] = [lambda t: Complex(0.002*(t-13.7)**4-0.002*(t-13.7)**2+3.6*t+20, 16*math.sqrt(t)), 0, 0.58, -0.81, 0, 1,1.75]
stockList["M"] = [lambda t: Complex(-0.005*(t-18.4)**3+0.005*(t-18.4)**2+3.6*t+64, 16.5*math.sqrt(t)+.5*(t-11)+39), 0, 0.90,  0.91, 0, 1,1]
stockList["N"] = [lambda t: Complex(0.008*(t-11.1)**3-.15*(t-11.1)**2+.15*t+115, 2*t*math.sin(2*t)+t+80), 0, 0.77,  0.49, 0, .3,1.5]
stockList["O"] = [lambda t: Complex(-24*math.sin(2*t)/t+2*t+100, .1*(t-10)**2+93), 0, 0.87,  0.46, 0, .2,.75]
stockList["P"] = [lambda t: Complex(15/(2.75*math.sin(3*t/4)+3.5)+3.5*t+100, t+math.e**(t-21)+120), 0, 0.76,  0.12, 0, .75,.75]
stockList["Q"] = [lambda t: Complex(2*t+30+38*(t-6.9)/(1+(t-6.9)**2), 27+t/2-27.5*(t-4.5)/(1+(t-4.5)**2)), 0, 0.67, -0.29, 0, 1,1]
stockList["R"] = [lambda t: Complex(2*math.sin(t)+10*math.sqrt(t)+35, 2*t+21-75*(t-11.5)/(1+(t-11)**2)), 0, 0.83,  0.74, 0, 1,.1]
stockList["S"] = [lambda t: Complex(5+2*t+abs(-23+.5*(t-11)**2), 21+.1*(t-11)**2), 0, 0.62, -0.67, 0, .65,1]
stockList["T"] = [lambda t: Complex(10*math.cbrt(7*t-100)+80, 20+2*t+35/(1+.5*(t-12)**2)), 0, 0.94,  0.85, 0, 2,.2]
stockList["U"] = [lambda t: Complex(3*math.sqrt(8*math.sin(t)+20)+40+2.5*t, 37+1.5*t+35/(1+.5*(t-3)**2)), 0, 0.59, -0.78, 0, .5,.5]
stockList["V"] = [lambda t: Complex(3*t*math.sin(1.2*t)+100, 67+1.5*t+35/(1+10*(t-1)**2)), 0, 0.94,  0.78, 0, 2.5,.5]
stockList["W"] = [lambda t: Complex(95+20*math.sin(math.sqrt(20*t)), 71/t+1.5*t+50), 0, 0.65,  0.18, 0, 1.8,.25]
stockList["X"] = [lambda t: Complex(7*math.sqrt(7*math.sin(t)+7)+t+70, 61+t+5*math.sin(math.sqrt(10*t))), 0, 0.88,  0.97, 0, 1.2,1.6]
stockList["Y"] = [lambda t: Complex(80/(1+.1*(t-7)**2)+25-t/3, 20+.8*math.e**(5-t/2)), 0, 0.57, -0.56, 0, 4,.4]
stockList["Z"] = [lambda t: Complex(10*math.sin(.07*(t-5)**2)+.15*(t-1)**2+50, math.e**(.2*t+math.sin(t/2))/2+45), 0, 0.93,  0.22, 0, .3,1.5]
#Will have about 24 more stocks.
 
def loadFile()->None:
    """
    Purpose:Load in progress from previous instance.
    """
    data = load()
    for key, val in data.items():
        if key in stockList:
            fn = stockList[key][0]
            stockList[key] = [fn]+ val
    print("Loaded Previous Data.")
    for key, value in stockList.items():
        print(f"{key}: {value}")
def load():
    filename = 'ExigentFinanceGameData.json'
    with open(filename, 'r') as f:
        return json.load(f)
def saveAsFile()->None:
    """
    Purpose: Save progress to be loaded in the next session.
    """
    dicion = {key: val[1:] for key, val in stockList.items()}
    filename = 'ExigentFinanceGameData.json'
    with open(filename, "w") as f:
        json.dump(dicion, f, indent=4)
    print(f"All progress saved successfully to '{filename}.")

def satis_Impact(score:float, investAmount)->float:
    """Update employee satisfaction based on amount invested."""
    if investAmount >3: 
        print("{Mark?} Over-invested into facilities. Employees slacked off.")
    while investAmount >0:
        if score <=.5 and investAmount >= 1 : #x_1 undetermined as of now
            investAmount -= 1
            score += .10
        elif score <= .75 and investAmount >= 1.4: #Also unknown
            score += .05
            investAmount -= x_2
        elif score <= .90 and investAmount >= 1.5: #Still unknown
            score += .025
            investAmount -= x_3
        elif score >.90 and investAmount >= 1.5: #Do I need to type it again?
            score += (1.00-score)/2
            investAmount -= x_4
        else: #Break the loop
            investAmount = 0
    return score
def commun_Impact(score:float, investAmount)->float:
    """Update CVR based on amount invested."""
    if investAmount >5: 
        print("{Not sure if this should be Mark:} Over-invested into marketing.")
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
    
    if score >= 1: 
        score = 1
    return score
def growth_Impact(score:float, investAmount)->float:
    """Increase growth factor based on the amount invested."""
    return score + investAmount

def adv_year(ticker:str, Satis:float, Commun:float, growth:float)-> None:
    """
    In terms of millions, how much will the ticker increase in this year if the following amounts are invested into them.
    """
    if ticker not in stockList.keys():raise ValueError("Input a ticker of an actual company, please.")

    stockList[ticker][1]+=1
    output = stockList[ticker][0](stockList[ticker][1])
    predicted_value = output.real
    predicted_cost  = output.Im()

    min_rev = predicted_value*(1-stockList[ticker][5]/100)**stockList[ticker][1]
    max_rev = predicted_value*(1+stockList[ticker][5]/100)**stockList[ticker][1]
    min_cost = predicted_cost-stockList[ticker][1]*stockList[ticker][6]
    max_cost = predicted_cost+stockList[ticker][1]*stockList[ticker][6]


    stockList[ticker][2] = satis_Impact(stockList[ticker][2], Satis)
    try:
        y = 1/(1+1/stockList[ticker][2])-3/7
    except:
        y = 4/7
    skew_factor = 1.7*y+.15

    stockList[ticker][3]= commun_Impact(stockList[ticker][3], Commun)
    try:
        x = math.atan(stockList[ticker][3])*1/(math.cos(stockList[ticker][3]))**2
    except:
        x = 0
    if x <0: revenue_translate = 2-math.e**(-x)
    else:revenue_translate = math.e**(x**0.5)

    stockList[ticker][4] = growth_Impact(stockList[ticker][4], growth)
    fnDHO:Callable[[float, float],float] = lambda x, max : -1.8* math.e**(-4*x/max/5)*math.cos(1.7*x/max + 1)+1
    z = r.randint(1,6*stockList[ticker][1])
    multiply_revenue = fnDHO(stockList[ticker][4], z)

    cRv = r.uniform(0,1)
    if cRv+skew_factor >=0.5:trueCost = r.uniform(min_cost, predicted_cost)
    else:trueCost = r.uniform(predicted_cost, max_cost)
    trueCost= round(trueCost, 2)

    trueValue = r.uniform(min_rev, max_rev)*multiply_revenue+revenue_translate
    trueValue = round(trueValue,2)
    print('{Mark:} The revenue generated this year was $'+str(trueValue)+'M, but the cost incurred was $'+str(trueCost)+'M.')
    
    stockList[ticker][2]*= 0.9
    stockList[ticker][2]=round(stockList[ticker][2], 2)

    pulseEvent = r.uniform(0,1)
    if pulseEvent >0.98: 
        stockList[ticker][3] = 0.9
        print("{Mark:} Excellent marketing year. Beneficial results.")
    elif pulseEvent <0.02: 
        stockList[ticker][3] = -0.9
        print("{Mark:} Horrific marketing year. Putrid results.")
    elif pulseEvent >.9: 
        stockList[ticker][3] = .5
        print("{Mark:} Good enough marketing year. Passable results.")
    elif pulseEvent <0.1: 
        stockList[ticker][3] = -0.5
        print("{Mark:} Poor marketing year. Improvable results.")
    else: 
        stockList[ticker][3] *= 4/5
        stockList[ticker][3] = round(stockList[ticker][3], 2)
        print("{Mark:} Typical marketing year. Average results.")    

    #Decay of growth. Have drop by a flat amount if 1) year is even and below the crest of 2) if year is odd.
    if stockList[ticker][1]%2==0: 
        stockList[ticker][4] *= 2/3
        stockList[ticker][4]=round(stockList[ticker][4], 2)
        print("{Mark:} Your investments in expansion have decayed in value.")
    #Decay amount flatly from invest. Rather large to let them try again.
    elif z < stockList[ticker][4]: 
        if stockList[ticker][4]-z>z:
            if z == 1: stockList[ticker][4]=0
            else:stockList[ticker][4] = 1
            print("{Mark:} A rival firm noticed how much you spent and successfully stole good expansion targets. A lot of money has been wasted.")
        else:
            stockList[ticker][4] = round(z - (stockList[ticker][4]-z),2)
            print("{Mark:} A rival firm noticed how much you spent and successfully stole some expansion targets. A portion of money has been wasted.")
    if multiply_revenue>=1.4: print("{Mark:} Your firm was able to scale its operations exceedingly better than its peers. Growth is high.")
    #decay amount to shove them past the crest and then some. 

    print("{Mark:} Your current CVR is "+str(stockList[ticker][3])+", and your current employee satisfaction rating is "+str(stockList[ticker][2])+'.')
    #print("{Mark:} Your predicted profits this quarter would have been $"+str(output.hyperbolic_length())+"M")
    print("{Mark:} Your predicted revenue this year was $"+str(round(output.Re(),2))+"M, and your predicted costs were $"+ str(round(output.Im(),2))+"M.")
    ## Print what the predicted profit would have been for this turn.

    pass
##Idea: Make a function into the load() routine s.t. all companies are then set to have finished X years. #For introducing new-ish companies after some sessions.
def time_travel(destination:int)->None:
    """

    """
    loadFile()
    for key in stockList:
        if destination>= stockList[key][1] and key!="ZRO":stockList[key][1] = destination
        elif key !="ZRO": raise ValueError("Wanting to return to a year that company "+key+" has already completed. Maybe try advancing to year "+str(stockList[key][1]))

#Update reset() whenever more functions are added.
def reset()->None:
    """
    Reset all data to year 0. WARNING:WILL DELETE OLD SAVE.
    """
    stockList["ZRO"] = [lambda t: Complex(0,0), 0, 0, 0, 0, 1.2, 2]
    stockList["A"] = [lambda t: Complex(0.1*(t-7.6)**3-1.2*(t-7.6)**2+140, 0.4*(t-5.9)**2+80.6), 0, 0.85, -0.85, 0, 1.75,2]
    stockList["B"] = [lambda t: Complex(17*math.sqrt(2*t-2)+20, 0.8*t+4.8**(0.1*t)+51), 0, 0.68, -0.25, 0, 1.75,1]
    stockList["C"] = [lambda t: Complex(30*(t-5)/(0.1*(t-5)**2+1)+80, 15*math.sqrt(t)+24), 0, 0.75,  0.15, 0, 1.5,1]
    stockList["D"] = [lambda t: Complex(.03*(t-12)**3+50, 0.75*t+22), 0, 0.78,  0.45, 0, .5,.5]
    stockList["E"] = [lambda t: Complex(80-2.2*math.e**(4-t), 12*math.sqrt(t)+15), 0, 0.92,  0.68, 0, .5,.5]
    stockList["F"] = [lambda t: Complex(105-.2*(t-16)**2, 10+.15*(t+6)**2), 0, 0.84,  0.25, 0, 1.8,1]
    stockList["G"] = [lambda t: Complex(35+4*t+16*math.sin(.5*t), 76-0.1*(t-5)**2), 0, 0.89, -0.08, 0, 1.25,.75]
    stockList["H"] = [lambda t: Complex(4*t+.1*math.e**(t/2-5)+20, 40+.5*(t-11)**2), 0, 0.73,  0.34, 0, 1.75,1.5]
    stockList["I"] = [lambda t: Complex(0.02*(t-11.7)**3+80, 2*t+35), 0, 0.62, -0.21, 0, 1,1.5]
    stockList["J"] = [lambda t: Complex(10*math.sqrt(0.8*(t-1))+90, 54/(.5*(t-6.6)**2+1)+83), 0, 0.61, -0.37, 0, .2,.5]
    stockList["K"] = [lambda t: Complex(40+2.4*t+.75*t*math.sin(t), .01*(t-12)**3+45), 0, 0.67, -0.62, 0, .75,.75]
    stockList["L"] = [lambda t: Complex(0.002*(t-13.7)**4-0.002*(t-13.7)**2+3.6*t+20, 16*math.sqrt(t)), 0, 0.58, -0.81, 0, 1,1.75]
    stockList["M"] = [lambda t: Complex(-0.005*(t-18.4)**3+0.005*(t-18.4)**2+3.6*t+64, 16.5*math.sqrt(t)+.5*(t-11)+39), 0, 0.90,  0.91, 0, 1,1]
    stockList["N"] = [lambda t: Complex(0.008*(t-11.1)**3-.15*(t-11.1)**2+.15*t+115, 2*t*math.sin(2*t)+t+80), 0, 0.77,  0.49, 0, .3,1.5]
    stockList["O"] = [lambda t: Complex(-24*math.sin(2*t)/t+2*t+100, .1*(t-10)**2+93), 0, 0.87,  0.46, 0, .2,.75]
    stockList["P"] = [lambda t: Complex(15/(2.75*math.sin(3*t/4)+3.5)+3.5*t+100, t+math.e**(t-21)+120), 0, 0.76,  0.12, 0, .75,.75]
    stockList["Q"] = [lambda t: Complex(2*t+30+38*(t-6.9)/(1+(t-6.9)**2), 27+t/2-27.5*(t-4.5)/(1+(t-4.5)**2)), 0, 0.67, -0.29, 0, 1,1]
    stockList["R"] = [lambda t: Complex(2*math.sin(t)+10*math.sqrt(t)+35, 2*t+21-75*(t-11.5)/(1+(t-11)**2)), 0, 0.83,  0.74, 0, 1,.1]
    stockList["S"] = [lambda t: Complex(5+2*t+abs(-23+.5*(t-11)**2), 21+.1*(t-11)**2), 0, 0.62, -0.67, 0, .65,1]
    stockList["T"] = [lambda t: Complex(10*math.cbrt(7*t-100)+80, 20+2*t+35/(1+.5*(t-12)**2)), 0, 0.94,  0.85, 0, 2,.2]
    stockList["U"] = [lambda t: Complex(3*math.sqrt(8*math.sin(t)+20)+40+2.5*t, 37+1.5*t+35/(1+.5*(t-3)**2)), 0, 0.59, -0.78, 0, .5,.5]
    stockList["V"] = [lambda t: Complex(3*t*math.sin(1.2*t)+100, 67+1.5*t+35/(1+10*(t-1)**2)), 0, 0.94,  0.78, 0, 2.5,.5]
    stockList["W"] = [lambda t: Complex(95+20*math.sin(math.sqrt(20*t)), 71/t+1.5*t+50), 0, 0.65,  0.18, 0, 1.8,.25]
    stockList["X"] = [lambda t: Complex(7*math.sqrt(7*math.sin(t)+7)+t+70, 61+t+5*math.sin(math.sqrt(10*t))), 0, 0.88,  0.97, 0, 1.2,1.6]
    stockList["Y"] = [lambda t: Complex(80/(1+.1*(t-7)**2)+25-t/3, 20+.8*math.e**(5-t/2)), 0, 0.57, -0.56, 0, 4,.4]
    stockList["Z"] = [lambda t: Complex(10*math.sin(.07*(t-5)**2)+.15*(t-1)**2+50, math.e**(.2*t+math.sin(t/2))/2+45), 0, 0.93,  0.22, 0, .3,1.5]
    saveAsFile()
