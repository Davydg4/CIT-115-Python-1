#Inter Planetary Weights Assignment

#Surface Gravity Factor
fMERCURY = 0.38
fVENUS = 0.91
fMOON = 0.165
fMARS = 0.38
fJUPITER = 2.34
fSATURN = 0.93
fURANUS = 0.92
fNEPTUNE = 1.12
fPLUTO = 0.066

#Input
sName = str(input("What is your name: "))
iEARTH_WEIGHT = int(input("What is your weight: "))

print(sName, "here are your weights on our Solar System's planets:")

#Calculations

fMercuryWeight = iEARTH_WEIGHT * fMERCURY 
fVenusWeight = iEARTH_WEIGHT * fVENUS
fMoonWeight = iEARTH_WEIGHT * fMOON
fMarsWeight = iEARTH_WEIGHT * fMARS
fJupiterWeight = iEARTH_WEIGHT * fJUPITER
fSaturnWeight = iEARTH_WEIGHT * fSATURN
fUranusWeight = iEARTH_WEIGHT * fURANUS
fNeptuneWeight = iEARTH_WEIGHT * fNEPTUNE
fPlutoWeight = iEARTH_WEIGHT * fPLUTO

#Formatting
print("Weight on Mercury:           " + format(fMercuryWeight, '.2f'))
print("Weight on Venus:            " + format(fVenusWeight, '.2f'))
print("Weight on our Moon:          " + format(fMoonWeight, '.2f'))
print("Weight on Mars:              " + format(fMarsWeight, '.2f'))
print("Weight on Jupiter:          " + format(fJupiterWeight, '.2f'))
print("Weight on Saturn:           " + format(fSaturnWeight, '.2f'))
print("Weight on Uranus:           " + format(fUranusWeight, '.2f'))
print("Weight on Neptune:          " + format(fNeptuneWeight, '.2f'))
print("Weight on Pluto:              " + format(fPlutoWeight, '.2f'))







