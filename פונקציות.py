## built-in functions ##

# 1. len(input/parameter) # 16 = output
# print(?)

#n = len("this is a string") # n: variable # 16 = output
#print(n) # input

##n = len("this is a string")
##print(n)
##if n > 10:
##    print("this is a long string")
##elif n < 5:
##    print("this is a short string")
##


##L = [2, 1, 3]
##print(min(L) + max(L))
# 1. min
# 2. max
# 3. min + max
# 4. print



##lst = [1, -15, 20] 

##x = max(lst) #20
##y = sum(lst) #6
##z = len(lst) #3
##
##result = min(x, y, z)
##
##print(x)
##print(y)
##print(z)
##
##print(result)


##result = print(1+2)
##print(result)  # 3, None


##print(3)+print(4) #TypeError: unsupported operand type(s) for +: 'NoneType'
###and 'NoneType'

##L = [1,4,5,3,2]
##L = sorted(L)
##print(L)

##L = [1,4,5,3,2]
##L_sort = sorted(L)
##print(L_sort)
##print(L)


##def max2(a, b):
##    if a > b:
##        return a
##    else:
##        return b
##
##
##result = max2(3,5)
##print(result)
##result2 = max2(4,-5)
##print(result2)
##x = 2
##y = -2
##result3 = max2(x,y)
##print(result3)

##result4 = max2(x + y + 3, x * y)
##print(result4)
##

##def max3_v1(a,b,c):
##    if a > b:
##        if a > c:
##            return a
##        else:
##            return c
##    else:
##        if b > c:
##            return b
##        else:
##            return c
##
##result5 =  max3_v1(1,2,3)
##print(result5)

##
##and
##
##def max3_v2(a,b,c):
##    if a > b and a > c:
##        return a
##    else:
##        if b > a and b > c:
##            return b
##        else:
##            return c
##
##result6 =  max3_v2(1,2,3)
##print(result6)
##

##def avg(lst):
##    return sum(lst)/len(lst)
##
##lst = [1,2,3,4,5]
##res = avg(lst)
##print(res)



##def max3_v2(a,b,c):
##    if a > b and a > c:
##        return a
##    elif b > a and b > c:# elif = else:....if
##        return b
##    else:
##        return c
##
##result6 =  max3_v2(1,2,3)
##print(result6)

##
##x = 15
##
##if x < 10:
##    x = x + 8
##else:
##    if x > 20:
##        x = x + 1
##
##print(x)



##x = 15
##
##if x < 10:
##    x = x + 8
##elif x > 20:
##    x = x + 1
##elif x > 10:
##    x = x + 1
##
##print(x)


##x = 15
##
##if x < 10:
##    x = x + 8
##else:
##    x = x + 1
##
##print(x)


##def what(st, c):
##    if c in st:
##        return True
##    else:
##        return False
## 
##print(what("hello", "t")) # False
##print(what("hello", "e")) # True



##def add1(n):
##    n = n + 1
##    return n
##
##n = 6
##
##print(add1(6))
##print(n)


##def add1(n):
##    n = n + 1
##    return n
##
##n = 6
##n = add1(n)
####m = add1(n)
##
##print(add1(n))

##
##def what(string, char):
##	if char*3 in string:
##		return True
##	else:
##		return False
##
##letter = "a"
##text = "hello aaa world"
##
##print(what(text, letter))

##def max3_v1(a,b,c):
##    if a > b:
##        if a > c:
##            return a
##        else:
##            return c
##    else:
##        if b > c:
##            return b
##        else:
##            return c
##a = 1
##b = 2
##c = 3
##result = max3_v1(a,b,c)
##print(result)


def max2(a, b):
    # delete pass and fill in your code below
    if a > b:
        return a
    else:
        return b
      
### TESTS ###

