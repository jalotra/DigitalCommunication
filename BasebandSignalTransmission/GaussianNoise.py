'''
    This class contains code to implement the different types of noises that we encounter
    while learning Digital COmmunication.
'''
# Works fine
# Learn why does samples taken from gaussian function consitutes a white_noise.
# Next I HAVE TO IMPLEMENT A WAY TO CALCULATE THE POWER SPECTRAL DENSITY OF THE WHITE_NOISE 
# FROM SAMPLES TAKEN BY THE white_noise function   
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import time


class GaussianNoise(object):
    def __init__(self, standard_deviation, starting_time, ending_time, time_period):
        # For a white gaussian Noise the value of mean is always zero
        self.pi = np.pi
        self.standard_deviation = standard_deviation
        self.starting_time = starting_time
        self.ending_time = ending_time
        self.time_period = time_period


    #  This func makes samples of white gaussian noise in a given timeperiod
    # loc defines mean, scale defines standard deviation
    def gaussian_white_noise(self, number_of_samples, scaling_factor):
        samples = []
        for _ in range (int((self.ending_time - self.starting_time)/self.time_period)):
            samples.append(np.random.normal(loc = 0, scale = self.standard_deviation, size = number_of_samples))
  
        samples = np.append(np.dot(scaling_factor, samples).flatten() ,np.random.normal(loc = 0, scale =                 self.standard_deviation))
        return samples
        
    # SAMPLES ARE OF THE TYPE np.ndarray
    def print_gaussian_white_noise_samples(self, number_of_samples, scaling_factor):
        samples = self.gaussian_white_noise(number_of_samples, scaling_factor)
        print(len(samples))
        print(samples) 
        
    def counter(self, number):
        count = 0
        while number % 10 == 0:
            count += 1
            number /=10
        return count
        

    def sampling_frequency(self, number_of_samples):
        timeStampsIncrements = (self.time_period/number_of_samples)
        timeStamps = []
    
        for i in range(int((self.ending_time-self.starting_time)/self.time_period)):
            x = self.starting_time + self.time_period*i
            while(float(format(x, '.'+'{}'.format(self.counter(number_of_samples))+'f')) < self.starting_time + self.time_period*(i+1)):
                timeStamps.append(float(format(x, '.'+'{}'.format(self.counter(number_of_samples))+'f')))
                x += timeStampsIncrements
        timeStamps.append(self.ending_time)
        return timeStamps

    def seaborn_plot_gaussian(self, number_of_samples, scaling_factor):
        df = pd.DataFrame(dict(TimeStamps = self.sampling_frequency(number_of_samples),
            NoiseAmplitude = self.gaussian_white_noise(number_of_samples, scaling_factor)))
        g = sns.relplot(x= "TimeStamps", y= "NoiseAmplitude", kind="line", data= df)
        plt.grid(color='black', linestyle='-', linewidth=.5)
        plt.show(g)


if __name__ == "__main__":
    NoiseObject = GaussianNoise(standard_deviation = 1 , starting_time = -1000, ending_time = 1000, time_period = 100)
#     print(len(NoiseObject.gaussian_white_noise(number_of_samples = 100,scaling_factor = 1)))
#     print(len(NoiseObject.sampling_frequency(number_of_samples = 100)))
    NoiseObject.seaborn_plot_gaussian(number_of_samples = 100, scaling_factor = 1)



    # def plot():
    #     WhiteNoiseObject = GaussianNoise(1.2, 'GAUSSIAN WHITE NOISE')
    #     print("#################################################################################")
    #     print(WhiteNoiseObject.name)
    #     print()
    #     number_of_samples = int(input('Total number of samples \n'))
    #     print("#################################################################################")
    #     WhiteNoiseObject.plot_gaussian_white_noise(number_of_samples,scaling_factor = 1)
    
    # def print_samples():
    #     WhiteNoiseObject = GaussianNoise (1.2, 'GAUSSIAN WHITE NOISE')
    #     print("#################################################################################")
    #     print(WhiteNoiseObject.name)
    #     print()
    #     number_of_samples = int(input('Total number of samples \n'))
    #     scaling_factor = int(input('Enter the scaling factor to increase or decrease the amplitude of noise '))
    #     print("#################################################################################")
    #     WhiteNoiseObject.print_gaussian_white_noise_samples(number_of_samples, scaling_factor )
    
    # def seaborn_plot():
        
    #     WhiteNoiseObject = GaussianNoise(0.9, 'GAUSSIAN WHITE NOISE')
    #     print("#################################################################################")
    #     print(WhiteNoiseObject.name)
    #     print()
    #     number_of_samples = int(input('Total number of samples \n'))
    #     scaling_factor = int(input('Enter the scaling factor to increase or decrease the amplitude of noise '))
    #     print("#################################################################################")
    #     WhiteNoiseObject.seaborn_plot_gaussian(number_of_samples, scaling_factor)

    # seaborn_plot()

