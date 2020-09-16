import sys
#print(sys.argv[0]) #the command
#print(sys.argv[1]) #the parameter to the command (what you will be working with)

my_dict_unsort = {}
my_set = open(sys.argv[1]).read().split("\n") #transforms inputted text file into a list
for var in my_set: #turns the list of strings into a list of integers and puts them in a dictionary where the keys are the number of times the component is repeated
    hex = int(var, 16) #base 16 hex
    if not hex in my_dict_unsort:
        my_dict_unsort[hex] = 1
    else:
        my_dict_unsort[hex] += 1
#print(my_set)
#print(my_dict)
vars = my_dict_unsort.keys()
vars.sort(); #sorts all my int variables

for x in vars: #iterates through my sorted keys and prints their string value and the number of times they repeat
    if my_dict_unsort[x] >= 2:
        #print x,my_dict_unsort[x]
        print "%x" % x + " " + str(my_dict_unsort[x])
