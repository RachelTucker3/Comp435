import sys
#print(sys.argv[0]) #the command
#print(sys.argv[1]) #the parameter to the command (what you will be working with)


my_set = open(sys.argv[1]).read().split("\n") #transforms inputted text file into a list
#print(my_set)
my_dict = {i: my_set.count(i) for i in my_set} #creates a dictionary where the keys are then number of times a component is repeated
#print(my_dict)
for x in my_dict:
    if x[0] == '0': #takes care of the cases of a number starting with 0
        if len(x) > 1:
            copy = x.replace('0', '')
        if copy[0] == 0: #if my copy is now empty because the value was all zeros
            copy = '0'
            print copy, my_dict[x];
        else: #if my copy isn't empty after deleting zeroes
            print copy, my_dict[x];
    else: #if my string does not begin with a zero
        print x,my_dict[x]
