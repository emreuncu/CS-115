import matplotlib.pyplot as plt
import numpy as np

student = np.loadtxt('students.txt', skiprows=1)
full = student[student[:, 0] == 1]
half = student[student[:, 0] == 2]
non = student[student[:, 0] == 3]

plt.figure('Question 2')
plt.clf()
# histogram
plt.subplot(2, 2, 1)
plt.hist(half[:, 3], 4)
plt.title('Frequency of Writing Gr. of Half Sc. Students')
plt.xticks([50, 75])

# plot
plt.subplot(2, 2, 2)
plt.plot(half[:, 1], 'm:o')
plt.plot(half[:, 2], 'c-x')
plt.ylabel('Grades')
plt.title('Math vs Reading gr. of Half Sc. Students')
plt.legend(['Math', 'Reading'])

# pie chart
pie_label = 'Full', 'Half', 'None'
nums = [len(full), len(half), len(non)]
plt.subplot(2, 2, 3)
plt.pie(nums, labels=pie_label, explode=(0, 0, 0.12), autopct='%.1f%%')
plt.title('Scholarship Percentages')

# bar
plt.subplot(2, 2, 4)
bar_data = [np.mean(half[:, 2]), np.mean(student[:, 2])]
plt.bar('Half-Sc.', bar_data[0])
plt.bar('All', bar_data[1])
plt.ylabel('Average of Grades')
plt.title('Reading Grades: Half Sc. vs All Students')
plt.show()