##print("********************")
##print("Starting the test:")
##
##print("********************")
##print("Checking the maximum between 3, 12")
##ans = max2(3, 12)
##if ans == 12:
##    print("CORRECT: Very good, 12 is the maximal number")
##else:
##    print("WRONG: 12 is the maximal number but the code returned", ans)
##
##print("********************")
##print("Checking the maximum between -3, -12")
##ans = max2(-3, -12)
##if ans == -3:
##    print("CORRECT: Very good, -3 is the maximal number")
##else:
##    print("WRONG: -3 is the maximal number but the code returned", ans)
##
##print("********************")
##print("Checking the maximum between 0, 0")
##ans = max2(0, 0)
##if ans == 0:
##    print("CORRECT: Very good, 0 and 0 are equal so 0 is also the maximal number")
##else:
##    print("WRONG: 0 is the maximal number but the code returned", ans)
##    
##print("********************")    
##print("Tests concluded, add more tests of your own below!")
##
##if max2(4.5, 81.25) == 81.25:
##    print("Good")
##else:
##    print("Bad")
##

##def min2(a, b):
##    if a > b:
##        return b
##    else:
##        return a
##    
##### TESTS ###
##
##print("********************")
##print("Starting the test:")
##
##print("********************")
##print("Checking the minimum between 10 and 3")
##ans = min2(10, 3)
##if ans == 3:
##    print("CORRECT: Very good, 3 is smaller than 10")
##else:
##    print("WRONG: 3 is smaller than 10 but the code returned", ans)
##    
##print("********************")
##print("Checking the minimum between -1 and -7")
##ans = min2(-1, -7)
##if ans == -7:
##    print("CORRECT: Very good, -7 is smaller than -1")
##else:
##    print("WRONG: -7 is smaller than -1 but the code returned", ans)
##
##print("********************")
##print("Checking the minimum between 10 and 10")
##ans = min2(10, 10)
##if ans == 10:
##    print("CORRECT: Very good, 10 is equal to 10 therefore it also the minimal number")
##else:
##    print("WRONG: 10 is equal to 10 therefore it is also the minimal number but the code returned", ans)
##
##print("********************")    
##print("Tests concluded, add more tests of your own below!")
##print("********************")
##
    

def max4(a, b, c, d):
    if a > b:
        if a > c:
            if a > d:
                return a
            else:
                return d
        else:
            if c > d:
                return c
            else:
                return d
    else:
        if b > c:
            if b > d:
                return b
            else:
                return d
        else:
            if c > d:
                return c
            else:
                return d

print("********************")
print("Starting the test:")

print("********************")
print("Checking the maximum between 1, 3, 5, 7")
ans = max4(1, 3, 5, 7)
if ans == 7:
    print("CORRECT: Very good, 7 is the largest number")
else:
    print("WRONG: 7 is the largest number but the code returned", ans)
    
print("********************")
print("Checking the maximum between 7, 1, 3, 5")
ans = max4(7, 1, 3, 5)
if ans == 7:
    print("CORRECT: Very good, 7 is the largest number")
else:
    print("WRONG: 7 is the largest number but the code returned", ans)
    
print("********************")
print("Checking the maximum between 1, 7, 3, 5")
ans = max4(1, 7, 3, 5)
if ans == 7:
    print("CORRECT: Very good, 7 is the largest number")
else:
    print("WRONG: 7 is the largest number but the code returned", ans)
    
print("********************")
print("Checking the maximum between 1, 3, 7, 5")
ans = max4(1, 3, 7, 5)
if ans == 7:
    print("CORRECT: Very good, 7 is the largest number")
else:
    print("WRONG: 7 is the largest number but the code returned", ans)
    
print("********************")
print("Checking the maximum between -5, -5, -5, -5")
ans = max4(-5, -5, -5, -5)
if ans == -5:
    print("CORRECT: Very good, -5 is the largest number")
else:
    print("WRONG: -5 is the largest number but the code returned", ans)
            
print("********************")    
print("Tests concluded, add more tests of your own below!")
print("********************")

            
        
        

