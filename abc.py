def divide_numbers():
    try:
        # Get input from the user
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Attempt to perform the division
        result = numerator / denominator

        # Display the result
        print(f"The result of {numerator} / {denominator} is: {result}")

    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Division by zero is not allowed.")

    except ValueError:
        # Handle invalid input (e.g., non-numeric input)
        print("Error: Please enter valid numeric values.")

    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
    finally :
        print("hi gyt hjvn")
        x=7875+678
        print(f"fghddfgh : {x}")

# Call the function to execute the program
divide_numbers()
