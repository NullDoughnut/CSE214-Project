import stdaudio
import math


# 01/04/26: Dillan van Wyk: created the Audio_Manager class and play_tone function
class Audio_Manager:
    def __init__(self):
        self.sample_rate = 44100

    def play_tone(self, frequency, duration=0.2):
        samples = [
            math.sin(2 * math.pi * frequency * i / self.sample_rate)
            for i in range(int(self.sample_rate * duration))
        ]
        stdaudio.playSamples(samples)
