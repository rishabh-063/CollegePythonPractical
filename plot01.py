import matplotlib.pyplot as plt

students = ['Amit','Ravi','Neha','Priya','Sahil']
marks = [45, 90, 58, 32, 88]

plt.plot(students, marks, marker='s', linestyle='--', color='blue', label='Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Student Marks')
plt.ylim(0, 100)
plt.grid(True)
plt.legend()
plt.show()