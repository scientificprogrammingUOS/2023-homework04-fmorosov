import numpy as np

# implement the function strange pattern

def strange_pattern(tup):
    n = tup[0] 
    if len(tup) > 1:
        m = tup[1]
    else:
        m = tup[0]
    bool_arr = np.full(shape=(n,m),fill_value=False)
    i = 0
    z = 0
    for x in range(0,n):
        for y in range(0,m,3):
            z = y + i
            if z < m:
               bool_arr[x][z] = True
        i =(i+2)%3

    return bool_arr


if __name__ == "__main__":
    # use this for your own testing!
     print(strange_pattern((10,10)))