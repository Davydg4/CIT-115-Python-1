def getFloatInput(sPrompt):

    fValue = 0

    while fValue <= 0:
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                print("Must be a positive numeric value")
        except ValueError:
            print("Must be a positive numeric value")

    return fValue
            
def getGallonsOfPaint(fSqFeetWall, fFeetGallon):
    return round(fSqFeetWall / fFeetGallon)
    

def getLaborHours(fLaborGallonsHour, iGallonsOfPaint):
    return iGallonsOfPaint * fLaborGallonsHour
   
def getPaintCost(fPaintPrice, iGallonsOfPaint):
    return fPaintPrice * iGallonsOfPaint

def getLaborCost(fLaborHours, fPaintLaborHour):
    return fLaborHours * fPaintLaborHour


def getSalesTax(fLaborCharges, fPaintCharges, sStateJob):

    fSalesTax = fLaborCharges + fPaintCharges

    if sStateJob == "CT":
        fSalesTax *= .06
    elif sStateJob == "MA":
        fSalesTax *= .0625
    elif sStateJob == "ME":
        fSalesTax *= .085
    elif sStateJob == "NH":
        fSalesTax *= .0
    elif sStateJob == "RI":
        fSalesTax *= .07
    elif sStateJob == "VT":
        fSalesTax *= .06
    else:
        fSalesTax = 0
    return fSalesTax

def showCostEstimate(fPaintCharges, fLaborCharges, fSalesTax):
    return fPaintCharges + fLaborCharges + fSalesTax

   
    
