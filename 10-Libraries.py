# We can import libraries with the import statement
import random


# another cool library is called matplotlib
# Instead of importing all of matplotlib, we're only import pyplot, and we're giving it a new name: plt!
import matplotlib as plt

# Now for the big one. There's a library called pandas that we're going to use a lot
# It helps us interact with the kind of data you would find in a spreadsheet

import pandas as pd

#Then use things from those libraries with the dot operator like this:
random.random()

# If you ever want to know all the stuff you can access with a dot, you can use the dir() function
# tho be careful, its output can be a little overwhelming sometimes
dir(random)

x = [0, 1, 2, 3, 4, 5, 6]
x_squared = [0, 1, 4, 9, 16, 25, 36]

plt.plot(x, x_squared)

raw_data = {
    'state': ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois', 'Ohio', 'Georgia'],
    'abbreviation': ['CA', 'TX', 'FL', 'NY', 'PA', 'IL', 'OH', 'GA'],
    'population': [39613493, 29730311, 21944577, 19299981, 12804123, 12569321, 11714618, 10830007],
    'number_starbucks': [2821, 1042, 694, 645, 357, 575, 378, 326]
}

df = pd.DataFrame(raw_data)