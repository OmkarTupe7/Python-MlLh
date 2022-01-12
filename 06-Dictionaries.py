# Sometimes out data doesn't really fit in a list--if we have pairs of values we can use a dictionary!
cityPopulations = {
   # Mumbai is the key and 520000 is the value
    'Mumbai' : 520000,
    'Navi-Mumbai' : 875675
}
print(cityPopulations)

# To get a specific value we can index it with key
print(cityPopulations['Mumbai'])

# To add a key value pair/update, we can assign it like this:
cityPopulations ['Wardha'] = 25000
cityPopulations ['Mumbai'] = 785432
print(cityPopulations)

# We can also get all the keys and values of a dictionary with the .keys()/.values() method
print(cityPopulations.keys())
print(cityPopulations.values())