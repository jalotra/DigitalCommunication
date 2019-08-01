'''
    This class contains code to implement the different types of noises that we encounter
    while learning Digital COmmunication.
'''
# Works fine
# Learn why does samples taken from gaussian function consitutes a white_noise.
# Next I HAVE TO IMPLEMENT A WAY TO CALCULATE THE POWER SPECTRAL DENSITY OF THE WHITE_NOISE 
# FROM SAMPLES TAKEN BY THE white_noise function   
import numpy
import matplotlib.pyplot as plt


class Noise(object):
    def __init__(self, name):
        self.name = name 

    def white_noise(self, mean, standard_deviation, number_of_samples):
        samples = numpy.random.normal(mean, standard_deviation, size = number_of_samples )
        return samples
        
    # SAMPLES ARE OF THE TYPE numpy.ndarray
    def print_white_noise_samples(self, mean, standard_deviation, number_of_samples):
        samples = self.white_noise(mean, standard_deviation, number_of_samples)
        print(samples) 

    def plot_white_noise(self, mean, standard_deviation, number_of_samples):
        plt.plot(self.white_noise(mean, standard_deviation, number_of_samples))
        plt.show()


if __name__ == "__main__":
    def plot():
        WhiteNoiseObject = Noise('white_noise_describer')
        print(WhiteNoiseObject.name)
        mean = int(input('Input the mean '))
        std = int(input('Input the standard deviation'))
        number_of_samples = int(input('Total number of samples'))
        WhiteNoiseObject.plot_white_noise(mean, std, number_of_samples)
    def print_samples():
        WhiteNoiseObject = Noise('white_noise_decriber')
        print(WhiteNoiseObject.name)
        mean = int(input('Input the mean '))
        std = int(input('Input the standard deviation'))
        number_of_samples = int(input('Total number of samples'))
        WhiteNoiseObject.print_white_noise_samples(mean, std, number_of_samples)
    
    #plot()
    print_samples()