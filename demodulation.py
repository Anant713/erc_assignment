from scipy.io import wavfile as wavy
import numpy as np 
import matplotlib as plt
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

fs , signal = wavy.read('modulated_noisy_audio.wav')
signal=signal / np.max(np.abs(signal))
frt = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(signal), d=1/fs)

half = len(signal) // 2
frt_halfed = np.abs(frt[:half])
freqs_halfed = freqs[:half]

carrier_index = np.argmax(frt_halfed)
carrier_freq = freqs_halfed[carrier_index]

envelope = np.abs(signal)

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

cutoff = 3000  # cutoff frequency in Hz (depends on your message bandwidth)
message = lowpass_filter(envelope, cutoff=cutoff, fs=fs)



print (carrier_freq)
plt.figure(figsize=(10, 8))
plt.title("FFT Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.plot(freqs_halfed, frt_halfed)
plt.show()

plt.figure(figsize=(10, 8))
plt.plot(message)
plt.title("Demodulated Message Signal")
plt.show()
from scipy.io.wavfile import write

# normalizing to 16-bit int range before saving
message_out = (message / np.max(np.abs(message)) * 32767).astype(np.int16)
write("demodulated_message.wav", fs, message_out)

