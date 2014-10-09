import sys
import math
import unittest
# precisao #
epsilon = 0.0001

class mathPyTest(unittest.TestCase):
   # Testes para senos primeiro usarmos alguns valores
   #essencias para funcao seno 
   def test_sen(self):
      self.assertGreaterEqual(epsilon,math.fabs( 1 - math.sin(3.14159265359 / 2)))
      self.assertGreaterEqual(epsilon,math.fabs( 0 - math.sin(3.14159265359)))
      self.assertGreaterEqual(epsilon,math.fabs( (-1) - math.sin(3.14159265359 * (3 / 2))))
   # Testes para factorial primeiro alguns valores
   #essencias para funcao factorial    
   def test_factorial(self):
      self.assertEqual(math.factorial(0),1)
      self.assertEqual(math.factorial(1),1)
   # Testes para log2 usando alguns valores
   #essencias para funcao log2
   def test_log2(self):
      self.assertGreaterEqual(epsilon, math.fabs(0 - math.log(1,2)))
      self.assertGreaterEqual(epsilon, math.fabs(1 - math.log(2,2)))     
         

if __name__ == '__main__':
    unittest.main()

def sen(x):
   sin = 0
   for i in range(0, 11):
      aux1 = math.pow(-1,i)
      aux2 = math.pow(x,2*i + 1)
      aux3 = math.factorial(2*i + 1)
      sin = sin + (aux1 * aux2) / aux3
   return sin

def factorial(n):
   c = 1
   for i in range(1, n + 1) :
      c = c * i
   return c

def log2(n):
   return math.log(n) / math.log(2)       