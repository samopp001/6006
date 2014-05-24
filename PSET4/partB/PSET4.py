from decimal import Decimal
import math

# Returns the next guess after one iteration of Newton's method.
#
# Arguments:
#  - number: The number whose cube root is to be calculated.
#  - guess: The current guess of the cube root.
def CubeRootNewtonIteration(number, guess):
  assert type(number) == int

  # BEGIN STUDENT CODE
  square = guess * guess
  cube = guess * guess * guess
  return guess - ((cube - number)/(3.0 *square))
  # END STUDENT CODE


# Returns an integer guess for the cube root of the number.
#
# Arguments:
# - number: The number whose cube root is to be calculated.
def CubeRootGuess(number):
  assert type(number) == int

  # BEGIN STUDENT CODE
  return int(math.pow(number,1/3.0))
  # END STUDENT CODE


# Returns the best floating-point approximation to the cube root of the number.
#
# Arguments:
# - number: The number whose cube root is to be calculated.
def FloatCubeRoot(number):
  assert type(number) == int

  # BEGIN STUDENT CODE
  return math.pow(number,1/3.0)
  # END STUDENT CODE


# Returns a guess of the reciprocal of the given decimal number.
#
# Arguments:
# - number: The decimal number whose reciprocal is to be guessed.
def ReciprocalGuess(number):
  assert type(number) == Decimal

  # BEGIN STUDENT CODE
  exponent = (-1) * number.shorten(1).exponent - 1
  numTest = number.shorten(1).significand
  if numTest == 0:
    return Decimal(long(0),1,number.precision)
  reciprocal = 10L / numTest
  return Decimal(reciprocal,exponent,number.precision)
  # END STUDENT CODE


# Returns the reciprocal of the give decimal number, computed to the same
# precision as number itself (i.e., number.precision).
#
# Arguments:
# - number: The decimal number whose reciprocal is to be computed.
def DecimalReciprocal(number):
  assert type(number) == Decimal

  # BEGIN STUDENT CODE
  guess = ReciprocalGuess(number)
  for i in range(10):
    guess = guess * (2 - guess * number)
  return guess
  # END STUDENT CODE


# Returns the best approximation to the cube root of the number using decimal
# numbers with the given number of digits of precision.
#
# Arguments:
# - number: The number whose cube root is to be calculated.
# - precision: The number of digits of precision to use.
def DecimalCubeRoot(number, precision):
  assert type(number) == int
  assert type(precision) == int

  # Note: You will need to pass reciprocal=DecimalReciprocal when creating
  #       Decimal numbers with support for division.

  # BEGIN STUDENT CODE
  guess0 = CubeRootGuess(number)
  state0 = Decimal(guess0,precision=precision, reciprocal=guess0)
  state1 = Decimal(number,precision=precision, reciprocal=guess0)
  state3 = Decimal(3,precision=precision, reciprocal=guess0)
  for i in range(15):
    square = state0 ** 2
    cube = square * state0
    state0 = state0 - ((cube - state1) * DecimalReciprocal((square*state3)))
  return state0
  # END STUDENT CODE
