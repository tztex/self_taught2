hrs = input("Enter Hours")
h = float(hrs)
rate = input("Enter Rate")
r = float(rate)
if h > 40:
    pay = 40 * r
    ot = (h - 40) * (r+(r/2))
    total = pay + ot
    print(total)
else:
    pay = h * r
    print(pay)
