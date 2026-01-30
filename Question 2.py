def dict_function(lst):
    dictionary = {}                 #creating an empty dictionary to store the values
    for x in lst:
        length = len(x)              #determining the length of the word
        if length % 2 == 0:         #determining the parity of the word
            parity = "even"
        else : parity = "odd"
        dictionary[x] = {"length":length, "parity":parity}             #updating the dictionary
    return dictionary