import numpy as np
import random
import matplotlib.pyplot as plt
# code  with
MyData = np.random.normal(loc= 300.0, size=1000)
print(np.mean(MyData))

sample_mean = []
for i in range(50):
  y = random.sample(MyData.tolist(), 4)
  avg = np.mean(y)
  sample_mean.append(avg)
  plt.hist(sample_mean)
  plt.show()

print(np.mean(sample_mean))


sample_mean.sort()
print('Lower 95 Confidence Level Cutoff : ',sample_mean[24])
print('up 95 Confidence Level Cutoff : ',sample_mean[747])
print ('mdeian Mean: ',sample_mean[499])
