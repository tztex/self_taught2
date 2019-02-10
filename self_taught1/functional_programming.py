#state is value of a programs variable while running
#global is global state
#eliminate global states and keep track of data by passing from one function to another
#advantage is eliminates global state errors

a = 0

def increment():
    global a
    a += 1

def increment(a):
    return a + 1