import numpy as np
import sounddevice as sd
import soundfile as sf
import sys
import queue

listen = True
record = True

duration = 5.5  # seconds
start_idx = 0
cycle = 0

q = queue.Queue()

device_name = "1 - Acer T272HL (AMD High Defin"

device = sd.query_devices(device_name, 'output')
samplerate = int(device['default_samplerate'])
channels = device['max_output_channels']
amplitude = 0.06
frequency = 500

# ~ 1136 samples / 25.8 ms
# outdata[:] = my_data
# outdata[:, 1] = my_channel_data
def callback(outdata, frames, time, status):
    global cycle
    if status:
        print(f"Error : {status}")
    global start_idx
    t = (start_idx + np.arange(frames)) / samplerate
    t = t.reshape(-1, 1)
    outdata[:] = amplitude * np.sin(2 * np.pi * frequency * t)
    if(record):
        q.put(outdata.copy())
    if(not listen):
        outdata.fill(0)
    start_idx += frames
    cycle = cycle + 1
    if(cycle == 100):
        cycle = 0
        print(f"{frames} frames")
        print(f"capture: {time.inputBufferAdcTime}")
        print(f"now: {time.currentTime}")
        print(f"output: {time.outputBufferDacTime}")
        print(f"status: {status}")
        print(outdata[0:1])
        print(f"q.size: {q.qsize()}")


def play_record():
    with sf.SoundFile("record.wav", mode='x', samplerate=samplerate,
                      channels=channels, subtype="PCM_24") as file:
        with sd.OutputStream(device=device_name, channels=channels, callback=callback,
                                samplerate=samplerate):
            while True:
                file.write(q.get())

def play_only():
    with sd.OutputStream(device=device_name, channels=channels, callback=callback,
                            samplerate=samplerate):
        print("press return to quit")
        input()

if(record):
    play_record()
else:
    play_only()

