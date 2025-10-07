from db_setup import reset_database

def main():
    reset_database()
    
    print("Welcome to the Statistics Program!")
    print("What would you like to do today? (select 'q' at any point to quit)")
    while True:
        print("1: Measures of Central Tendency (MCT)")
        print("2: Method of Least Squares (MLS)")

        try:
            mode = int(get_input("Select mode (1 or 2): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue # Go back to top of while loop

        if mode == 1:
            while True:
                print("MCT Options:")
                for key, (label, _) in mct_operations.items():
                    print(f"{key}: {label}")
                try:
                    mct_choice = int(get_input("Select MCT option: "))
                    func = mct_operations[mct_choice][1]
                    result = func()
                    print(f"Result: {result}")
                    break
                except (KeyError, ValueError):
                    print("Invalid MCT option selected.")
                    continue

        elif mode == 2:
            while True:
                print("MLS Options:")
                for key, (label, _) in mls_operations.items():
                    print(f"{key}: {label}")
                try:
                    mls_choice = int(get_input("Select MLS option: "))
                    func = mls_operations[mls_choice][1]
                    result = func()
                    print(f"Result: {result}")
                    break
                except (KeyError, ValueError):
                    print("Invalid MLS option selected.")
                    continue
        else:
            print("Invalid mode selected.")
            continue
        
        break


##### MEASURES OF CENTRAL TENDENCY functions
def mct_mean():
    total_sum = 0
    
    numbers = get_number_array()

    for num in numbers:
        total_sum += int(num)
   
    average = total_sum/len(numbers)

    # If number is a whole number, do not include .0 at the end
    if average.is_integer():
        average = int(average)    
    
    return f"The mean of your data set is: {average}"

def mct_median():
    numbers = get_number_array()
    numbers.sort()

    n = len(numbers)
    mid_index = n // 2

    if n % 2 == 1: # Odd length
        median = numbers[mid_index]
    else: # Even length
        median = (numbers[mid_index - 1] + numbers[mid_index]) / 2

    # If number is a whole number, do not include .0 at the end
    if median.is_integer():
        median = int(median)

    return f"The median of your data set is: {median}"

def mct_mode():
    pass


##### METHODS OF LEAST SQUARES functions
def mls_linear():
    """1. Get data. 2. Find sums. 3. Put sums in formula. 4. Put values back into equation."""
    
    print("--- Linear Regression (y = mx + b) ---")
    print("Please enter your x values: ")
    x_values = get_number_array()
    
    print("Please enter your y values (in the same order): ")
    y_values = get_number_array()

    roundingfigs = input("Please enter")

    return
    #return f("Your x value is: {x_value} and your y value is: {y-value}")

def mls_nonlinear():
    pass


##### OTHER functions
def get_number_array():
    while True:
        # Get data set from user
        user_input = get_input("Please enter data, separated only by a comma (no spaces): ")

        # Check for spaces - disallow
        if ' ' in user_input:
            print("Error: Please do NOT include spaces. Try again.")
            continue

        # Split data set array by commas into parts
        parts = user_input.split(",")

        # Validate each part is a number
        try:
            numbers = [float(part) for part in parts]
        except ValueError:
            print("Error. Please only enter numbers separated by commas. Try again.")
            continue

        if not numbers:
            print("Error. No numbers entered. Try again.")
            continue
            
        return numbers

def get_input(prompt):
    user_input = input(prompt).strip()
    if user_input.lower() in ["q", "quit", "exit"]:
        print("Quitting the program. Goodbye!")
        exit()
    return user_input

##### DICTIONARY DEFINITIONS
mct_operations = {
    1: ("Mean", mct_mean),
    2: ("Median", mct_median),
    3: ("Mode", mct_mode)
}

mls_operations = {
    1: ("Linear Regression", mls_linear),
    2: ("Non-linear Regression", mls_nonlinear)
}

# Python idiom, allows export
if __name__ == "__main__":
    main()
