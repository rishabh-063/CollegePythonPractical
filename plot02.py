import matplotlib.pyplot as plt

students = ['Amit','Ravi','Neha','Priya','Sahil']
marks = [45, 90, 58, 32, 88]

plt.bar(students, marks, color='black', label='Marks',width=0.5)
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Student Marks')
plt.ylim
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('student_marks_bar_plot.png', dpi=300, bbox_inches='tight')
plt.show()