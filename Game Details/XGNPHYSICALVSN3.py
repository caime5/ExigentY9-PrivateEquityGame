import random as r
from typing import Self, Callable
import math
import json
import copy
"""
This is a slightly different game version than the other physical one present in this directory. This is because the Stock Class was implemented in this version.
Switch at your own leisure; you will need to rename saves or otherwise modify the save functionality though if you wish to swap them.
"""
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

class Stock:
    def __init__(self, name:str, function:Callable[[int], Complex], start_year:int, satisfaction:float, cvr:float, growth:float, r_factor:float, m_factor:float):
        self.name = name
        self.function = function
        self.start_year = start_year
        self.satisfaction = satisfaction
        self.cvr = cvr
        self.growth = growth
        self.r_factor = r_factor
        self.m_factor = m_factor
    def __eq__(self, other):
        if not isinstance(other,Stock):
            return False
        return self.name == other.name
    def printEq(self):
        try:
            source = dill.source.getsource(self.function)
            print(source.strip(','))
        except Exception as e:
            print(f"Error: {e}")
    def __hash__(self): #Set making/equivalence
        return hash(self.name)
    def __str__(self):
        return "This is the stock of Ticker "+self.name
    def __repr__(self):
        return str([self.name, self.start_year, self.satisfaction, self.cvr, self.growth, self.r_factor, self.m_factor])
    def predictedCost(self):
        return self.function(self.start_year).Im()
    def predictedValue(self):
        return self.function(self.start_year).Re()
    def predictedProfit(self):
        return -self.predictedCost + self.predictedValue

def saveAsFile()->None:
    dicion:dict[str, list[float|int]]
    for stock in stockExchange:
        dicion[stock.name] = [stock.start_year, stock.satisfaction, stock.cvr, stock.growth, stock.r_factor, stock.m_factor]
    filename = 'ExigentFinanceGameDatav3.json'
    with open(filename, "w") as f:
        json.dump(dicion, f, indent=4)
    print(f"All progress saved successfully to '{filename}.")
def load(name = 'ExigentFinanceGameDatav3.json'):
    filename = name
    with open(filename, 'r') as f:
        return json.load(f)
def loadFile(name = 'ExigentFinanceGameDatav3.json'):
    data = load(name)
    for key, val in data.items():
        for stock in stockExchange:
            if stock == B and key == "B":
                print(B.name, B.start_year, B.satisfaction, B.cvr, B.growth, B.r_factor, B.m_factor)
            if key == stock.name:
                stock.name = key 
                stock.start_year = val[0]
                stock.satisfaction = val[1]
                stock.cvr = val[2]
                stock.growth =val[3]
                stock.r_factor = val[4]
                stock.m_factor = val[5]
    print("Loaded Previous Data.")
    for stock in stockExchange:
        print(repr(stock))


