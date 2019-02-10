import statistics
import keyword

#divide large programs into modules
#must import it first to use variables and functions
#import math math.pow(2,3)
#statistics to calculate mean, average,
#use keyword module to see if a string is a python keyword
#create module, import in another module and use code from it
    #create tsp folder
    #create module_one.py
        #put in def print_hello():
        #print ("Hello")
# mean
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(nums))
# median
print(statistics.median(nums))
# mode
print(statistics.mode(nums))

print(keyword.iskeyword("for"))

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.variance(data))

