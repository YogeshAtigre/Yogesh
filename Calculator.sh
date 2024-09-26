#!/bin/bash

# Prompt the user for input
read -p "Enter the first number: " num1
read -p "Enter the second number: " num2
read -p "Enter an operator (+, -, *, /): " operator

# Perform the calculation based on the operator
if [[ "$operator" == "+" ]]; then
    result=$(echo "$num1 + $num2" | bc)
elif [[ "$operator" == "-" ]]; then
    result=$(echo "$num1 - $num2" | bc)
elif [[ "$operator" == "*" ]]; then
    result=$(echo "$num1 * $num2" | bc)
elif [[ "$operator" == "/" ]]; then
    if [[ "$num2" == 0 ]]; then
        echo "Error: Division by zero is not allowed."
        exit 1
    else
        result=$(echo "scale=2; $num1 / $num2" | bc)
    fi
else
    echo "Invalid operator. Please use +, -, *, or /."
    exit 1
fi

# Display the result
echo "Result: $num1 $operator $num2 = $result"

