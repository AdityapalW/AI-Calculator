import nltk
import re

# Download NLTK data (only required for the first time)
nltk.download('punkt')

# Function to identify the arithmetic operation from user input
def identify_operation(text):
    if 'add' in text or 'sum' in text or 'plus' in text:
        return 'addition'
    elif 'subtract' in text or 'minus' in text or 'difference' in text:
        return 'subtraction'
    elif 'multiply' in text or 'times' in text or 'product' in text:
        return 'multiplication'
    elif 'divide' in text or 'division' in text or 'over' in text:
        return 'division'
    else:
        return None

# Function to extract numbers from user input
def extract_numbers(text):
    return list(map(float, re.findall(r'\d+\.?\d*', text)))

# Function to perform the calculation
def perform_calculation(operation, numbers):
    if operation == 'addition':
        return sum(numbers)
    elif operation == 'subtraction':
        return numbers[0] - numbers[1]
    elif operation == 'multiplication':
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operation == 'division':
        try:
            return numbers[0] / numbers[1]
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Unknown operation."

# Main function to interact with the user
def ai_calculator():
    print("Welcome to the AI-Based Calculator!")
    print("You can ask me to perform operations like addition, subtraction, multiplication, or division.")
    print("For example, you can say 'What is the sum of 5 and 3?' or 'Divide 10 by 2'.")

    while True:
        user_input = input("\nEnter your calculation (or type 'quit' to exit): ").lower()
        if user_input == 'quit':
            print("Thank you for using the AI-Based Calculator. Goodbye!")
            break

        # Identify the operation and extract numbers from user input
        operation = identify_operation(user_input)
        numbers = extract_numbers(user_input)

        if operation and len(numbers) >= 2:
            result = perform_calculation(operation, numbers)
            print(f"The result is: {result}")
        else:
            print("Sorry, I couldn't understand your request. Please try again.")

# Run the AI-based calculator
if __name__ == '__main__':
    ai_calculator()
