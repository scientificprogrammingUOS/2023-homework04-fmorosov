import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    if lower_bound >= upper_bound:
        raise TypeError("lower_bound has to be smaller than upper_bound!")
    x = locals()
    for val in x:
        if not isinstance(x[val],(int,float)):
            raise TypeError("Please only enter integers or floats")
    x = np.random.normal(loc=0.0, scale=1.0, size=1000)
    x = x[x>lower_bound]
    x = x[x<upper_bound]
    mean = np.mean(x)
    std = np.std(x)
    print(x)
    print()
    return (mean,std) 


if __name__ == "__main__":
    print(gaussian_analysis(0,1,-1,1)) 
