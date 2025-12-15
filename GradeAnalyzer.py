#Grade Analyzer

#Inputs
sName = input("Name of person that we are calculating the grades for: ")
fT1 = float(input("Test 1: "))
fT2 = float(input("Test 2: "))
fT3 = float(input("Test 3: "))
fT4 = float(input("Test 4: "))
sDrop = input("Do you wish to Drop the Lowest Grade Y or N? ")

#Scores must be > 0
if fT1 < 0 or fT2 < 0 or fT3 < 0 or fT4 < 0:
    print("Test scores must be greater than 0")
    raise SystemExit

# sDrop must be a Y or N
if sDrop != "Y" and sDrop != "N":
    print("Enter Y or N to Drop the Lowest Grade")
    raise SystemExit

# Determine which test is the Lowest
if (fT1 < fT2) and (fT1 < fT3) and (fT1 < fT4):
    sLowestGrade = fT1
elif (fT2 < fT1) and (fT2 < fT3) and (fT2 < fT4):
    sLowestGrade = fT2
elif (fT3 < fT1) and (fT3 < fT2) and (fT3 < fT4):
    sLowestGrade = fT3
else:
    sLowestGrade = fT4

#If user wants to Drop Lowest Grade 
if sDrop == "Y" and sLowestGrade == fT1:
    fAverage = (fT2 + fT3 + fT4) /3
elif sDrop == "Y" and sLowestGrade == fT2:
    fAverage = (fT1 + fT3 + fT4) /3
elif sDrop == "Y" and sLowestGrade == fT3:
    fAverage = (fT1 + fT2 + fT4) /3
else:
    fAverage = (fT1 + fT2 + fT3) /3

#If user doesn't want to Drop Lowest Grade
if sDrop == "N":
    fAverage = (fT1 + fT2 + fT3 + fT4) /4

print(sName,"test average is: ",format(fAverage,'.1f'))


#Test average's letter grade value
if fAverage >= 97.0:
    print("Letter Grade for the test is: A+")
elif fAverage >= 94.0:
    print("Letter Grade for the test is: A")
elif fAverage >= 90.0:
    print("Letter Grade for the test is: A-")
elif fAverage >= 87.0:
    print("Letter Grade for the test is: B+")
elif fAverage >= 84.0:
    print("Letter Grade for the test is: B")
elif fAverage >= 80.0:
    print("Letter Grade for the test is: B-")
elif fAverage >= 77.0:
    print("Letter Grade for the test is: C+")
elif fAverage >= 74.0:
    print("Letter Grade for the test is: C")
elif fAverage >= 70.0:
    print("Letter Grade for the test is: C-")
elif fAverage >= 67.0:
    print("Letter Grade for the test is: D+")
elif fAverage >= 64.0:
    print("Letter Grade for the test is: D")
elif fAverage >= 60.0:
    print("Letter Grade for the test is: D-")
else:
    print("Letter Grade for the test is: F")
    












