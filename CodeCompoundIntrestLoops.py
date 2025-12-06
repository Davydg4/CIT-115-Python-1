#Code Compound Intrest with Loops

#Inputs
fDeposit = 0
while fDeposit <= 0:

 try:
    fDeposit = float(input("What is the Original Deposit (positive value): "))
    fDeposit <= 0 == print("Input must be a positive numeric value")
    
 except ValueError:
    print("Input must be a positive numeric value")

fInterestRate = 0
while fInterestRate <= 0:

 try:
     fInterestRate = float(input("What is the Intrest Rate (positive value): "))
     fInterestRate <= 0 == print("Input must be a positive numeric value")

 except ValueError:
    print("Input must be a positive numeric value")

iMonths = 0
while iMonths <= 0:

 try:
     iMonths = int(input("What is the Number of Months (positive value): "))
     iMonths <= 0 == print("Input must be a positive numeric value")

 except ValueError:
    print("Input must be a positive numeric value")

fGoal = float(input("What is the Goal Amount (can enter 0 but not negative): "))
if fGoal < 0:
    print("Input can not be negative number")
    fGoal = float(input("What is the Goal Amount (can enter 0 but not negative): "))
    if fGoal < 0:
        print("Input can not be negative number")
        raise SystemExit
        
#Convert Interest Rate Percentage to decimal value
fInterestRate /= 100

fMonthly_Interest_Rate = fInterestRate / 12

#Loop statements
fMonthly_Interest_Rate *= fDeposit

fAccountBalance = 0.0
for iMonths in range(1, iMonths + 1):
    fAccountBalance += fMonthly_Interest_Rate    
    print("Month:", iMonths, "Account Balance is: $",format(fAccountBalance + fDeposit,',.2f'))
    


fAccountBalance += fDeposit

while fGoal > fAccountBalance:
    fAccountBalance += fMonthly_Interest_Rate
    iMonths += 1
    if fGoal <= fAccountBalance:
        print("It will take:",iMonths,"months to reach the goal of $ ",format(fGoal,'.2f'))


    
    





   



    
    

        
    

        






    



 
