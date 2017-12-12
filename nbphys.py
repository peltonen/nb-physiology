"""
A collection of tools for analysis of electrophysiological data that are specific to Ginty lab applications.
These methods mostly wrap tools built by others.

"""

import numpy as np
import traceRoutines as tm
import scipy.signal as signal
import matplotlib as plt

__all__ = ['trace2spikes', 'mergeXSGs', 'parseXSGHeader', 'lpFilter', 'pGrid', 'iGrid']


def trace2spikes(trace, minThresh = 200):
  all_spike_peaks = []
  all_thresholds = []
  all_spike_boundaries = []
  b, a = signal.butter(8, 0.025, 'high')
  hp_trace = signal.filtfilt(b,a,trace, padlen=150)
  hp_thresh = hp_trace.max() * 0.66
  if hp_thresh < minThresh:
    return([-1])
  spike_boundaries = zip(tm.findLevels(hp_trace, hp_thresh, mode='rising')[0], tm.findLevels(hp_trace, hp_thresh, mode='falling')[0])
  spike_peaks = [np.argmax(trace[s[0]:s[1]])+s[0] for s in spike_boundaries]
  return spike_peaks


def pltTS(trace, spikes, Fs):
  t = np.linspace(0, len(trace) / Fs, len(trace))
  plt.plot(trace) 
  plt.vlines(sTimes, hp_trace.max() * 1.1,hp_trace.max() * 1.8)
  return



def iGrid(startIndex, row=28, col=5, intervals=[[0, 10000],[10600, 19000],[19000, 28000],[28000,35900]]):
  iGrid = np.zeros(shape=(row,col, len(intervals)))
  ri, ci = [0,0]
  for x in xsgs[startIndex:(startIndex + row * col)]:
    spikes = nbp.trace2spikes(x['ephys']['chan0'])
    temp = []
    for i in intervals:
      temp.append(len(filter(lambda s: s > i[0] and s < i[1], spikes)))
    iGrid[ri,ci] = temp
    if ri%2 == 0:  #we are traveling right
      if ci == (col-1): # we are at the end of the range, so we should move down      
        ri = ri + 1 
      else:
        ci = ci + 1
    else:  #we are traveling left
      if ci == 0: # we are at the end of the range, so we should move down      
        ri = ri + 1 
      else:
        ci = ci - 1
  return(iGrid)

def pGrid(startIndex, row=28, col=5, intervals=[[0, 10000],[10600, 19000],[19000, 28000],[28000,35900]]):


  return


def hpFilter(trace):
  b, a = signal.butter(8, 0.025, 'high')
  hp_trace = signal.filtfilt(b,a,trace, padlen=150)
  return hp_trace

def lpFilter(trace, Fs, Fcut):
	b, a = signal.bessel(4, Fcut/(Fs * 1.0), 'low')
	lp_trace = signal.filtfilt(b,a,trace, padlen=150)
  	return lp_trace