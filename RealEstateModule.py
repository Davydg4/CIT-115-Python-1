#Inputs

def getFloatInput(sPrompt):

    fValue = 0

    while fValue <= 0:
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                print("Input a number that is greater than 0.")
        except ValueError:
            print("Input a number that is greater than 0.")

    return fValue

def getMedian(fSalesList):

    fMedian = ""

    iLength = len(fSalesList)

    if iLength % 2 != 0:
        iNumber = (iLength + 1) // 2
        fMedian = fSalesList[iNumber -1]
    else:
        middle_number = iLength // 2
        fMedian = (fSalesList[middle_number - 1] + fSalesList[middle_number]) / 2

    return fMedian
    
        



