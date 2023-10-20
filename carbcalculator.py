import csv

#def CarbCalculator function

def CarbCalculator():
    
    #Setting vars for carb input
    try:
        product = input("Enter product:")
        x = input("Enter Listed Carbs:")
        y = input("Enter Product Weight:")
        z = input("Enter Portion Size:")
        
        #Setting vars for carb calculation
        productvalue = str(product)
        xx = float(x)
        yy = float(y)
        zz = float(z)
        
        #Carb Calculator
        
        result = round(xx / yy * zz, 1)
        header = ["Product, Portion Size, Carbohydates, Carbs Per Portion"]
        data = f"{productvalue}, {xx}, {zz}, {result}"
        print(result)

        with open('carbs_and_portions.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            
            writer.writerow([header])
            writer.writerow([data])
            
            return(True)
        
    #Error Handling
    except Exception:
        print("Error:Please enter a numerical value")
        
CarbCalculator()
