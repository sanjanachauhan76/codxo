import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTVWXYZ"
lowercase_leters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*()_"

upper, lower, nums, syms = True, True, True, False

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_leters
if nums:
    all += digits
if syms:
    all += symbols

length  =10
amount = 100

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)