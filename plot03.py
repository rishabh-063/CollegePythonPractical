import matplotlib.pyplot as plt

study_hours = ['1','2','3','4','5','6']
marks = [45, 90, 58, 32, 88, 76]

plt.scatter(study_hours, marks, color='green', label='Marks', marker='o')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.ylim(0, 100)
plt.title('Study Hours vs Marks')
plt.legend()
plt.grid(True)
plt.savefig('study_hours_vs_marks.png',dpi=300, bbox_inches='tight') 
plt.show()
