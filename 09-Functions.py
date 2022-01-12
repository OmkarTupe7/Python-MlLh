# Functions let us package up a bit of code to reuse multiple times

def my_adding_function(foo, bar):
    my_sum = foo + bar
    return my_sum
    

# In the above function...
# def is our keyword that says we're writing a function
# my_adding_function is the name of our function, this is what we'll use later to call it
# (foo, bar) are our arguments--these are the inputs to our function
# the colon (:) tells us we're entering an indented code block, and that the function continues until we unindent
# my_sum = foo + bar is the core logic of our function
# return my_sum is our return statement--this shows us what the function gives us back when we call it
