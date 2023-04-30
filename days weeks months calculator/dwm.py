age = input("What is your current age")

a = int(age)

y = 90 - a
d = y * 365
w = y * 52
m = y * 12

message = f"You have {d} days, {w} weeks, {m} months left"
print(message)
