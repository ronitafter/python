
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

