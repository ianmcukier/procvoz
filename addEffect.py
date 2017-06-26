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

def robotvoice (fileread, filewrite):
    dado,freqsamp = wavimport(fileread)
    dadoChorus = efeitos.chorus(dado, 500, 0, 1, 2, 30, 44100)
    dadoFlanger = efeitos.flanger(dadoChorus, 3000, 0.8, 0.2, 10, 1, 44100)
    return dadoFlanger

def flangervoice (fileread, filewrite):
    dado,freqsamp = wavimport(fileread)
    dadoFlanger = efeitos.flanger(dado, 10, 0.2, 0.8, 10,7, 35000)
    return dadoFlanger

def rndresample (fileread,filewrite, dado):
    """ trocar fileread por filewrite pra escrever em cima"""
    dado,freqsamp = wavimport(fileread)
    newfreq = random.randrange(15, 20, 1)*freqsamp/20
    wavwrite(filewrite, newfreq, dadoFlanger)
    return newfreq

#def speedx(sound_array, factor):
#    """ Multiplies the sound's speed by some `factor` """
#    indices = np.round( np.arange(0, len(sound_array), factor) )
#    indices = indices[indices < len(sound_array)].astype(int)
#    return sound_array[ indices.astype(int) ]

#def stretch(sound_array, f, window_size, h):
#    """ Stretches the sound by a factor `f` """
#
#    phase  = np.zeros(window_size)
#    hanning_window = np.hanning(window_size)
#    result = np.zeros( int(len(sound_array)/f) + window_size)
#
#    for i in np.arange(0, len(sound_array)-(window_size+h), h*f):
#
#        # two potentially overlapping subarrays
#        a1 = sound_array[int(i):int(i + window_size)]
#        a2 = sound_array[int(i) + int(h): int(i + window_size + h)]
#
#        # resynchronize the second array on the first
#        s1 =  np.fft.fft(hanning_window[1] * a1)
#        s2 =  np.fft.fft(hanning_window[1] * a2)
#        angle = np.angle(s2/s1)
#        phase = (phase[0] + angle[0]) % 2*np.pi
#        a2_rephased = np.fft.ifft(np.abs(s2)*np.exp(1j*phase))
#
        # add to result
 #       i2 = int(i/f)
 #       result[i2 : i2 + window_size] += hanning_window[1]*a2_rephased

  #  result = ((2**(16-4)) * result/result.max()) # normalize (16bit)

   # return result.astype('int16')

#def pitchshift(snd_array, n, window_size=2**13, h=2**11):
 #   """ Changes the pitch of a sound by ``n`` semitones. """
  #  factor = 2**(1.0 * n / 12.0)
   # stretched = stretch(snd_array, 1.0/factor, window_size, h)
    #return speedx(stretched[window_size:], factor)


