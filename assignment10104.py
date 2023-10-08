while True:
    input_text = input("Enter a string : ")
    if input_text.lower() == 'done':
        break
    cleaned_text = input_text.translate(str.maketrans("" ,"",',.:!?'))
    cleaned_text = cleaned_text.upper()
    print("Processed string:", cleaned_text)