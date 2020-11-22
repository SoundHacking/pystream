import sounddevice as sd

duration = 5.5  # seconds

cycle = 0

# ~ 1136 samples / 25.8 ms
# outdata[:] = my_data
# outdata[:, 1] = my_channel_data
def callback(indata, outdata, frames, time, status):
    global cycle
    if status:
        print(status)
    outdata[:] = indata
    cycle = cycle + 1
    if(cycle == 100):
        cycle = 0
        print(f"{frames} frames")
        print(f"capture: {time.inputBufferAdcTime}")
        print(f"now: {time.currentTime}")
        print(f"output: {time.outputBufferDacTime}")
        print(f"status: {status}")
        print(indata[0:9])

def connect_default():
    with sd.Stream(channels=2, callback=callback):
        sd.sleep(int(duration * 1000))

def connect_devices(input,output):
    with sd.Stream( device=(input,output),
                    channels=2,
                    callback=callback):
        sd.sleep(int(duration * 1000))

def main():
    print(sd.get_portaudio_version())
    #use cut name for first device 
    # '1 - Acer T272HL (AMD High Defin' instead of '1 - Acer T272HL (AMD High Definition Audio Device)'
    connect_devices(    "Mikrofon (2- USB PnP Sound Devi",
                        "1 - Acer T272HL (AMD High Defin")


main()
