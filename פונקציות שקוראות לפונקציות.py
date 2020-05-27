##def max2(a,b):
##        if a > b:
##                return a
##        else:
##                return b
##
##def max3_vs(a,b,c):
##        max_a_b = max2(a,b) # b (2)
##        max_all = max2(max_a_b, c) #max2(2, 3) #c(3)
##        return max_all
##
##result = max3_vs(1,2,3)
##print(result)


##def max2(a,b):
##        if a > b:
##                return a
##        else:
##                return b
##
##def max3_vs(a,b,c):
##        return max2(max2(a,b),c)
##
##result = max3_vs(1,2,3)



##
##def max2(a, b):
##        if a > b:
##                return a
##        else:
##                return b
##
##def max3(a, b, c):
##        max_a_b = max2(a, b) # b (2)
##        max_all = max2(max_a_b, c) #max2(2, 3) #c(3)
##        return max_all
##
##def max4_v1(a, b, c, d):
##        max_a_b_c = max3(a, b, c)
##        max_all = max2(max_a_b_c, d)
##        return max_all
##
##result = max4_v1(7,13,0,42)
##print(result)



##def max2(a, b):
##    if a > b:
##        return a
##    else:
##        return b
##
##def max3_v3(a,b,c):
##    max_a_b = max2(a,b)
##    max_all = max2(max_a_b, c)
##    return max_all
##
##def max10(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
##    x = max3_v3(a1, a2, a3)
##    y = max3_v3(a4, a5, a6)
##    z = max3_v3(a7, a8, a9)
##    max_xyz = max3_v3(x, y, z)
##    result = max2(max_xyz, a10)
##    return result
##
##res = max10(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
##print(res)
#



def max2(a,b):
    if a > b:
        return a
    else:
        return b

def max3(a,b,c):
    max_a_b = max2(a,b)
    max_all = max2(max_a_b, c)
    return max_all
    
def max4_v1(a,b,c,d):
    max_a_b_c = max3(a,b,c)
    max_all = max2(max_a_b_c, d)
    return max_all
    
def max4_v2(a,b,c,d):
    ab = max2(a,b)
    cd = max2(c,d)
    res = max2(ab,cd)
    return res
    
    




### TESTS ###

print("********************")
print("Starting the test:")

print("********************")
print("Checking the maximum between 3, 7, 12, -20")
ans = max4_v2(3, 7, 12, -20)
if ans == 12:
    print("CORRECT: Very good, 12 is the maximal number")
else:
    print("WRONG: 12 is the maximal number but the code returned", ans)

print("********************")
print("Checking the maximum between -10, -20, -25, -12")
ans = max4_v2(-10, -20, -25, -12)
if ans == -10:
    print("CORRECT: Very good, -10 is the maximal number")
else:
    print("WRONG: -10 is the maximal number but the code returned", ans)




### EXTRA TESTS ###

import validation

print("********************")
print("\n\nNow checking your implementation:")

print("Checking that max4_v2 does not call max3")
if validation.test_no_max3(max4_v2):
    print("CORRECT: Very good, max4_v2 does not call max3")
else:
    print("WRONG: max4_v2 calls max3")    
    
print("********************")
print("Checking that max4_v2 calls max2")
if validation.test_max2(max4_v2):
    print("CORRECT: Very good, max4_v2 calls max2")
else:
    print("WRONG: max4_v2 does not call max2")    
    
print("********************")    
print("Tests concluded, add more tests of your own below!")
print("********************")





        
