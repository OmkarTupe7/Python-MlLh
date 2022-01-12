#Create a list of integers from 1 through 6. Loop through it and check to see if each number is greater than 3
# if it is print out "NUMBER is greater than 3" (replacing number with the current number)

numbers = [1,2,3,4,5,6]

for num in numbers:
    if num > 3:
        print(str(num) +" "+ 'Is greater than 3')
        # print(f'{num} Is greater than 3') #This works in other IDE's