 #Atsutse Johnson Kingsley
      #Index Number = 6930821  
#Question a
w = 10   #This is load intensity of beam
Load_intensity = w

L = 12   #This length of beam
beam_length = L

x = 0   #This marks a distance on the beam 


#M is the Bending Moment of the beam
M = str((w * (-6*x**2 + 6*L*x - L**2))/12)

#V is the Shear Force of the beam
V = str(w * ((L/2) - x))

print('Bending Moment when x = 0 is ' + M + ' KN/m') 
print() #a space between answers in console
print('Shear Force when x = 0 is ' + V + 'KN')
#Calculates Shear Force and Bending Moment when x = 0


x = 12    #when calculating for the Bending moment at the end of the beam, x = L
BM= str((w * (-6*x**2 + 6*L*x - L**2))/12)    #Equation for Bending Moment
print()
print(' Bending Moment when x = 12 is ' + BM + 'KN/m')


V = str(w * ((L/2) - x))   #Equation for 
print()
print(' Shear Force when x = 12 is ' + V + 'KN')
#Calculates for Shear Force and Bending Moment when x = 12


#Question b
a = -6
b = 72
c = -144

com_square = b/(2*a)
#Shows the coefficient of x in the quadratic of the form ax^2 + bx + c = 0 of which we multiply by 1/2

constant = -c/a + com_square**2
#Square the term b/2a and add it to the constant -c/a 
#The constant is - in order to represent the quadratic -6x^2 + 72x - 144 in the form x^2 + bx/a = -c/a 
 

point_of_contraflexure_a = (constant**0.5 - com_square)
point_of_contraflexure_b = (-constant**0.5 - com_square)
#point_of_contraflexure_1 and point_of_contraflexure_2 are roots of the quadratic equation.
print()
print(f'a)The distances at which the bending moment will be zero are x1 = {point_of_contraflexure_a} and x2= {point_of_contraflexure_b}') 


#Question c
V = 0    #To get x, Equate V to zero
x = V + (L/2)   # Solve the original V equation to make x the subject
point_of_zero_shear_force = x 
print()
print('c) ' + str(point_of_zero_shear_force) + ' is the point at which the Shear Force is = 0')


#Question d
import numpy as np
beam_length = 12    #Length of the beam in milimetres(Steps is in milimetres so convert beam_length to milimetres)
steps = 0.01    #(milimetres), convert a step of 10milimetres to metres because the beam_length is in metres
w = 10
span_of_beam = np.arange (0, beam_length + steps, steps)    # list of discretized beam length
x = span_of_beam    #The beam_span is every point on the beam starting from 0 and ending at 12m
M = w * (-6*x**2 + 6*L*x - L**2)/12     # Moment Equation
print()   
print('e) The Moment for each step along the span is {0}'.format(M))
#This is to provide the Bending Moment for each value of x within the beam_span



#Question e
start = 0    #0 is the starting point of our range
step = 0.01    #(milimetres), convert a step of 10mm to m
q = L + step    #L=12metres which is the span of the beam
x = np.arange(start,q,step)
V = w*(L/2 - x)    #V is the shear force
print()
print('(e) The shear force for each step along the span is {}'.format(V))


#Question f
"""
Let the absolute value of the bending moment array be AM
Also let the minimum AM be m_AM
"""
AM = abs(span_of_beam) 
m_AM = min(AM)
"""
When the bending moment is m_AM, we get an expression x**2 - Lx + (L**2/6)+(2*m_AM)/w = 0
"""

#from the above;
a = 1
b = -L
c = (L**2/6)+(2*m_AM)/w
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a
print()
print(f'f)The points along L at which the absolute values of the bending moment array is minimum are {0} and {1}'.format(root_1f,root_2f))     


#Question g
"""
Let the relative errors be R_error
"""
R_error_1 = ((9.464101615137753-9.46)/9.464101615137753*100)
R_error_2 = (( 2.539999999999999-2.5358983848622456)/2.539999999999999*100)
print()
print('(g) The relative errors between estimated points of contra-flexure are {0}% and {1}%'.format(R_error_1,R_error_2))



#Question h
import numpy as np
def calculate_M(w, L, x):
    return(w * (-6*x**2 + 6*L*x - L**2)/12)

beam_length = 12
steps = 10
BMoment_values = []

for x in span_of_beam:
    M = calculate_M(w, L, x)
    BMoment_values.append(M) 
    
max_Y = max(BMoment_values) 
min_Y = min(BMoment_values)
print()
print("h) Maximum bending moment:", max_Y) 


print()
print("Minimum bending moment:", min_Y) 
print()
print()
print('#GITHUB USERNAME =  JAKE-12345')
