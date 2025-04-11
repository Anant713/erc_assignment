![image](https://github.com/user-attachments/assets/487e9f0b-725e-4f48-aa3d-45da0d44e487)
Fast fourier transform graph
![image](https://github.com/user-attachments/assets/188df3a7-d925-42b4-b56b-5be385963c75)
Fast fourier transform magnitude graph (halved)
![Screenshot 2025-04-11 152940](https://github.com/user-attachments/assets/b1fef1db-c4f8-41e1-8639-b940193cd50c)
Demodulated message graph
##Carrier frequency obtained = 10582.307314454129 Hz

## Libraries used --> matplotlib, scipy , numpy
# explaination of the code in blocks -->
- fs , signal = wavy.read('modulated_noisy_audio.wav')
- signal = signal / np.max(np.abs(signal))
### fs = sampling rate ( Depend on how/on which device the audio was recorded)
### signal = array of amplitudes of the waveform
- frt = np.fft.fft(signal)
- freqs = np.fft.fftfreq(len(signal), d=1/fs)
### frt = fourier transform of the signal
### freqs = corresponding frequencies
- half = len(signal) // 2
- frt_halfed = np.abs(frt[:half])
- freqs_halfed = freqs[:half]
### len(signal) = number of amplitude values(no. of smples) in the signal
### As the fourier transform of a real function is symmetric abot y=0, so we can take any one half to reduce calculation. Thus, I have take the positive half.
- carrier_index = np.argmax(frt_halfed)
- carrier_freq = freqs_halfed[carrier_index]
### The frequency for whicch the FFT has a peak is the carrier frequency. Reasion --> It is the frequency which controbutes the maximum to the wave. 
- envelope = np.abs(signal)
### Determines the envelope
-    def butter_lowpass(cutoff, fs, order=5):
-      nyq = 0.5 * fs   
## Nyquist frequency = sampling freq/2
-     normal_cutoff = cutoff 
## nyq  // normalising the cutoff freq
-      b, a = butter(order, normal_cutoff, btype='low', analog=False) 
-      return b, a
## btype=low => low  pas filter , order =5 ==> Higher order would give a sharper change, normal_cutoff = the cutoff freq(normalised)
  
- def lowpass_filter(data, cutoff, fs, order=5):
-     b, a = butter_lowpass(cutoff, fs, order=order)
-     y = filtfilt(b, a, data) 
-     return y

- cutoff = 3000  # cutoff frequency in Hz (depends on your message bandwidth, human voice is <=3000Hz mostly)
- message = lowpass_filter(envelope, cutoff=cutoff, fs=fs)
  








