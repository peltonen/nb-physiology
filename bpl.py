"""
Tools for analyzing electrophysiologial data acquired in Ephus.

"""


def summarizeXSGs(xsgs):
  IVTepochs = {0 : 'approachCell',
          1 : 'electrical stimulation',
          2 : 'stroke grid',
          3 : 'ChR Light stimulation',
          4 : 'indent',
          5 : 'strainForce',
          6 : 'air puff grid',
          7 : 'indentGrid',
          8 : 'blank',
          9 : 'also blank'}
  for eps in IVTepochs.keys():
    trialsInEpoch = filter(lambda x: x['epoch'] == eps, xsgs)
    numInEpoch = len(trialsInEpoch)
    acqNums = [int(x['acquisitionNumber']) for x in trialsInEpoch]
    if numInEpoch > 0:
      print numInEpoch, IVTepochs[eps]
      print acqNums 
  return    





