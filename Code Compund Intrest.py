#Code Compound Intrest

#Input
fPrincipalInvestment = float(input("Enter the starting principal: "))
fIntrestRate = float(input("Enter the annual intrest rate: "))
iCompounding = int(input("How many times per year is the intrest compounded? "))
iYears = int(input("For how many years will the account earn intrest? "))

#Calculations
fIntrest_Rate = fIntrestRate/100

fFutureValue = fPrincipalInvestment * (1+fIntrest_Rate/iCompounding)**(iYears * iCompounding)

#Output
print("At the end of 2 years you will have $",format(fFutureValue, '.2f'))


