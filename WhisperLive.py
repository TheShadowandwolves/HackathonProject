#!/usr/bin/env python3
import whisper
import os
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write


with open("output.txt","w+"):
    pass
with open("stop.txt","w+") as f:
    f.write("False")

Model = 'small'     # Whisper model size (tiny, base, small, medium, large)
English = True      # Use English-only model?
Translate = False   # Translate non-English to English?
SampleRate = 44100  # Stream device recording frequency
BlockSize = 30      # Block size in milliseconds
Threshold = 0.2    # Minimum volume threshold to activate listening
Vocals = [50, 1000] # Frequency range to detect sounds that could be speech
EndBlocks = 50      # Number of blocks to wait before sending to Whisper


class StreamHandler:
    flag = False
    def __init__(self, assist=None):
        if assist == None:  # If not being run by my assistant, just run as terminal transcriber.
            class fakeAsst(): running, talking, analyze = True, False, None
            self.asst = fakeAsst()  # anyone know a better way to do this?
        else: self.asst = assist
        self.running = True
        self.padding = 0
        self.prevblock = self.buffer = np.zeros((0,1))
        self.fileready = False
        #print("\033[96mLoading Whisper Model..\033[0m", end='', flush=True)
        self.model = whisper.load_model(f'{Model}{".en" if English else ""}')
        #print("\033[90m Done.\033[0m")

    def callback(self, indata, frames, time, status):
        #if status: print(status) # for debugging, prints stream errors.
        if not any(indata):
            #print('\033[31m.\033[0m', end='', flush=True) # if no input, prints red dots
            #print("\033[31mNo input or device is muted.\033[0m") #old way
            #self.running = False  # used to terminate if no input
            return
        # A few alternative methods exist for detecting speech.. #indata.max() > Threshold
        #zero_crossing_rate = np.sum(np.abs(np.diff(np.sign(indata)))) / (2 * indata.shape[0]) # threshold 20
        freq = np.argmax(np.abs(np.fft.rfft(indata[:, 0]))) * SampleRate / frames
        if np.sqrt(np.mean(indata**2)) > Threshold and Vocals[0] <= freq <= Vocals[1] and not self.asst.talking:
            print('.', end='', flush=True)
            if self.padding < 1: self.buffer = self.prevblock.copy()
            self.buffer = np.concatenate((self.buffer, indata))
            self.padding = EndBlocks
        else:
            self.padding -= 1
            if self.padding > 1:
                self.buffer = np.concatenate((self.buffer, indata))
            elif self.padding < 1 < self.buffer.shape[0] > SampleRate: # if enough silence has passed, write to file.
                self.fileready = True
                write('dictate.wav', SampleRate, self.buffer) # I'd rather send data to Whisper directly..
                self.buffer = np.zeros((0,1))
            elif self.padding < 1 < self.buffer.shape[0] < SampleRate: # if recording not long enough, reset buffer.
                self.buffer = np.zeros((0,1))
               # print("\033[2K\033[0G", end='', flush=True)
            else:
                self.prevblock = indata.copy() #np.concatenate((self.prevblock[-int(SampleRate/10):], indata)) # SLOW

    def process(self):
        if self.fileready:
           # print("\n\033[90mTranscribing..\033[0m")
            result = self.model.transcribe('dictate.wav',fp16=False,language='en' if English else '',task='translate' if Translate else 'transcribe')
            text = result["text"]
            with open("output.txt","a+") as f:
                f.write(f"{text}")
            with open("stop.txt","r") as f:
                stop = f.readline()
            if stop == "True":
                raise KeyboardInterrupt
            if self.asst.analyze != None: self.asst.analyze(result['text'])
            self.fileready = False

    def listen(self):
       # print("\033[32mListening.. \033[37m(Ctrl+C to Quit)\033[0m")
        with sd.InputStream(channels=1, callback=self.callback, blocksize=int(SampleRate * BlockSize / 1000), samplerate=SampleRate):
            while self.running and self.asst.running: self.process()

def main():
    try:
        handler = StreamHandler()
        handler.listen()
    except (KeyboardInterrupt, SystemExit): pass
    finally:
       # print("\n\033[93mQuitting..\033[0m")
        if os.path.exists('dictate.wav'): os.remove('dictate.wav')

if __name__ == '__main__':
    main()  # by Nik

