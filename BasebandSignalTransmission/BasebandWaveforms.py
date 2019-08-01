"""
    This class implements different waveforms of single band BaseBand Signals 
    .The objective is to learn how white_noise distorts the data that is present in the message 
    signal . 
     """

import numpy
import matplotlib.pyplot as plt

class BasebandWaveforms(object):

    def __init__(self):
        self.pi = numpy.pi

    def unit_step_function(self, number_of_samples):
        timeStamps = numpy.arange(-4*self.pi, 4*self.pi, 8*self.pi/number_of_samples)
        # print(timeStamps)
        # print(len(timeStamps))
        unit_step_vector = []

        for value in timeStamps:
            if value > 0 :
                unit_step_vector.append(1)
            elif value == 0 : 
                unit_step_vector.append(0.5)
            else:
                unit_step_vector.append(0)

        # print(unit_step_vector)
        # print(len(unit_step_vector))
        return timeStamps, unit_step_vector

    def pulse_function(self, number_of_samples):
        timeStamps = numpy.arange(-4*self.pi, 4*self.pi, 8*self.pi/number_of_samples)
        # print(timeStamps)
        # print(len(timeStamps))
        pulse_vector = []

        for value in timeStamps:
            if value > 0 :
                pulse_vector.append(1)
            elif value == 0 : 
                pulse_vector.append(0.5)
            else:
                pulse_vector.append(-1)

        # print(unit_step_vector)
        # print(len(unit_step_vector))
        return timeStamps, pulse_vector

    

    def plot_unit_step_function(self, number_of_samples):
        x_values , y_values = self.unit_step_function(number_of_samples)
        plt.plot(x_values , y_values)
        plt.title('UNIT STEP FUNCTION ')
        plt.xlabel('< -- TimePeriod -- >')
        plt.ylabel('< -- Amplitude -- >')
        plt.xticks([x for x in numpy.arange(-4*self.pi, 4*self.pi +1 , self.pi/2)])
        plt.show()

    def plot_pulse_function(self, number_of_samples):
        x_values , y_values = self.pulse_function(number_of_samples)
        plt.plot(x_values , y_values)
        plt.title('PULSE FUNCTION ')
        plt.xlabel('< -- TimePeriod -- >')
        plt.ylabel('< -- Amplitude -- >')
        plt.xticks([x for x in numpy.arange(-4*self.pi, 4*self.pi +1 , self.pi/2)])
        plt.show()
       


if __name__ == "__main__":
    Functions = BasebandWaveforms()
    # UnitStep.unit_step_function()
    # Functions.plot_unit_step_function(4001) 
    Functions.plot_pulse_function(4001)
    
