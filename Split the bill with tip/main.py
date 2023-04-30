print("Welcome to the tip calculator.\n")
a = float(input("What is your total bill?\n$"))
print("What percentage tip would you like to give?")
b = int(input())
print("how many people to split the bill?")
c = int(input())

d = ((b / 100) * a + a) / c
d = "{:.2f}".format(d)
print(f"Each person should pay : ${d}")
