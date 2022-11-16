import operator

# This module exports a set of functions corresponding to the intrinsic
# operators of Python.  For example, operator.add(x, y) is equivalent
# to the expression x+y.  The function names are those used for special
# methods; variants without leading and trailing '__' are also provided
# for convenience.

#Defining a  dictionary
dict = {1: "Om", 3: "Aditya", 4: "Papa", 2: "Mummy", 0: "Shree"}
print('Original dictionary : ',dict)

#By keeping the keys in ascending order
sorted_k=sorted(dict.items())
print('Dictionary in ascending order by value : ',sorted_k)


#By keeping the values in ascending order using Operator
sorted_vo= sorted(dict.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_vo)

#By keeping the values in ascending order using Lambda
sorted_vl = sorted(dict.items(),key=lambda item: item[1])
print('Dictionary in ascending order by value : ',sorted_vl)

