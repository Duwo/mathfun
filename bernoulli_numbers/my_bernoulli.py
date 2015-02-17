from fractions import Fraction as Fr
import matplotlib
from matplotlib import pyplot as pl
import numpy as np
import math

def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result

def bernoulli(m):
  A = [0] * (m+1)

  for k in range(0, m+1):
    p_plus = k + 1
    if k == 0:
      A[k] = 1
    else:
      sum_previous_bernullis = 0
      for i in range(0,k):
        sum_previous_bernullis += binomialCoeff(p_plus, i) * A[i]
      A[k] = Fr(p_plus - sum_previous_bernullis, binomialCoeff(p_plus,k))
  return A

if __name__ == "__main__":
  # plot the numbers
  # Choose how many
  n = 50

  # Essential arrays
  x = np.linspace(0, n-1, n)
  y_numerator = np.zeros(n)
  y_denominator = np.zeros(n)
 
  # Bernoulli numbers
  A = bernoulli(2*n)

  # Number of digits in numerator and in denominator
  for i in range(0,n):
    if(A[i] != 0):
      y_numerator[i] = math.ceil(math.log(abs(A[i].numerator))) +1
      y_denominator[i] = math.ceil(math.log(abs(A[i].denominator))) +1 

  # Remove zero valued Numbers and move to new arrays
  x_plot = []
  y_plot = []
  y_plot2 = []
  for i in range(0,len(x)):
    if(i < 3):
      x_plot.append(x[i])
      y_plot.append(y_numerator[i])
      y_plot2.append(y_denominator[i])
    if(i >= 3 & i % 2 == 0):
      x_plot.append(x[i])
      y_plot.append(y_numerator[i])
      y_plot2.append(y_denominator[i])
  
  # Plot the lines and smile :)
  line1 = pl.plot(x_plot,y_plot, 'b', label ="$D(Numerator(B_n))$")
  line2 = pl.plot(x_plot,y_plot2, 'r', label ="$D(Denominator(B_n))$")
  pl.title("Bernoulli Numbers digit length (Not including 0:s)")
  pl.xlabel("n")
  pl.legend(loc="upper left")
  pl.savefig("Bernoulli_numbers.png")

