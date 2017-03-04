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

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "Or he is %d centimeters tall." % inches_to_cm(height)
print 'He weighs %d pounds.' % weight
print 'Or he weighs %r kilograms.' % round(lbs_to_kg(weight),1)
print 'He has %s hair and %s eyes.' % (hair_color, eye_color)
print 'And! His teeth are %s.' % teeth_color

print 'If I add %d, %d, and %d I get %d.' % (weight, height, age, weight + height + age)
