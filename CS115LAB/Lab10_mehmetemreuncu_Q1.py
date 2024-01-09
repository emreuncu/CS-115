import matplotlib.pyplot as plt
import numpy as np

in_height = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70])
bo_height = np.array([22, 26, 29, 34, 38, 40, 45, 50, 52])

plt.figure('Question 1')
plt.clf()
plt.plot(in_height, bo_height, 'b.')
plt.xlabel('Initial Height')
plt.ylabel('Bounce Height')
plt.title('Initial Height vs Bounce Height')

fit = np.polyfit(in_height, bo_height, 1)
predicted_dis = np.polyval(fit, in_height)
plt.plot(in_height, predicted_dis, 'r')
plt.show()
