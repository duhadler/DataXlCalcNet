from fractions import Fraction
from decimal import Decimal
import datetime as dt    



def getAsDoubleFormula(MpString):
    result = float(Fraction(MpString) if  '/' in MpString else Decimal(MpString))
    return result


def getAsDoubleFormulaStr(MpString):    
    Formula = "result = float(Fraction('" + MpString +"') if  '/' in '" + MpString + "' else Decimal('" + MpString + "'))"
    return Formula


res = getAsDoubleFormula("2/3"); print(res)
res = getAsDoubleFormula("2.3346293462938462934629356E40"); print(res)


print(getAsDoubleFormulaStr("2/3"))
print(getAsDoubleFormulaStr("2.3346293462938462934629356E40"))
