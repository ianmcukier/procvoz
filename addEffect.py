import source, efeitos, os
from scipy.io import wavfile
import scipy
import random
import numpy as np

MODELDIR = '/home/ian/Documents/Projetos/ProcVoz/'

def wavimport (filename):
    sampFreq,snd = wavfile.read(os.path.join(MODELDIR, filename))
    return snd, sampFreq

def wavwrite (filename, rate,data):
    wavfile.write(os.path.join(MODELDIR,filename), rate, data)
    return os.path.join(MODELDIR,filename)

def robotvoice (data):
    dadoChorus = efeitos.chorus(dado, 500, 0, 1, 2, 30, 44100)
    dadoFlanger = efeitos.flanger(dadoChorus, 3000, 0.8, 0.2, 10, 1, 44100)
    return dadoFlanger

def flangervoice (data):
    dadoFlanger = efeitos.flanger(dado, 10, 0.2, 0.8, 10,7, 35000)
    return dadoFlanger

def rndresample (filename, data,freqsamp):
    newfreq = random.randrange(15, 30, 1)*freqsamp/20
    newdata = data[:data.size:2]
    wavwrite(filename, int(newfreq), data)
    return int(newfreq)

def reversewav (data):
    reversed_data = data[::-1]
    return reversed_data





