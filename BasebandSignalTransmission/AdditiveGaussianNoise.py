import numpy
import matplotlib.pyplot as plt 
import sys

#My Modules
import BasebandWaveforms as BW
import GaussianNoise as GN

scaling_factor = 2

def add_noise_to_functions():
    x_unit_step_vector, y_unit_step_vector = BW.BasebandWaveforms.pulse_function(BW.BasebandWaveforms(), 4001)
    y_noise_vector = GN.GaussianNoise.gaussian_white_noise(GN.GaussianNoise('Gaussian White Noise'), number_of_samples = 1000, scaling_factor = scaling_factor)

    resultant_waveform_y_values = numpy.add(y_unit_step_vector, y_noise_vector)

    return (x_unit_step_vector, resultant_waveform_y_values)


def plotting_the_distorted_wave():
    x_timestamps, y_values  = add_noise_to_functions()
    plt.plot(x_timestamps, y_values)
    plt.title('DISTORTED WAVE WITH POWER THAT IS {}00%'.format(300*scaling_factor))
    plt.xlabel('TimePeriod')
    plt.ylabel('Amplitude of the Distorted Wave')
    plt.show()

if __name__ == "__main__":
    plotting_the_distorted_wave()
