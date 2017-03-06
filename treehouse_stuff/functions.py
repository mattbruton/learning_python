def hows_the_parrot():
    print('He\'s pining for the fjords!')

hows_the_parrot()

def lumberjack(name):
    if name.lower() == 'matt':
        print('{} is a lumberjack and he\'s OK!'.format(name))
    else:
        print('{0} sleeps all night and {0} works all day!'.format(name))

lumberjack(input('What\'s your name?\n'))

def average(num1, num2):
    return (num1 + num2) / 2

print(average(4, 10))
