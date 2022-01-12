# If statements let us check some condition, and only run code if that condition is True

cheeseonpizza_aregood = True
if cheeseonpizza_aregood:
    print('Cheese Superiority and we all agree!') 
else:
    print('What kind of alien are you?')

pineappleonpizza = False
if pineappleonpizza:
    print('Call the Police1')
else:
    print('What do you want?')

# We can also use comparision operators

myAge = 19
if myAge >= 18:
    print('You can get your Driving License')
else:
    print("You should be 18 or above")

# And logical operators here instead of using else-if we elif

temperature_C = 21
weather = 'windy'

if temperature_C > 30 and weather == 'Sunny':
    print("Its a Sunny Day!")
elif temperature_C < 18 and weather == 'Snowy':
    print('Stay Inside your houses')    
else:
    print("Normal Cold & Cloudy")    