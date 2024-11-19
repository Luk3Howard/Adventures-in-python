#deckaring the dictionary, dictionary keys and data can be different data types
myDict = {"One":1.35, 2.5:"Two Point Five", 3:"+", 7.9:2}


#print the entire dictionary
print (myDict)
#note: may display in a different order than the one I've declared them in!


#print the item with key = "One"
print (myDict["One"])


#print the item with key = 7.9
print (myDict[7.9])


#modify the item with key = 2.5 to "Two and a Half" and print the updated dictionary
myDict[2.5] = "Two and a Half"
print (myDict)


#add a new item and print the updated dictionary
myDict["Luke"] = "An absolute legend and should be more confident in himself! You got this bro!"
print (myDict)


#remove the item with the key = "One" and print the updated dictionary
del myDict["One"]
print (myDict)
