"""
    This class implements different waveforms of single band BaseBand Signals 
    .The objective is to learn how white_noise distorts the data that is present in the message 
    signal . 
     """

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class BasebandWaveforms(object):

    def __init__(self, time_period):
        self.pi = np.pi
        self.time_period = time_period

    def unit_step_function(self, number_of_samples):
        timeStamps = np.arange(-self.time_period, self.time_period, (self.time_period/number_of_samples))
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
    
    def decimal_to_binary(self, decimal_number):
        binary = bin(decimal_number)
        binary = binary[2:]
        binary_list = []
        count = 0
        for binary_info in binary:
            count += 1 
            binary_list.append(int(binary_info))
        return binary_list, count
            
        

    def pulse_function(self, duty_cycle, decimal_number_to_send, number_of_samples):
        binary_list = self.decimal_to_binary(decimal_number_to_send)[0]
        
        
        # Works fine
        timeStamps = []
        for i, _ in enumerate(binary_list):
            starting_time_period = self.time_period * i
            ending_time_period = self.time_period * (i+1)
            timeStamps.append(np.arange(starting_time_period,ending_time_period, (ending_time_period-starting_time_period)/number_of_samples))
        print(np.dot(1,timeStamps).flatten())
        #print(len(np.dot(1, timeStamps).flatten()))
    
    
       #Now I have to create a pulse vector for all values in timeStamps keeping in mind the duty_cycle and also the binary_list_values.
        
        #duty_cycle is the percentage for which I want my pulse wave to be 1 .
        #So for example if the time_period = 2s and duty cycle is 0.5 then for half of the time the wave must be one 
        #and for the remaining half period it should be zero.
        pulse_vector = []
        for i, binary_values in enumerate(binary_list):
            if binary_values == 1:
                x = 0
                while(x < int(len(timeStamps[i])*duty_cycle/100)):
                    pulse_vector.append(1)
                    x += 1
                    
                while(x < int(len(timeStamps[i]))):
                    pulse_vector.append(0)
                    x += 1
            else:
                for _ in timeStamps[i]:
                    pulse_vector.append(-1)
                    
#         print(pulse_vector)
#         print(len(pulse_vector))
    
    
        return np.dot(1,timeStamps).flatten(), pulse_vector


    def plot_unit_step_function(self, number_of_samples):
        x_values , y_values = self.unit_step_function( number_of_samples)
        plt.plot(x_values , y_values)
        plt.title('UNIT STEP FUNCTION ')
        plt.xlabel('< -- TimePeriod -- >')
        plt.ylabel('< -- Amplitude -- >')
        plt.xticks([x for x in np.arange(-self.time_period, self.time_period, self.time_period/10)])
        plt.show()

    def plot_pulse_function(self, duty_cycle, decimal_number_to_send, number_of_samples):
#         x_values , y_values = self.pulse_function(duty_cycle, decimal_number_to_send, number_of_samples)
#         plt.plot(x_values , y_values)
#         plt.title('PULSE FUNCTION ')
#         plt.xlabel('< -- TimePeriod -- >')
#         plt.ylabel('< -- Amplitude -- >')
# #         plt.xticks([x for x in np.arange(0, ending_time, -(starting_time-ending_time)/10)])
#         plt.show()
    
        df = pd.DataFrame(dict(TimeStamps= self.pulse_function(duty_cycle, decimal_number_to_send, number_of_samples)[0],
                              Amplitude = self.pulse_function(duty_cycle, decimal_number_to_send, number_of_samples)[1]))
        g = sns.relplot(x= "TimeStamps", y= "Amplitude", kind="line", data= df)
        plt.grid(color='black', linestyle='-', linewidth=.5)
        plt.title('ORIGINAL SIGNAL THAT HAS TO BE TRANSMITTED REPRESENTING {} IN BINARY'.format(decimal_number_to_send))
        plt.show(g)
       


if __name__ == "__main__":
    Functions = BasebandWaveforms(10)
    # UnitStep.unit_step_function()
    # Functions.plot_unit_step_function(4001) 
#     Functions.plot_unit_step_function(number_of_samples = 100)
    Functions.plot_pulse_function(duty_cycle = 50,decimal_number_to_send = 25, number_of_samples = 1000)
    