A = Stock("A", lambda t: Complex(0.1*(t-7.6)**3-1.2*(t-7.6)**2+140, 0.4*(t-5.9)**2+80.6), 0, 0.85, -0.85, 0, 1.75,2)
B = Stock("B", lambda t: Complex(17*math.sqrt(2*t-2)+20, 0.8*t+4.8**(0.1*t)+51), 0, 0.68, -0.25, 0, 1.75,1)
C = Stock("C", lambda t: Complex(30*(t-5)/(0.1*(t-5)**2+1)+80, 15*math.sqrt(t)+24), 0, 0.75,  0.15, 0, 1.5,1)
D = Stock("D", lambda t: Complex(.03*(t-12)**3+50, 0.75*t+22), 0, 0.78,  0.45, 0, .5,.5)
E = Stock("E", lambda t: Complex(80-2.2*math.e**(4-t), 12*math.sqrt(t)+15), 0, 0.92,  0.68, 0, .5,.5)
F = Stock("F", lambda t: Complex(105-.2*(t-16)**2, 10+.15*(t+6)**2), 0, 0.84,  0.25, 0, 1.8,1)
G = Stock("G", lambda t: Complex(35+4*t+16*math.sin(.5*t), 76-0.1*(t-5)**2), 0, 0.89, -0.08, 0, 1.25,.75)
H = Stock("H", lambda t: Complex(4*t+.1*math.e**(t/2-5)+20, 40+.5*(t-11)**2), 0, 0.73,  0.34, 0, 1.75,1.5)
I = Stock("I", lambda t: Complex(0.02*(t-11.7)**3+80, 2*t+35), 0, 0.62, -0.21, 0, 1,1.5)
J = Stock("J", lambda t: Complex(10*math.sqrt(0.8*(t-1))+90, 54/(.5*(t-6.6)**2+1)+83), 0, 0.61, -0.37, 0, .2,.5)
K = Stock("K", lambda t: Complex(40+2.4*t+.75*t*math.sin(t), .01*(t-12)**3+45), 0, 0.67, -0.62, 0, .75,.75)
L = Stock("L", lambda t: Complex(0.002*(t-13.7)**4-0.002*(t-13.7)**2+3.6*t+20, 16*math.sqrt(t)), 0, 0.58, -0.81, 0, 1,1.75)
M = Stock("M", lambda t: Complex(-0.005*(t-18.4)**3+0.005*(t-18.4)**2+3.6*t+64, 16.5*math.sqrt(t)+.5*(t-11)+39), 0, 0.90,  0.91, 0, 1,1)
N = Stock("N", lambda t: Complex(0.008*(t-11.1)**3-.15*(t-11.1)**2+.15*t+115, 2*t*math.sin(2*t)+t+80), 0, 0.77,  0.49, 0, .3,1.5)
O = Stock("O", lambda t: Complex(-24*math.sin(2*t)/t+2*t+100, .1*(t-10)**2+93), 0, 0.87,  0.46, 0, .2,.75)
P = Stock("P", lambda t: Complex(15/(2.75*math.sin(3*t/4)+3.5)+3.5*t+100, t+math.e**(t-21)+120), 0, 0.76,  0.12, 0, .75,.75)
Q = Stock("Q", lambda t: Complex(2*t+30+38*(t-6.9)/(1+(t-6.9)**2), 27+t/2-27.5*(t-4.5)/(1+(t-4.5)**2)), 0, 0.67, -0.29, 0, 1,1)
R = Stock("R", lambda t: Complex(2*math.sin(t)+10*math.sqrt(t)+35, 2*t+21-75*(t-11.5)/(1+(t-11)**2)), 0, 0.83,  0.74, 0, 1,.1)
S = Stock("S", lambda t: Complex(5+2*t+abs(-23+.5*(t-11)**2), 21+.1*(t-11)**2), 0, 0.62, -0.67, 0, .65,1)
T = Stock("T", lambda t: Complex(10*math.cbrt(7*t-100)+80, 20+2*t+35/(1+.5*(t-12)**2)), 0, 0.94,  0.85, 0, 2,.2)
U = Stock("U", lambda t: Complex(3*math.sqrt(8*math.sin(t)+20)+40+2.5*t, 37+1.5*t+35/(1+.5*(t-3)**2)), 0, 0.59, -0.78, 0, .5,.5)
V = Stock("V", lambda t: Complex(3*t*math.sin(1.2*t)+100, 67+1.5*t+35/(1+10*(t-1)**2)), 0, 0.94,  0.78, 0, 2.5,.5)
W = Stock("W", lambda t: Complex(95+20*math.sin(math.sqrt(20*t)), 71/t+1.5*t+50), 0, 0.65,  0.18, 0, 1.8,.25)
X = Stock("X", lambda t: Complex(7*math.sqrt(7*math.sin(t)+7)+t+70, 61+t+5*math.sin(math.sqrt(10*t))), 0, 0.88,  0.97, 0, 1.2,1.6)
Y = Stock("Y", lambda t: Complex(80/(1+.1*(t-7)**2)+25-t/3, 20+.8*math.e**(5-t/2)), 0, 0.57, -0.56, 0, 4,.4)
Z = Stock("Z", lambda t: Complex(10*math.sin(.07*(t-5)**2)+.15*(t-1)**2+50, math.e**(.2*t+math.sin(t/2))/2+45), 0, 0.93,  0.22, 0, .3,1.5)


