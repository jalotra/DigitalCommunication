# This code solves the problem of finding out the fourier transform for the 
# function g(t) = A[u(t) - u(t-T)]

'''By the knowledge of fundamental concepts of 
 fourier transform of unit function and time-shifting property 
 '''
# WE KNOW THAT THE FINAL FOURIER TRANSFORM LOOKS LIKE 
# G(iw) = A(1-exp(-iwT))(pi*delta(w) + 1/jw) 

# IMport Modules
import numpy as np
import math
import matplotlib.pyplot as plt

def delta_function(w):
    if w == 0:
        return 1
    else:
        return 0



def function_definer(A, w, T):
    return np.imag((A*(1-(np.exp(-1j*w*T))*(np.pi*delta_function(w) + (1/1j*w)))))


def fourier_transform(low_frequency_range , high_frequency_range, T):
    pi = np.pi
    low_angular_frequency_range = 2*pi*low_frequency_range
    high_angular_frequency_range = 2*pi*high_frequency_range

    frequency_timestamps = np.linspace(low_angular_frequency_range, high_angular_frequency_range, 10000).flatten()

    y_values = [function_definer(A = 10, w= w, T= T) for w in frequency_timestamps ]

    return (frequency_timestamps, y_values)

def plotter():
    plt.plot(fourier_transform(-10e+8,10e+8, 1)[0], fourier_transform(-10e+8, 10e+8, 1)[1])
    plt.grid()
    plt.show()



if __name__ == "__main__":
    # print(fourier_transform(-100, 100, 1))
    plotter()







