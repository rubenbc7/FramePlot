import wave
import numpy as np
import matplotlib.pyplot as plt

steve = wave.open('steve.wav', 'r')
slime = wave.open('slime.wav', 'r')


framesGM = steve.readframes(-1)
framesAN = slime.readframes(-1)
ondaconvertidaGM = np.frombuffer(framesGM, dtype='int16')
ondaconvertidaAN = np.frombuffer(framesAN, dtype='int16')

#print(frames[:10])

framerate_gm = steve.getframerate()
print (framerate_gm)
time_gm = np.linspace(start=0, stop=len(ondaconvertidaGM)/framerate_gm, num=len(ondaconvertidaGM))
print(time_gm[:10])

framerate_AN = slime.getframerate()
print (framerate_AN)
time_AN = np.linspace(start=0, stop=len(ondaconvertidaAN)/framerate_AN, num=len(ondaconvertidaAN))
print(time_AN[:10])

plt.title('Good morning vs Good slime')

plt.xlabel('Tiempo (segundos')
plt.ylabel('Amplitud')

plt.plot(time_gm, ondaconvertidaGM, label='steve')
plt.plot(time_AN, ondaconvertidaAN, label='slime', alpha=0.5)

plt.legend()
plt.show()