#!/usr/bin/env python3
"""Play a sine signal."""
import numpy as np
import sounddevice as sd

start_idx = 0

device_name = "1 - Acer T272HL (AMD High Defin"

samplerate = sd.query_devices(device_name, 'output')['default_samplerate']
amplitude = 0.1
frequency = 500

def callback(outdata, frames, time, status):
    if status:
        print(f"Error : {status}")
    global start_idx
    t = (start_idx + np.arange(frames)) / samplerate
    t = t.reshape(-1, 1)
    outdata[:] = amplitude * np.sin(2 * np.pi * frequency * t)
    start_idx += frames

with sd.OutputStream(device=device_name, channels=1, callback=callback,
                        samplerate=samplerate):
    print('press Return to quit')
    input()
