# Remove special symbols from string python

def remove_special_symbols(input_string):
    processed_string = ""
    
    for char in input_string:
        if char.isalnum() or char.isspace():
            processed_string += char
    
    return processed_string

# Example usage:
my_string = "Hello @World! How are you?"
result = remove_special_symbols(my_string)
print(result)