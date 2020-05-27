#list1 = [1, 5, 4]
#list2 = ["hello", "world"]
#list3 = [23, 5.6, -17, "computer"]
#list4 = []
#print(list3)
#print(len(list3))
#print([1,2] + [3])
#print( list1 +[888])
#print( list1 +[888, 999])
#print( list1 + list4)
#print([1,2] * 4)
#print(list3 * 2)
#print([1,2] == [2,1])
#print([1,2] == [1] + [2])
#print(2 in [1,2]) #true
#print(3 in [1,2]) #false
#print("hello" in list2)
#print(list3[0])
#print(list3[1])
#print(list3[2])
#i = 3
#print(list3[i])
#print(len(list1 + list2))
#print(len(list1*10))
#print(list1[2])
#print(list1[2] + list2[1])
#print(list3 + 3)
#print(list == [5,4] + [1])
#print(list4 + [1,5,4] == list1)

#max-min
#list = [4,8,3,1]
#print(max(list))
#print(min(list))

#sorted
#print(sorted(list))

#list = sorted(list)
#print(list)
#print(sorted([1, "hello"]))#TypeError: '<' not supported between instances of 'str' and 'int'
#print(sorted(["hello", "world", "aaa"]))

#list1 = [1,2,3]
#list2 = "hello world"
#list1[0] = 10
#list2[0] = "A"
#print(list2) #TypeError: 'str' object does not support item assignment

#sum

#print(sum([1,2,3,4]))


#
L1 = [5, 1, 4, 3, 2]
L2 = [7, 6, 8]
L3 = []

#print(max(L1)) #5
#print(min(L2)) #6
#print(min(L1) + max(L2)) #9
#print(min(L3) + max(L2)) #ValueError: min() arg is an empty sequence
#print(sorted(L2 + L1) == sorted(L2) + sorted(L1)) #false
print(sorted(L3))