AA = Stock("AA", lambda t: Complex(-2*math.sqrt(1.5*(t-10)*(t-15)*(t-20)*(t-25)+1000)+150, -0.4*(t-17.2)**2+40), 11, .61, -.37, 0, 1, 0.5)
BB = Stock("BB", lambda t: Complex(0.05*(t-6)**3-3.5*t+100, -3*t*math.sin(t)/((t-14)**2+1)+105), 11, .76, .12, 0, 1, .24)

stockExchange = {A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,BB}

def adv_year(company:Stock, Satis:float, Commun:float, Growth:float)-> None:
    """
    In terms of millions, how much will the ticker increase in this year if the following amounts are invested into them.
    """
    Satis = max(0, Satis)
    Commun = max(Commun, 0)
    growth = max(growth, 0)

    company.start_year += 1
    pVal = round(company.predictedValue(company.start_year), 2)
    pCost = round(company.predictedCost(company.start_year), 2)
    minVal = pVal*(1-company.r_factor/100)**company.start_year
    maxVal = pVal*(1+company.r_factor/100)**company.start_year
    minCost = pCost - company.start_year*company.m_factor
    maxCost = pCost + company.start_year*company.m_factor

    if company.start_year>10:
        #hard mode
        company.satisfaction, satisFlag = satis_Impact_Recession(company.satisfaction, Satis)
        company.cvr, commFlag = commun_Impact_Recession(company.cvr, Commun)
    else:
        company.satisfaction, satisFlag = satis_Impact(company.satisfaction, Satis)
        company.cvr, commFlag = commun_Impact(company.cvr, Commun)
    try:
        y = 1/(1+1/company.satisfaction) - 3/7
    except:
        y = 4/7
    skew_factor = 1.7*y+0.15
    try:
        x = math.atan(company.cvr)*1/(math.cos(company.cvr))**2
    except:
        x = 0
    if x<0:
        revenue_translate = 2-math.e**(-x)
    else:
        revenue_translate =math.e**(x**0.5)
    company.growth = growth_Impact(company.growth, Growth)
    fnDHO:Callable[[float, float], float] = lambda x,max : -1.2* math.e**(-4*x/max/5)*math.cos(1.7*x/max + 1)+1
    if company.start_year>10:
        foci = lambda x: 1/(4*math.pi*math.e*(0.09*(x-8)))
        foe = foci(company.start_year)
        z = company.start_year - 8
        fnDHO = lambda x, p: .25 +0.5*math.e**(-math.e*p*x)*math.cos(p*x)+ 2.4581*math.e**(-x*p)*(math.sin(2*x*p))**2
        multiply_revenue = fnDHO(company.growth, foe)
    else:
        z = r.randint(1,6*company.start_year)
        multiply_revenue = fnDHO(company.growth, Growth)
    cRv = r.uniform(0,1)
    if cRv + skew_factor >= 0.5:trueCost = r.uniform(minCost, pCost)
    else:trueCost = r.uniform(pCost, maxCost)
    
    if company.start_year>10:trueCost *= 1.2
    trueCost = round(trueCost, 2)
    trueValue = r.uniform(minVal, maxVal)*multiply_revenue+revenue_translate
    trueValue = round(trueValue, 2)

    print("The revenue generated this year was $"+str(trueValue)+'M, but the cost incurred was $'+str(trueCost)+'M.')
    print("The predicted revenue this year was $"+str(pVal)+'M; the predicted cost was $'+str(pCost)+'M.')
    company.satisfaction *= 0.9
    company.satisfaction = round(company.satisfaction, 2)

    pulseEvent = r.uniform(0,1)
    if pulseEvent >0.98:
        company.cvr = 0.9
        print("Excellent marketing year. Beneficial results.")
    elif pulseEvent < 0.02:
        company.cvr = -.9
        print("Horrible marketing year. Putrid results.")
    elif pulseEvent >0.9:
        company.cvr = .5
        print("Good marketing year. Passable results.") #Change to a better message after w5.
    elif pulseEvent <0.1:
        company.cvr = -.5
        print("Bad marketing year. Improvable results.")
    else:
        company.cvr *=4/5
        company.cvr = round(company.cvr, 2)
        print("Typical marketing year. Average results.")
    
    if satisFlag: print("{Mark:} Over-invested into facilities. Employees slacked off.")
    if commFlag: print("{Mark:} Over-invested into marketing. Advertisements skipped.")

    if company.start_year%2==0:
        company.growth *=2/3
        if company.start_year>10:
            company.growth *=3/4
        company.growth = round(company.growth, 2)
        print("Your investments have decayed in value.")
    elif z< company.growth:
        if company.growth - z > z and company.start_year<= 10:
            if z == 1:
                company.growth = 0
            else:
                company.growth = 1
            print("Rival firms noticed how much you spent and successfully stole good expansion targets. A lot of money has been wasted.")
        elif company.start_year>10:
            if multiply_revenue < 0.75:
                company.growth = round(company.growth*3/4, 2)
                print("Rival firms noticed how much you spent and successfully stole good expansion targets. A lot of money has been wasted.")
            else:
                company.growth = round(company.growth*7/8, 2)
                print("A rival firm noticed how much you spent and successfully stole some expansion targets. A portion of money has been wasted.")
        else:
            company.growth = round(z-(company.growth-z), 2)
            print("A rival firm noticed how much you spent and successfully stole some expansion targets. A portion of money has been wasted.")
    if multiply_revenue >= 1.4:
        print("Your firm was able to scale its operations exceedingly better than its peers. Growth is high.")
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
        else: 
            investAmount = 0
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
        else: 
            investAmount = 0
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
    
    if score >= 1: 
        score = 1
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
    
    if score >= 1: 
        score = 1
    return (score, flag)

