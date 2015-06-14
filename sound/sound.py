import numpy as np
import scikits.audiolab as al
alformat = al.Format('wav')
filename = "hydrogen.wav"
fs = 32000

data = np.zeros(320000)
#data2 = np.zeros(32000)
#data = np.zeros(320000)
t = np.linspace(0, 10, 320000)
for n in range(1, 2, 1):
  print(n)
  #data += np.sin(n * 2 * np.pi * t * 440)
  data += np.sin(1 * 2 * np.pi * t * 440)

#data = np.sin(2 * np.pi * t * 440)
#time = np.linspace(0, 1, 320000)
#i = -1
#print(time.shape)
#for t in time:
  #i+=1
  #for n in range(1,2,1):
    #print(n)
    #data[i] += float(1)  / (float(n)**2) * np.sin(n * 2 * np.pi * t * 440)
    #data[i] += np.sin((1 - (float(1)/(n**2))) * 2 * np.pi * t * 440)


data = np.array([data* np.exp(t), data*np.exp(t) ])
f = al.Sndfile(filename, 'w', alformat, 2, fs)
f.write_frames(data.transpose())
f.close
    
    
