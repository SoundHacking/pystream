from scipy.io.wavfile import read
import sounddevice as sd
import numpy

def print_devices():
    devices = sd.query_devices()
    for device in devices:
        print(device["name"])

def main():
    audio = read("piano2.wav")
    sampling_frequency = audio[0]
    audio_array = numpy.array(audio[1])


    #Play on a specific device - add this line
    sd.default.device = "1 - Acer T272HL (AMD High Defin"

    sd.play(audio_array,sampling_frequency)
    sd.wait()


main()
