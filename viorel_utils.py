import numpy as np 

def see(*args, **kwargs):
  """Shorthand for print() to see stuff faster"""
  print(*args, **kwargs)

def sigmoid(z):
  """
  Compute the sigmoid of z
  Parameters
  ----------
  z : array_like
      A scalar or numpy array of any size.
  Returns
  -------
    g : array_like
        sigmoid(z)
  """
  z = np.clip( z, -500, 500 )           # protect against overflow
  g = 1.0/(1.0+np.exp(-z))
  
  return g