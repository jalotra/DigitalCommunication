import numpy
import matplotlib.pyplot as plt 
import sys

#My Modules
import BasebandWaveforms as BW
import GaussianNoise as GN

# scaling_factor = 2

def add_noise_to_functions(scaling_factor, decimal_number_to_send, time_period, standard_deviation, number_of_samples, duty_cycle, starting_time, ending_time):
    timeStamps_pulse_vector, value_pulse_vector = BW.BasebandWaveforms.pulse_function(BW.BasebandWaveforms(time_period), duty_cycle, decimal_number_to_send, number_of_samples)
    y_noise_vector = GN.GaussianNoise.gaussian_white_noise(GN.GaussianNoise(standard_deviation, starting_time, ending_time, time_period) ,
    number_of_samples, scaling_factor)[0]

    resultant_waveform_y_values = numpy.add(value_pulse_vector, y_noise_vector)

    return (timeStamps_pulse_vector, resultant_waveform_y_values)


def plotting_the_distorted_wave(scaling_factor, decimal_number_to_send, time_period, standard_deviation, number_of_samples, duty_cycle, starting_time, ending_time):
    x_timestamps, y_values  = add_noise_to_functions(scaling_factor, decimal_number_to_send, time_period, 
    standard_deviation, number_of_samples, duty_cycle, starting_time, ending_time)
    plt.plot(x_timestamps, y_values)
    plt.title('DISTORTED WAVE WITH NOISE AMPLITUDE THAT IS {}% OF THE BASEBAND SIGNAL'.format(standard_deviation*100))
    plt.xlabel('TimePeriod')
    plt.ylabel('Amplitude of the Distorted Wave')
    plt.grid(color='black', linestyle='-', linewidth=.5)
    plt.show()

if __name__ == "__main__":

    time_period = 10
    decimal_number = 16
    count = BW.BasebandWaveforms.decimal_to_binary(BW.BasebandWaveforms(time_period = time_period),decimal_number = decimal_number)[1]
#     print(count*time_period)
    plotting_the_distorted_wave(scaling_factor = 1, decimal_number_to_send = decimal_number, time_period = time_period , standard_deviation = 0.01, 
    number_of_samples = 200, duty_cycle = 50, starting_time = 0 , ending_time = count*time_period )
    