def reset()-> None:
    A = Stock("A", lambda t: Complex(0.1*(t-7.6)**3-1.2*(t-7.6)**2+140, 0.4*(t-5.9)**2+80.6), 0, 0.85, -0.85, 0, 1.75,2)
    B = Stock("B", lambda t: Complex(17*math.sqrt(2*t-2)+20, 0.8*t+4.8**(0.1*t)+51), 0, 0.68, -0.25, 0, 1.75,1)
    C = Stock("C", lambda t: Complex(30*(t-5)/(0.1*(t-5)**2+1)+80, 15*math.sqrt(t)+24), 0, 0.75,  0.15, 0, 1.5,1)
    D = Stock("D", lambda t: Complex(.03*(t-12)**3+50, 0.75*t+22), 0, 0.78,  0.45, 0, .5,.5)
    E = Stock("E", lambda t: Complex(80-2.2*math.e**(4-t), 12*math.sqrt(t)+15), 0, 0.92,  0.68, 0, .5,.5)
    F = Stock("F", lambda t: Complex(105-.2*(t-16)**2, 10+.15*(t+6)**2), 0, 0.84,  0.25, 0, 1.8,1)
    G = Stock("G", lambda t: Complex(35+4*t+16*math.sin(.5*t), 76-0.1*(t-5)**2), 0, 0.89, -0.08, 0, 1.25,.75)
    H = Stock("H", lambda t: Complex(4*t+.1*math.e**(t/2-5)+20, 40+.5*(t-11)**2), 0, 0.73,  0.34, 0, 1.75,1.5)
    I = Stock("I", lambda t: Complex(0.02*(t-11.7)**3+80, 2*t+35), 0, 0.62, -0.21, 0, 1,1.5)
    J = Stock("J", lambda t: Complex(10*math.sqrt(0.8*(t-1))+90, 54/(.5*(t-6.6)**2+1)+83), 0, 0.61, -0.37, 0, .2,.5)
    K = Stock("K", lambda t: Complex(40+2.4*t+.75*t*math.sin(t), .01*(t-12)**3+45), 0, 0.67, -0.62, 0, .75,.75)
    L = Stock("L", lambda t: Complex(0.002*(t-13.7)**4-0.002*(t-13.7)**2+3.6*t+20, 16*math.sqrt(t)), 0, 0.58, -0.81, 0, 1,1.75)
    M = Stock("M", lambda t: Complex(-0.005*(t-18.4)**3+0.005*(t-18.4)**2+3.6*t+64, 16.5*math.sqrt(t)+.5*(t-11)+39), 0, 0.90,  0.91, 0, 1,1)
    N = Stock("N", lambda t: Complex(0.008*(t-11.1)**3-.15*(t-11.1)**2+.15*t+115, 2*t*math.sin(2*t)+t+80), 0, 0.77,  0.49, 0, .3,1.5)
    O = Stock("O", lambda t: Complex(-24*math.sin(2*t)/t+2*t+100, .1*(t-10)**2+93), 0, 0.87,  0.46, 0, .2,.75)
    P = Stock("P", lambda t: Complex(15/(2.75*math.sin(3*t/4)+3.5)+3.5*t+100, t+math.e**(t-21)+120), 0, 0.76,  0.12, 0, .75,.75)
    Q = Stock("Q", lambda t: Complex(2*t+30+38*(t-6.9)/(1+(t-6.9)**2), 27+t/2-27.5*(t-4.5)/(1+(t-4.5)**2)), 0, 0.67, -0.29, 0, 1,1)
    R = Stock("R", lambda t: Complex(2*math.sin(t)+10*math.sqrt(t)+35, 2*t+21-75*(t-11.5)/(1+(t-11)**2)), 0, 0.83,  0.74, 0, 1,.1)
    S = Stock("S", lambda t: Complex(5+2*t+abs(-23+.5*(t-11)**2), 21+.1*(t-11)**2), 0, 0.62, -0.67, 0, .65,1)
    T = Stock("T", lambda t: Complex(10*math.cbrt(7*t-100)+80, 20+2*t+35/(1+.5*(t-12)**2)), 0, 0.94,  0.85, 0, 2,.2)
    U = Stock("U", lambda t: Complex(3*math.sqrt(8*math.sin(t)+20)+40+2.5*t, 37+1.5*t+35/(1+.5*(t-3)**2)), 0, 0.59, -0.78, 0, .5,.5)
    V = Stock("V", lambda t: Complex(3*t*math.sin(1.2*t)+100, 67+1.5*t+35/(1+10*(t-1)**2)), 0, 0.94,  0.78, 0, 2.5,.5)
    W = Stock("W", lambda t: Complex(95+20*math.sin(math.sqrt(20*t)), 71/t+1.5*t+50), 0, 0.65,  0.18, 0, 1.8,.25)
    X = Stock("X", lambda t: Complex(7*math.sqrt(7*math.sin(t)+7)+t+70, 61+t+5*math.sin(math.sqrt(10*t))), 0, 0.88,  0.97, 0, 1.2,1.6)
    Y = Stock("Y", lambda t: Complex(80/(1+.1*(t-7)**2)+25-t/3, 20+.8*math.e**(5-t/2)), 0, 0.57, -0.56, 0, 4,.4)
    Z = Stock("Z", lambda t: Complex(10*math.sin(.07*(t-5)**2)+.15*(t-1)**2+50, math.e**(.2*t+math.sin(t/2))/2+45), 0, 0.93,  0.22, 0, .3,1.5)
    AA = Stock("AA", lambda t: Complex(-2*math.sqrt(1.5*(t-10)*(t-15)*(t-20)*(t-25)+1000)+150, -0.4*(t-17.2)**2+40), 10, .61, -.37, 0, 1, 0.5)
    BB = Stock("BB", lambda t: Complex(0.05*(t-6)**3-3.5*t+100, -3*t*math.sin(t)/((t-14)**2+1)+105), 10, .76, .12, 0, 1, .24)
    saveAsFile()
def force_advance(destination:int)-> None:
    loadFile()
    for stock in stockExchange:
        if destination >= stock.start_year: stock.start_year = destination
        else: raise ValueError("Wantin to return to a year that company "+company.name+" has already completed.")
