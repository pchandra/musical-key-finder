#!/usr/local/bin/python3.9

import sys
import scipy.stats
import librosa
from keyfinder import *

file = sys.argv[1]
print(file)
y, sr = librosa.load(file)
onset_env = librosa.onset.onset_strength(y=y, sr=sr)
#simple static tempo
tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

#detect the key
y_harmonic, y_percussive = librosa.effects.hpss(y)
key = Tonal_Fragment(y_harmonic, sr)

#static tempo, uniform dist
prior = scipy.stats.uniform(30, 300)  # uniform over 30-300 BPM
utempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr, prior=prior)

#print evrything
key.print_chroma()
key.print_key()
print("BPM (static): ", tempo)
print("BPM (static uniform): ", utempo)
