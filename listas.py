list = ["a", "b", "c"]
different_list = ["A", 2, "C", 4.4]
#print(different_list[0])
list[1] = "8"
#print(list)

#--------------------------------------------------
large_list = ["Python","Java","C++","JavaScript"]
small_list = large_list[0:3]
#print(small_list)
large_list[3:5] = ["C#","PHP"]
#print(large_list)
#-------------------------------------------------
list_1 = [1,3]
list_1.append(4) #Adding to the list item at the end
#print(list_1)
list_1.append([5,6])
#print(list_1) # [1, 3, 4, [5, 6]]
list_1.insert(1,2) #(index,value)
#print(list_1)

letters = ["x","y","z"]
letters.remove("z") #Removing the value
#print(letters)

number = [1,2,2,2,2,3,4,5]
number.remove(2) #Removes the first element with value 2 
print(number.count(2)) #Count how many elements with that value there
#print(number)

names = ["Juan","Miguel","Silvia"]
names.pop() #Removes the last item from the list
#print(names)

names.pop(1) #Passing the index parameter
print(names)