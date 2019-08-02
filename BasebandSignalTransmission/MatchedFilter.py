import numpy 
import matplotlib.pyplot as plt


import BasebandWaveforms as BW 

class MatchedFilterResponse(object):
    def __init__(self):
        self.pi = numpy.pi
        self.time_period = 2*self.pi

    def signal_to_process(self, number_of_samples):
        timeStamps = numpy.arange(0, self.time_period, (self.time_period/(2*number_of_samples)))
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
        unit_step_vector[-1] = 0 
        unit_step_vector[0] = 0
        # print(unit_step_vector)
        # print(len(unit_step_vector))
        return (timeStamps, unit_step_vector)       

    def plotting_signal_to_process(self):
        x_values , y_values = self.signal_to_process(4001)
        plt.plot(x_values , y_values)
        plt.title('g(t) ')
        plt.xlabel('< -- TimePeriod -- >')
        plt.ylabel('< -- Amplitude -- >')
        plt.xticks([x for x in numpy.arange(0, self.time_period +1 , self.pi/2)])
        plt.show()


    def impulse_response_filter(self, K):
    # By theory h(t) = Kg(T-t) where T is the sampling Time Period
    # If the function looks something like this u(t) - u(T-t) which is only a single pulse
    # h(t) = Kg(t) Can be seen by plotting the graph
    
        if( -8*self.pi <= self.time_period <=  8*self.pi ):
            y_vector = numpy.dot(K, self.signal_to_process(2001)[1])

        return (self.signal_to_process(4001)[0] , y_vector)

    def plotting_impulse_response_filter(self, K):
        x_values , y_values = self.impulse_response_filter(K)
        plt.plot(x_values , y_values)
        plt.title('h(t) ')
        plt.xlabel('< -- TimePeriod -- >')
        plt.ylabel('< -- Amplitude -- >')
        plt.xticks([x for x in numpy.arange(0, self.time_period +1 , self.pi/2)])
        plt.show()


if __name__ == "__main__":
    OBJ = MatchedFilterResponse()
    # OBJ.plotting_signal_to_process()
    OBJ.plotting_impulse_response_filter(3.5)
    # OBJ.plotting_signal_to_process()
    