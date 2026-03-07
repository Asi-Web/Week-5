## Asiwome Agbleze
## CMSC 11s1/1
## Spring 2026
## Week 5 Assignment 1

def extract_character(text, start, length):
    # This extracts a substring starting at index 'start' and spanning 'length' characters using slincing
    end = start + length
    return text[start:end]

    def reverse_string(text):
        # Reverses the given string using slicing.
        return text[::-1]
    
    # Get user input
    user_text = input("Enter a string: ")

    start_index = int(input("Enter the starting index "))
    length = int(input("Enter the length: "))

    # Extract substring
    extracted = extract_character(user_text, start_index, length)

    # Reverse string
    reversed_text = reverse_string(user_text)

    # Display results
    print("\nResults:")
    print("Extracted substring:", extracted)
    print("Reversed string:", reversed_text)
