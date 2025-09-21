# Factor Generator App

A Python application that finds all factors of a given number and displays how different factor pairs multiply together to produce the original number.

## Description

This program takes a user-input number and calculates all of its factors. It then shows how each factor pairs with another to equal the original number, providing both individual factors and mathematical summaries.

## Features

- ✅ Interactive user interface with welcome message
- ✅ Finds all factors of any positive integer
- ✅ Displays factors in ascending order
- ✅ Shows factor pair multiplication summaries
- ✅ Continuous operation with user choice to continue or exit
- ✅ Clean, readable output formatting

## Example Usage

Welcome to the Factor Generator App
Enter a number to determine all factors of that number: 44
Factors of 44 are:
1
2
4
11
22
44
In summary:
1 * 44 = 44
2 * 22 = 44
4 * 11 = 44
Run again (y/n): n


## How It Works

1. **Input**: User enters a positive integer
2. **Factor Finding**: Program uses modulo division to identify all factors
3. **Pairing**: Factors are paired (first with last, second with second-to-last, etc.)
4. **Display**: Shows individual factors and their multiplication pairs
5. **Continuation**: User can choose to run again or exit

## Technical Implementation

- **Language**: Python 3
- **Key Concepts**: While loops, for loops, list manipulation, modulo operations
- **Data Structures**: Lists for storing factors
- **Control Flow**: Flag-controlled while loop for continuous operation

## Requirements

- Python 3.x
- No external dependencies

## Usage

1. Clone this repository
2. Run the program: `factorapp.py`
3. Follow the on-screen prompts

## Learning Objectives

This project demonstrates:
- While loop control with flags
- For loop iteration and range usage
- List manipulation and indexing
- Modulo operator for divisibility testing
- User input validation and program flow control
- Clean code organization and commenting
