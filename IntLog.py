from scipy import integrate
import numpy as np

# Define the parameters
# provide a,b and r the desired value
a = int(input("enter the value of alpha: "))
b = int(input("enter the value of beta: "))
r = int(input("enter the value of r: "))

# Definition of function to integrate
def f(t):
    return a**t * np.log(1 - (t**(1/b))**r)

# Perform the integral from 0 to 1
result, error = integrate.quad(f, 0, 1)

print("The integral is:", result)
print("The absolute error is:", error)
