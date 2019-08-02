# Digital Communication

This repository is basically the whole implementation of Simon Haykin and our course that we have to study in 5th Semester and it goes by the name Digital Communication. The Course can be found here : 

## Getting Started

Many of the electronics and communication students lack the power to replicate what is written in brilliant Books like Simon Haykin, thus we lack the required problem solving skills needed. And we get stuck if somebody asks us the change on output waveform as one changes some input parameters.
If you are a electronics and communication student ask yourself **Did you apply the theory that you learnt in books like Simon Hayin, Populis For Random Variables etc**. 

This project enables me to think of an algorithm, improve my technical skills, writing good pythonic code and finally learning scientific libraries.

### Prerequisites

1. Python is a pre-requisite and some knowledge of linear algebra.
2. Google and StackOverflow is the key ; at any point you have any difficulty in pointing out what a       particular numpy method does Search it.

### Installing
1. git clone https://github.com/jalotra/DigitalCommunication
2. cd DigitalCommunication
3. python3 -m venv venv
4. source venv/bin/activate 
4. pip install -r requirements.txt


### Folder Description:
**BaseBandSignalTransmission contains :**

 1. GaussianNoise.py -- Contains class that implements a gaussian white noise and returns its samples       or plots its time-response.

 2. BasebandWaveforms.py -- Contains class that right now implements UnitStep Function and a pulse function , Sine and Cosine waves of particular frequency has to implemented.

 3. AdditiveGaussianNoise.py -- Contains methods that add the Gaussian White Noise to a Baseband Signal.

 4. MatchedFilter.py -- Contains class that implements a matched filter response if g(t) is the input waveform the matchedFilter impulse response is K*g(T-t). See Docs for more details.

 5. FinalConvolution.py -- Contains class that convolves the input - noisyBaseBand waveform with that of the Matchedfilter response and plots the output. 
  
 6. docs -- HAS THEORY RELATED TO MATCHED FILTER RESPONSE AND WHY TO USE IT.
 

## Running the tests

Nothing written till now.


## Contributing
If you would like to add a particular function or filter you can make a pr.
NOT WRITTEN FULLY.





## Authors

* **Shivam Jalotra** - (https://shivamjalotra.me)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Rajoo Pandey Sir for teaching so fabulously in the class.
* Simon Haykin for  writing a wonderful Book.
* Jasmeet Singh Sobti for scribling whatever was taught in class on paper. 