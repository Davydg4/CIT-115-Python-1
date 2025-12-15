#List and Real Estate Analyzer

#Import
import RealEstateModule

#Input

def main():
    fSalesList = []

    sValue = ""
    while sValue != "N" and sValue != "n":
        fSalesPrice = RealEstateModule.getFloatInput("Enter property sales value: ")
        fSalesList.append(fSalesPrice)

        sValue = input("Enter another value Y or N: ")
        while True:
            
            if sValue == "Y" or sValue == "y":
                break
            elif sValue == "N" or sValue == "n":
                break
            else:
                sValue = input("Enter another value Y or N: ")
    
    fSalesList.sort()   
    
    iProperty = 1
    iElement = 0
    while iElement < len(fSalesList):
        print("Property", iProperty, "$ \t",format(fSalesList[iElement], ',.2f'))
        iProperty += 1
        iElement += 1
    #Lowest Value
    fMin = min(fSalesList)
    print("Minimum: \t $ \t",format(fMin,',.2f'))

    #Largest Value
    fMax = max(fSalesList)
    print("Maximum: \t $ \t",format(fMax,',.2f'))

    #Sum of all numbers in the list
    fTotal = sum(fSalesList)
    print("Total:  \t $ \t",format(fTotal,',.2f'))

    #Average of all the numbers in the list
    fAvg = fTotal / len(fSalesList)
    print("Average: \t $ \t",format(fAvg,',.2f'))

    #Median
    fMedian = RealEstateModule.getMedian(fSalesList)
    print("Median: \t $ \t",format(fMedian,',.2f'))

    #Commission
    fCommission = fTotal * .03
    print("Commission: \t $ \t",format(fCommission,',.2f'))
    

main()

 
