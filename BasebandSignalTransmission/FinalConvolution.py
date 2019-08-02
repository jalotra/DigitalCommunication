import numpy
import matplotlib.pyplot as plt
import sys

# k = float(sys.argv[1])

#My Modules
import MatchedFilter as MF
import AdditiveGaussianNoise as AGN

impulse_response_matched_filter = MF.MatchedFilterResponse.impulse_response_filter(MF.MatchedFilterResponse(), 1)
impulse_response_vector = impulse_response_matched_filter[1]


SCALING_FACTOR = 1.2
noisy_signal_vector = AGN.add_noise_to_functions(SCALING_FACTOR)[1]

timestamps = impulse_response_matched_filter[0]
# value_to_Add
# for i in range(4001):
# timestamps = 

convolved_vector = numpy.convolve(impulse_response_vector , noisy_signal_vector)
plt.plot(timestamps, convolved_vector)
plt.title('y(t) AFTER GETTING OUT FROM MATCHED FILTER RESPONSE\nDISTORTED WAVE WITH NOISE POWER THAT IS {}00%'.format(300*SCALING_FACTOR))
plt.show()