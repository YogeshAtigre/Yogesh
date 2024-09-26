#!/bin/bash

# Check if a file argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Check if the file exists
if [ ! -e "$1" ]; then
    echo "File '$1' does not exist."
    exit 1
fi

# Get the counts for lines, words, and characters using wc
line_count=$(wc -l < "$1")
word_count=$(wc -w < "$1")
char_count=$(wc -m < "$1")

# Display the results
echo "File: $1"
echo "Number of lines: $line_count"
echo "Number of words: $word_count"
echo "Number of characters: $char_count"

