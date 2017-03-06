name = 'Matt Bruton'
age = 31
height = 70
weight = 160
eye_color = 'Brown'
hair_color = 'Brown'
teeth_color = 'White'

def inches_to_cm(height_in_inches):
    return height_in_inches * 2.54;

def lbs_to_kg(weight_in_lbs):
    return weight_in_lbs * 0.453592;

print("Let's talk about {}.".format(name))
print("He's {} inches tall.".format(height))
print("Or he is {} centimeters tall.".format(inches_to_cm(height)))
print('He weighs {} pounds.'.format(weight))
print('Or he weighs {} kilograms.'.format(round(lbs_to_kg(weight), 1)))
print('He has {0} hair and {1} eyes.'.format(hair_color, eye_color))
print('And! His teeth are {}.'.format(teeth_color))

print('If I add {0}, {1}, and {2} I get {3}.'.format(weight, height, age, weight + height + age))
