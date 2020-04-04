import numpy as np
import matplotlib.pyplot as plt

np.random.seed(4)
data = np.random.randn(2,4)
fig , axs = plt.subplots(2,2, figsize=(5,5))

axs[0, 0].hist(data[0])
axs[0,1].scatter(data[0], data[1])
axs[1,0].plot(data[0],data[1])
axs[1,1].hist2d(data[0], data[1])


plt.show()


