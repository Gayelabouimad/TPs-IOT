# sphinx_gallery_thumbnail_number = 3
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # an empty figure with no axes
plt.title("first Plat")
fig.suptitle('Variation du temps en fonction du changement de SF')  # Add a title so we know which it is
ax1 = fig.add_subplot()

ax1.set_ylabel('time')
ax1.set_xlabel('SF')



t=[63, 114, 206, 300] # y
SF=[7 ,8 , 9, 10] # x

plt.plot(SF,t)
# plt.legend()

plt.show()
