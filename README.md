# AI-Calculator

A simple AI-based calculator that understands natural language inputs and performs basic arithmetic operations like addition, subtraction, multiplication, and division. The project is built using Python and utilizes Natural Language Processing (NLP) to interpret user input.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Examples](#examples)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The AI-Based Calculator can interpret arithmetic expressions given in natural language, such as:
- "What is the sum of 15 and 20?"
- "Multiply 12 by 3."
- "Subtract 5 from 10."

This makes it user-friendly and easy to interact with, especially for those who prefer to type commands in plain English.

## Features
- Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
- Understands natural language input.
- Easy-to-use command-line interface.
- Error handling for invalid inputs and division by zero.

## Technologies Used
- **Python**: The primary programming language used.
- **Natural Language Toolkit (NLTK)**: For text processing.
- **Regular Expressions (re)**: For extracting numbers from text.

## Installation

1. **Clone the Repository** 
   ```bash
   git clone https://github.com/AdityapalW/AI-Calculator.git
   cd ai-based-calculator

2. **Install Required Libraries**:
   Make sure you have Python installed on your system, then install the required dependencies:
   ```bash
   pip install nltk
   ```

3. **Download NLTK Data**:
   The first time you run the project, you will need to download some NLTK data:
   ```python
   import nltk
   nltk.download('punkt')
   ```

## How to Use

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the script using the following command:
   ```bash
   python ai_calculator.py
   ```

4. Follow the on-screen instructions to enter your arithmetic questions in natural language.

5. To exit the program, simply type `quit`.

## Examples
Here are some example commands you can try with the AI-Based Calculator:

- **Addition**: 
  - Input: `What is the sum of 15 and 20?`
  - Output: `The result is: 35.0`

- **Subtraction**:
  - Input: `Subtract 7 from 10`
  - Output: `The result is: 3.0`

- **Multiplication**:
  - Input: `Multiply 4 by 6`
  - Output: `The result is: 24.0`

- **Division**:
  - Input: `Divide 20 by 4`
  - Output: `The result is: 5.0`

## Future Improvements
- **Voice Input:** Add support for voice commands using speech recognition.
- **Extended Operations:** Include more complex operations like square roots, powers, and percentages.
- **GUI Interface:** Create a graphical user interface to enhance user interaction.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository, create a branch, and submit a pull request. Please make sure your code follows best practices and is well-documented.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you like.

