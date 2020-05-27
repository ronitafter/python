#קלט
start = 10000 #int
spend_list = [1200, 900, 354, 1300, 550, 620, 550, 715] #list
total = sum(spend_list)
#פלט
#הוצאות
print("Total:", total) #(מחרוזת,משתנה) #א#total=6189
money_left = start - total
print("you have", money_left, "dollars") #you have 3811 dollars
#ממוצע הוצאות
average = total / len(spend_list)
print("the average per week", average) #the average per week 773.625
#כמה זמן נשאר לטייל
weeks_left = money_left / average
print("you have approximately", weeks_left, "weeks left to travel")
#you have approximately 4.926159314913557 weeks left to travel


