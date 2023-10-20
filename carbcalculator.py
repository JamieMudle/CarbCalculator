import mysql.connector

# Define the CarbCalculator function
def CarbCalculator():
    try:
        # Establish a connection to the MySQL database
        db_connection = mysql.connector.connect(
            host='localhost',
            user='Jamie',
            password='Kn1ghtK1ller45!',
            database='carbscollector'
        )

        # Create a cursor to execute SQL queries
        cursor = db_connection.cursor()

        # Get user input for carb calculations
        product = input("Enter product: ")
        x = input("Enter Listed Carbs: ")
        y = input("Enter Product Weight: ")
        z = input("Enter Portion Size: ")

        # Setting vars for carb calculation
        productvalue = str(product)
        xx = float(x)
        yy = float(y)
        zz = float(z)

        # Carb Calculator
        result = round(xx / yy * zz, 1)
        print(f"Calculated result: {result}")

        # MySQL functionality

        insert_query = "INSERT INTO carbsandportions (product, carbohydrates, weight, portionsize, result) " \
                        "VALUES (%s, %s, %s, %s, %s)"
        data_to_insert = (productvalue, xx, yy, zz, result)
        cursor.execute(insert_query, data_to_insert)
        db_connection.commit()
        
        print("Data inserted successfully")

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    except ValueError:
        print("Error: Please enter numerical values for carbohydrates, product weight, and portion size.")
    finally:
        if 'db_connection' in locals() or 'db_connection' in globals():
            cursor.close()
            db_connection.close()

# Call the CarbCalculator function
CarbCalculator()
