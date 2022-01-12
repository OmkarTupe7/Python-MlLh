# We can use loops to do something multiple times--this is really helpful for working with lists

students = {'Nitin','Leena','Priti'}
for student in students:
    print('Welcome to my Class in Python ' + student)

# We can also use Logical Statements in Python

list = [1,2,3,4,5,6,7,8,9,10]
for num in list:
    if num >= 5:
        break
    else:
        print(num)
