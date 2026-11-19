import matplotlib.pyplot as plt

students = ['Amit','Ravi','Neha','Priya','Sahil']
marks = [85, 90, 78, 92, 88]

plt.subplot(1,2, 1)
plt.plot(students, marks, marker='o')
plt.title('Line Plot')
plt.subplot(1,2, 2)
plt.bar(students, marks)
plt.title('Bar Plot')
plt.tight_layout()
plt.savefig('line_and_bar_plot.png', dpi=300, bbox_inches='tight')
plt.show()