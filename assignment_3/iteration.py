bounded = []
diverges = []
iterations = []

def iteration(c,z0):
    """ Preforms iteration of function z_n = z_n**2 + c such that c is a complex number.
    
    Iteration is preformed on complex number than assessed if the its absolute length converges within /
    10 iterations or diverges. Results of each nature are added to arrays.
    Parameters
    ----------
    c : numpy.complex128
        Represents a number in the compelex domain of the form c = x +iy.
    
    z0 : float
        Inital estimate of the iteration.
    
    Returns
    -------
    
    """
    z_n = z0
    for n in range(0,100):
        z_n = z_n**2 + c 
    
        if abs(z_n) <= 2:
            bounded.append(c)
        
        if abs(z_n) > 2:
            diverges.append(c)
            iterations.append(n)
    return bounded, diverges, iterations
