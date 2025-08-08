# thisset = {'a','b','c','d'}
# print(thisset)



import copy
thislist = []


shallowcoppy = copy.copy(thislist)
thislist[1] = "hello"

shallowcoppy[0] = "hdgj"
print(shallowcoppy)
print(thislist)







deepcopy = copy.deepcopy(thislist)



