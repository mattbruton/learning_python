try:
    count = int(input("Give me a number: \n"))
except ValueError:
    print("That's not a number :(")
else:
    while count:
        print("Hi, {}".format(count))
        count -= 1
