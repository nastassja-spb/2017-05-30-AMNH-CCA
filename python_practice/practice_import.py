'''
Here is the docstring:
We will use this to see how we can import from another module.
''' 

import practice_script as ps

print (ps.sample_int)
myalg = ps.Algebra(1.5, 5.0)
#no print statement below
myalg.multiply()
print (myalg.multiply())# this *does* have a return value
 

for x in [1,3,5] :
# Let's loop over different values fo r the first argument in the Algebra class
    myalg = ps.Algebra(x, 5.0)
    print (myalg.add())
