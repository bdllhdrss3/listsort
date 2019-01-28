
mylist = [2,0,6,5,1,7,'z','a']

        #separating digits from chars in list before making dictonary
numbers = [x for x in mylist if x in range(0,100)]
chars= [x for x in mylist if x not in range(0,100000)]

        #getting evens and odds from the pre made variable of numbers

evens1 = str([x for x in numbers if x%2 == 0 and x != 0])
odd1 = str([x for x in numbers if x%2 == 1 and x != 0])
        #creating the dictionary
dictionary ={}
        #filling in the keys and values in the dictionary

dictionary['Odd'] = odd1
dictionary['Evens'] = evens1
dictionary['Chars'] = chars
print('\n\n')
        
print('the dictionary is here sir!\n')
print(dictionary)
print('\n')
