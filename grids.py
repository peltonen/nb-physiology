"""

Computes responses to tactile stimuli along a grid, including indentation, stroke, and air puff


"""

"""


"""
import nbphys as nbp
import stgtracker as stgtrk


def function puffGrid(rows, cols, xsgs):
  #TODO:  check that the stage moved
  stgIter = stgtrk.stageIter(rows,cols)
  gridX = []
  gridY = []
  for x in xsgs[startTrace:(startTrace + rows * cols)]:
    spikes = nbp.trace2spikes(x['ephys']['chan0'], 200)
    pos = stgIter.next()
    #print pos
    for s in spikes:
      if s > 0:
        gridX.append(pos[1])
        gridY.append(pos[0])
  return(gridX, gridY)