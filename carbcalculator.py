#def CarbCalculator function

def CarbCalculator():
    
    #Setting vars for carb input
    try:
        x = input("Enter Listed Carbs:")
        y = input("Enter Product Weight:")
        z = input("Enter Portion Size:")
        
        #Setting vars for carb calculation

        xx = float(x)
        yy = float(y)
        zz = float(z)
        
        #Carb Calculator

        result = round(xx / yy * zz, 1)
        print(result)
    #Error Handling
    except:
        print("Error:Please enter a numerical value")
CarbCalculator()