#list1 = [[4, 5, 3], [-77, "abc"]]
#print(len(list1)) # 2
#print(list1[0]) # [4, 5, 3]
#print(list1[1]) # [-77, 'abc']
#print(list1[0][0]) # 4
#print(list1[0][2]) # 3

#inner_list = list1[0]
#print(inner_list[2]) #3
#print(list1[0][2][0]) # TypeError: 'int' object is not subscriptable
#print(list1[1][1][0]) # a

#L = [1, [2], ["a", "list"]]
#print(L[0][1]) #TypeError: 'int' object is not subscriptable
#print(len(L)) # 3

#L = [1, [2], [“a”, “list”] ]
#print(L[2][1][0]) #l(L)

##table = [[4, 7, 8, 9],
##        [6, 0, -3, 1],
##        [12, 3, 4, 2]] #list
#print(len(table)) # 3
#print(sum(table[0])) # 28
##s0 = sum(table[0])
##s1 = sum(table[1])
##s2 = sum(table[2])
#print(s0 + s1 + s2) # 53
##sums_list = ( s0, s1, s2)
##print(sum(sums_list))
#print(len(table[0])) # 4
#print(table[0]) # [4, 7, 8, 9]
#print(table[0][3]) # 9
#print(table[0][1][0]) # TypeError: 'int' object is not subscriptable

##Commentout: Alt + 3
##Uncomment: Alt + 4

##T = [
## [1, 2, 3],
## [4, 5, 6],
## [7, 8, 9]
## ]
##
##i=0
##j=1

##print(T[i][j]) # 2
##print(T[j][i]) # 4
##print(T[0] + T[1]) #[1, 2, 3, 4, 5, 6]
##print(T[1][2] + T[2][0]) # 13
##print(T[2] * T[0][1]) [7, 8, 9, 7, 8, 9]
##print(sum(T)) # TypeError: unsupported operand type(s) for +: 'int' and 'list'
##print(sum(T[1])) # 15

table = [ [6, 9, -18, 12, 21],
          [5, 20, 0, 4, 16],
          [-6, 5, -12, -6, -13]]

table_sum = 0
table_min = 0
table_max = 0
sorted_table = []

# Write your code here:

s0 = sum(table[0])
s1 = sum(table[1])
s2 = sum(table[2])
table_sum = ( s0, s1, s2)
#print(sum(table_sum)) # 43

m0 = max(table[0])
m1 = max(table[1])
m2 = max(table[2])
table_max = (m0, m1, m2)
print(max(table_max)) # 21

mi0 = min(table[0])
mi1 = min(table[1])
mi2 = min(table[2])
table_min = (mi0, mi1, mi2)
print(min(table_min)) # -18


o0 = sorted(table[0])
o1 = sorted(table[1])
o2 = sorted(table[2])
table_sorted = (o0, o1, o2)
print(sorted(o0 + o1 + o2)) # [[-18, 6, 9, 12, 21], [-13, -12, -6, -6, 5], [0, 4, 5, 16, 20]]



