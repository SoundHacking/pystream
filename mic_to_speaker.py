import sounddevice as sd

duration = 5.5  # seconds

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata

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
