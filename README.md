# fourier-analysis
Fourier analysis for photoresistor data

This application was created to analyse a light captured by photoresistor. In here you have a simple Arduino code, that takes the analg signal and converts it into the digital one. 

# How it works? 
Firstly, you have to create a circuit, which is just a voltage divider (second resistor depends on your photoresistor resistance). Next you send the data through COM port and receive it through RealTerm. I guess you can capture it even through Python.

Then the Python script analyzes the file you want, which name you have to manually type inside the code. The sampling frequency is tricky, beacuse you have to calculate somehow how fast your PC works. From my experience, each computer had its own sampling rate, so on my personal PC it was about 4.3 kHz, but at the univeristy it was only 3.3 kHz. 

The script plots your data, so for example, the lamp sample shows us almost perfect 50 Hz signal (and its harmonics). Generally, you can process any signal that way, as long as signal has been "translated" into numerical values. 

# Watch out!
In Spyder you can see two graphs simultaneously, time and frequency. In PyCharm however the frequency graphs appears after you close the time graph.
