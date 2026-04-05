import matplotlib.pyplot as plt

sizes = [40, 25, 20, 15]
labels = ['python', 'java', 'golang', 'c']
        
plt.pie(sizes, labels=labels,autopct='%1.1f%%', startangle=90)
plt.titile("Fruite Distribution")
plt.show()
