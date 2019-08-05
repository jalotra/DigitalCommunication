import numpy 
import matplotlib.pyplot as plt
import sys

# What I have to do
# To take in values from the AdditiveGaussianNoise script and also from MatchedFilterResponse
# Next is to convolve both the vectors and to plot the covolved vector with timeStamps

from AdditiveGaussianNoise import add_noise_to_functions
from MatchedFilter import MatchedFilterResponse 
import BasebandWaveforms as BW

class ConvolvedVector(object):

    def __init__(self, author):
        self.author = author

    def getting_noisy_bandpass_signal(self, scaling_factor, decimal_number_to_send, time_period, standard_deviation, 
    number_of_samples, duty_cycle, starting_time, ending_time):

        noise_x_values, noise_y_values = add_noise_to_functions(scaling_factor, decimal_number_to_send, time_period, 
        standard_deviation, number_of_samples, duty_cycle, starting_time, ending_time)

        return noise_x_values, noise_y_values

    def getting_matched_filter_response(self, K, duty_cycle, decimal_number_to_send, number_of_samples, time_period):
        filter_x_values, filter_y_values = MatchedFilterResponse(time_period = time_period).impulse_response(K, duty_cycle, decimal_number_to_send, number_of_samples)

        return filter_x_values, filter_y_values

    def convolving_noise_and_filter_response(self, first_vector, second_vector):
        convolved_vector = numpy.convolve(first_vector, second_vector)
        return convolved_vector


if __name__ == "__main__":
    OBJ = ConvolvedVector('Shivam Jalotra')
    time_period = 10
    decimal_number = 2
    duty_cycle = 100
    count = BW.BasebandWaveforms.decimal_to_binary(BW.BasebandWaveforms(time_period = time_period),decimal_number = decimal_number)[1]

    noise_x_values, noise_y_values = OBJ.getting_noisy_bandpass_signal(scaling_factor = 1, decimal_number_to_send = decimal_number, time_period = time_period , standard_deviation = 5, 
    number_of_samples = 200, duty_cycle = duty_cycle, starting_time = 0 , ending_time = count*time_period )

    filter_x_values, filter_y_values = OBJ.getting_matched_filter_response(K = 1, duty_cycle = duty_cycle, decimal_number_to_send = decimal_number, number_of_samples = 200, time_period = 10)

    convolvedVector = OBJ.convolving_noise_and_filter_response(noise_y_values, filter_y_values)

    step_size = noise_x_values[1] - noise_x_values[0]
    noise_time_values = numpy.arange(0, count*time_period, step_size/2)
    noise_time_values = noise_time_values[:-1]
    

    print(len(convolvedVector))
    print(len(noise_time_values))
    plt.plot(noise_time_values, convolvedVector)
    plt.grid(color='black', linestyle='-', linewidth=.5)
    plt.show()
    

    # print('{} \n {} \n {} \n {}\n'.format(len(noise_x_values), len(noise_y_values), len(filter_x_values), len(filter_y_values)))