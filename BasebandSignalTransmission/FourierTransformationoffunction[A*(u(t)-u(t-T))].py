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



def imag_part_function_definer(A, w, T):
    return np.imag((A*(1-(np.exp(-1j*w*T))*(np.pi*delta_function(w) + (1/(1j*w))))))

def real_part_function_definer(A, w, T):
    return np.real((A*(1-(np.exp(-1j*w*T))*(np.pi*delta_function(w) + (1/(1j*w))))))


def imag_fourier_transform(low_frequency_range , high_frequency_range, T):
    pi = np.pi
    low_angular_frequency_range = 2*pi*low_frequency_range
    high_angular_frequency_range = 2*pi*high_frequency_range

    frequency_timestamps = np.linspace(low_angular_frequency_range, high_angular_frequency_range, 10000).flatten()

    y_values = [imag_part_function_definer(A = 10, w= w, T= T) for w in frequency_timestamps ]

    return (frequency_timestamps, y_values)

def real_fourier_transform(low_frequency_range , high_frequency_range, T):
    pi = np.pi
    low_angular_frequency_range = 2*pi*low_frequency_range
    high_angular_frequency_range = 2*pi*high_frequency_range

    frequency_timestamps = np.linspace(low_angular_frequency_range, high_angular_frequency_range, 10000).flatten()

    y_values = [real_part_function_definer(A = 10, w= w, T= T) for w in frequency_timestamps ]

    return (frequency_timestamps, y_values)

def imag_plotter():
    plt.plot(imag_fourier_transform(-10e+8,10e+8, 1)[0], imag_fourier_transform(-10e+8, 10e+8, 1)[1])
    plt.grid()
    plt.xlabel('VALUES OF FREQUENCY')
    plt.ylabel('IMAGINARY PART')


def real_plotter():
    plt.plot(real_fourier_transform(-10e+8,10e+8, 1)[0], real_fourier_transform(-10e+8, 10e+8, 1)[1])
    plt.grid()
    plt.xlabel('VALUES OF FREQUENCY')
    plt.ylabel('REAL PART')
    
    

if __name__ == "__main__":
   # Plotting both the real and imaginary parts with sub-plots on the same plot
    

    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(imag_fourier_transform(-10e+8,10e+8, 1)[0], imag_fourier_transform(-10e+8, 10e+8, 10e+3)[1])
    ax1.set_xlabel('VALUES OF FREQUENCY')
    ax1.set_ylabel('IMAGINARY PART')
    ax1.grid()

    ax2.plot(real_fourier_transform(-10e+8,10e+8, 1)[0], real_fourier_transform(-10e+8, 10e+8, 10e+3)[1])
    ax2.set_xlabel('VALUES OF FREQUENCY')
    ax2.set_ylabel('REAL PART')
    ax2.grid()
    
    plt.show()

    







