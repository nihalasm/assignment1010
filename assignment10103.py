def count_characters(input_string):
    num_count = 0
    upper_count = 0
    lower_count = 0
    other_count = 0
    for char in input_string:
        if char.isnumeric():
            num_count += 1
        elif char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        else:
            other_count += 1
    return num_count, upper_count, lower_count, other_count
input_string = input("Enter a string: ")
num_count, upper_count, lower_count, other_count = count_characters(input_string)
print("Number of numbers:", num_count)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
print("Number of other characters:", other_count)