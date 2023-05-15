import numpy as np 

# implement your function to combine two numpy arrays 

def combination(a,b,axis=0):
   #We assume we are only dealing with 2D-arrays
   if axis not in [0,1]:
       raise TypeError("axis has to be 0 or 1")
   a = a.squeeze()
   b = b.squeeze()
   if(np.ndim(a)<np.ndim(b)):
       raise TypeError("The dimensions of a and b do not match")
   if(np.ndim(a)>np.ndim(b)):
       raise TypeError("The dimensions of a and b do not match")
   print(np.shape(a))
   print(np.shape(b))
   print(len(np.shape(a)))
   c = np.concatenate((a,b),axis)
   return c