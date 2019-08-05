import numpy as np
import matplotlib.pyplot as plt
import pandas
import seaborn as sns
import pandas as pd


import BasebandWaveforms as BW 

''' This class represents the matched filter response only for a pulse wave'''
class MatchedFilterResponse(object):
    def __init__(self, time_period):
        self.time_period = time_period
    
    # Impulse response of a matched can be represnented as K*g(T-t)
    def impulse_response(self, K, duty_cycle, decimal_number_to_send, number_of_samples):
        timeStamps_pulse_vector, value_pulse_vector = BW.BasebandWaveforms.pulse_function(BW.BasebandWaveforms(self.time_period),
         duty_cycle, decimal_number_to_send, number_of_samples)

        # To return a vector that represents a matched filter response 
        # I have to mutiply each timeStamp with -1
        # Then add self.time_period to each timeStamp 
        # Job will be done

        # print(type(timeStamps_pulse_vector))
        timeStampsVector = []
        for elements in timeStamps_pulse_vector:
            elements *= -1  
            elements +=  self.time_period
            timeStampsVector =  np.append(timeStampsVector, elements)
            
           
        # print(len(timeStamps_pulse_vector))
        # print(len(timeStampsVector))
        return timeStampsVector, np.dot(value_pulse_vector, K)
    
    def plot_matched_filter_response(self, K, duty_cycle, decimal_number_to_send, number_of_samples):
        df = pd.DataFrame(dict(TimeStamps= self.impulse_response(K, duty_cycle, decimal_number_to_send, number_of_samples)[0],
                              Amplitude = self.impulse_response(K, duty_cycle, decimal_number_to_send, number_of_samples)[1]))
        g = sns.relplot(x= "TimeStamps", y= "Amplitude", kind="line", data= df)
        df.head()
        plt.grid(color='black', linestyle='-', linewidth=.5)
        plt.title('ORIGINAL SIGNAL THAT HAS TO BE TRANSMITTED REPRESENTING {} IN BINARY'.format(decimal_number_to_send))
        plt.show()
       


    


if __name__ == "__main__":
    OBJ = MatchedFilterResponse(10)
    # OBJ.plotting_signal_to_process()
    OBJ.plot_matched_filter_response(K = 3, duty_cycle = 50, decimal_number_to_send = 50, number_of_samples = 500)
    # OBJ.plotting_signal_to_process()
    