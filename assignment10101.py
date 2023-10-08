while True:
    input_text = input("Enter two word: ")
    
    if input_text == "done" or not input_text:
        break
    
    words = input_text.split()
    
    if len(words) < 2:
        print("Please enter two word.")
    else:
        word1, word2 = words
        if word1 < word2:
            print(f"The word that comes before '{word2}' is '{word1}'.")
        elif word1 > word2:
            print(f"The word that comes before '{word1}' is '{word2}'.")
        else:
            print("Both words are the same.")