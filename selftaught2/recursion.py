# iterative algorithms use loops
# recursive rely on functions that calls themself
# write recursive inside function with a base case
# base case condition that ends function from calling itself
# 3 laws of recursion. 1. must have base case.
# 2. must change state and move to base case
# 3. must call itself recursively

# example
def bottles_of_beer(bob):
    if bob < 1:
        print("""No more bottles of beer on the wall. No more 
                 bottles of beer.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall. {} bottles
             of beer. Take one down, pass it around, 
             {} bottles of beer on the wall.""".format(tmp, tmp, bob))
    bottles_of_beer(bob)

def print_to_zero(n):
    if n < 0:
        return
    print(n)
    print_to_zero(n - 1)

print_to_zero(5)