#declaring the list, list elements can be of different data types
myList = [1, 2, 3, 4, 5, "Hello"]


#print entire list
print (myList)
#will return [1, 2, 3, 4, 5, "Hello"]


#print the third item (remember: index starts from 0!)
print (myList[2])
#will return 3


#print the last item in the list
print (myList[-1])
#will return "Hello"


#assign myList (from index 1 to 4) to myList2 and print myList2
myList2 = myList[1:5]
print (myList2)
#will return 2, 3, 4, 5


#modify the 2nd item in myList and print the updated list
myList[1] = 20
print (myList)
#will return 1, 20, 3, 4, 5, "Hello"


#append a new item to myList and print the updated list
myList.append("How are you?")
print (myList)
#will return 1, 20, 3, 4, 5, "Hello", "How are you?"


#remove the sixth item from myList and print the updated list
del myList[5]
print (myList)
#will return 1, 20, 3, 4, 5, "How are you?"
