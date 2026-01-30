def distribution_analysis(numbers):

    dictionary = {}                    #creating the dictionary

    for number in sorted(set(numbers)):   #first loop that iterate through each number of the list without duplicates
        count = 0
        for n in numbers:
            if n <= number:
                count += 1
        percentage_of_elements = (count/len(numbers))*100  #calcutating the percentage
        dictionary[number] = percentage_of_elements  #assigning the percentage to the number

    return dictionary

lst = [3, 1, 2, 3, 4, 2]

