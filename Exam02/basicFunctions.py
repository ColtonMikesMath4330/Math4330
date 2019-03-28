def twoNorm(vector):
  '''Calculates and returns the 2-norm of a given vector.
	
  Iterates over the elements of a given vector, adding the squares of 
  their absolute values, returning the square root of this sum.
	
  Args:
	vector: A list of complex and real valued numbers
  Returns:
	A non-negative real valued scalar which is the 2-norm of the given vector.
  '''
  result = 0
  for element in range(len(vector)):
	result = result + (vector[element].real)**2 + (vector[element].imag)**2
  result = result**(1/2)
  return result
 
 
 def scalarVectorMulti(scalar,vector):
   '''
   '''
   #Initializing result
   result = [0]*len(vector)
   #Overwrite the elements of result using scalar multiplication
   for element in range(len(result)):
     result[element] = scalar*vector[element]
   return result

   
 def normalize(vector):
   '''
   '''
   #Calculate twoNorm of a vector.
   norm = twoNorm(vector) 
   #If the vector is non-zero, normalize it.
   if (norm != 0):
     return scalarVectorMulti((1/norm),vector)
   #If the vector is zero, print "Invalid Input."
   else:
     print("Invalid input")
  
 def vectorAddition(vector_1,vector_2):
	'''
	'''
	#initialize result
    result = [0]*len(vector_1)
	for element in range(len(result)):
	  #overwrite the elements of result with our desired addition
	  result[element] = vector_1[element] + vector_2[element]
	return result
	

def complexConjugate(scalar):
	'''
	'''
	result = 0
	result = result + scalar.real
	result = result - (scalar.imag)*1j
	return result
	
def conjugateVector(vector):
	'''
	'''
	result = [0]*len(vector)
	for element in range(len(vector)):
      result[element] = complexConjugate(vector[element])
	return vector
	