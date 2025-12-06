#Paint Job with Functions and Output Files
import PaintJobModule



def main():

    fSqFeetWall = PaintJobModule.getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = PaintJobModule.getFloatInput("Enter paint price per gallon: ")
    fFeetGallon = PaintJobModule.getFloatInput("Enter feet per gallon: ")
    fLaborGallonsHour = PaintJobModule.getFloatInput("How many labor hours per gallon: ")
    fPaintLaborHour = PaintJobModule.getFloatInput("Labor charge per hour: ")

    sStateJob = input("State job is in: ")
    sLastName = input("Customer last name: ")

    iGallonsOfPaint = PaintJobModule.getGallonsOfPaint(fSqFeetWall, fFeetGallon)    
    print("Gallons of paint:",(iGallonsOfPaint))

    fLaborHours = PaintJobModule.getLaborHours(fLaborGallonsHour, iGallonsOfPaint)
    print("Hours of labor: ",format(fLaborHours,'.1f'))

    fPaintCharges = PaintJobModule.getPaintCost(fPaintPrice, iGallonsOfPaint)
    print("Paint charges: $",format(fPaintCharges,'.2f'))

    fLaborCharges = PaintJobModule.getLaborCost(fLaborHours, fPaintLaborHour)
    print("Labor charges: $",format(fLaborCharges,'.2f'))

    fSalesTax = PaintJobModule.getSalesTax(fLaborCharges, fPaintCharges, sStateJob)
    print("Tax: $", format(fSalesTax,'.2f'))

    fTotal = PaintJobModule.showCostEstimate(fPaintCharges, fLaborCharges, fSalesTax)
    print("Total Cost: $", format(fTotal,'.2f'))

    print("File: ",sLastName,"_PaintJobOutput.txt was created.")

    OutputFile = open("_PaintJobOutput.txt", 'w')

    OutputFile.write("Gallons of paint:" + str(iGallonsOfPaint) + '\n') 
    OutputFile.write("Hours of labor: " + str(fLaborHours) + '\n')
    OutputFile.write("Paint charges: $" + str(fPaintCharges) + '\n')
    OutputFile.write("Labor charges: $" + str(fLaborCharges) + '\n')
    OutputFile.write("Tax: $" + str(fSalesTax) + '\n')
    OutputFile.write("Total Cost: $" + (str(fTotal) + '\n'))
    
    OutputFile.close()

main()





    


