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


class GaussianNoise(object):
    def __init__(self, name):
        self.name = name 
        self.pi = numpy.pi

    def gaussian_white_noise(self, number_of_samples,scaling_factor, mean = 0, standard_deviation = 1):
        samples = numpy.random.normal(mean, standard_deviation, size = number_of_samples + 1 )
        return numpy.dot(scaling_factor, samples)
        
    # SAMPLES ARE OF THE TYPE numpy.ndarray
    def print_gaussian_white_noise_samples(self, number_of_samples, scaling_factor, mean = 0, standard_deviation = 1):
        samples = self.gaussian_white_noise(number_of_samples ,scaling_factor)
        print(samples) 

    def sampling_frequency(self, number_of_samples):
        samplingFrequency = (2*self.pi/number_of_samples)
        timeStamps = []
        x = 0
        while(x <= 2*self.pi):
            timeStamps.append(x)
            x += samplingFrequency

        return timeStamps



    def plot_gaussian_white_noise(self, number_of_samples ,scaling_factor):
        plt.plot(self.sampling_frequency(number_of_samples), self.gaussian_white_noise(number_of_samples, scaling_factor))
        plt.title('GAUSSIAN WHITE NOISE WITH STANDARD DEVIATION : 1 AND TIME PERIOD 2pi')
        plt.xlabel('TimePeriod')
        plt.ylabel('Amplitude of Noise')
        plt.xticks([x for x in numpy.arange(0, 2*self.pi +1 , self.pi/4)])
        plt.yticks(numpy.arange(-4*scaling_factor , 4*scaling_factor , 1))
        plt.show()


if __name__ == "__main__":
    def plot():
        WhiteNoiseObject = Noise('GAUSSIAN WHITE NOISE')
        print("#################################################################################")
        print(WhiteNoiseObject.name)
        print()
        number_of_samples = int(input('Total number of samples \n'))
        print("#################################################################################")
        WhiteNoiseObject.plot_gaussian_white_noise(number_of_samples,scaling_factor = 1)
    def print_samples():
        WhiteNoiseObject = Noise('GAUSSIAN WHITE NOISE')
        print("#################################################################################")
        print(WhiteNoiseObject.name)
        print()
        number_of_samples = int(input('Total number of samples \n'))
        print("#################################################################################")
        WhiteNoiseObject.print_gaussian_white_noise_samples(number_of_samples, scaling_factor = 1)
    
    plot()
    #print_samples()


