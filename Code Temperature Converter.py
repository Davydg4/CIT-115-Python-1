#Code Temperature Converter

#Input
print("Davyd's Temp Converter")

fTemperature = float(input("Enter a temperature: "))
sTemp = input("Is the temp F for Fahrenheit or C for Celsius?")



#Calculations

if sTemp == "F" and fTemperature > 212:
    print("Temp can not be > 212")
elif sTemp == "F":
   fCelsius = (5.0/9)*(fTemperature - 32)
   print("The Celsius equivalent is:", format(fCelsius,'.1f'))
elif sTemp == "C" and fTemperature > 100:
    print("Temp can not be > 100")
elif sTemp == "C":
    fFahrenheit = ((9.0/5.0)* fTemperature) + 32
    print("The Fahrenheit equivalent is:", format(fFahrenheit,'.1f'))
else:
    print("Enter a F or C")
    raise SystemExit


    






    
    
    
    


    


