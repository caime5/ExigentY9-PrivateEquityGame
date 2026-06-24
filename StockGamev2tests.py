from scipy.integrate import quad
import StockGamev2 as S

def functionTestsWork()->bool:
    value = True
    for key in S.stockList:
        try:
            for t in range(1,26):
                cpxVal = S.stockList[key][0](t)
        except  ZeroDivisionError:
            print(str(t)+"gave a divide by 0 error for Ticker"+key)
        except Exception as e:
            print("Something else went wrong for Ticker"+key)
            print(f"Something else went wrong for Ticker {key} at t={t}: {type(e).__name__} - {e}")
            value = False
    return value

def testProjectedProfitAZ()-> bool:
    """
    See if all functions so far have been inputted as expected.
    Current range is tickers A-Z.
    """
    flag = True
    projections = [503,577,518,542,524,534,529,506,547,654,575,484,457,468,656,416,630,451,603,560,579,294,424,598,500,532]
    index = 0
    for key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        fn = S.stockList[key][0]
        result = quad(lambda t:fn(t).Re(), 1, 25)[0]-quad(lambda t:fn(t).Im(),1,25)[0]
        if round(result,0) == projections[index]:
            index += 1
            if index == len(projections):break
        else:
            print("Ticker "+key+" has an error in its formulas. Check again.")
            flag = False
            break
    if flag:print("All tickers from A-Z work as intended for their projected profit integrals.")
    return flag