"""
This is a rest style.
If input is divisible by 3, it prints fizz
If input is divisible by 5, it prints buzz
If input is divisible by both 3 and 5, it prints FizzBuzz
Anything else is returned
"""


def fizz_buzz(input):
    fizz = input % 3
    buzz = input % 5
    if fizz == 0 and buzz == 0:
        print("FizzBuzz")
    elif fizz == 0:
        print("Fizz")
    elif buzz == 0:
        print("Buzz")
    else:
        print(input)


fizz_buzz(5)
