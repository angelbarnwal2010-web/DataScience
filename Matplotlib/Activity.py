import matplotlib.pyplot as plt
days=['Mon','Tue','Wed','Thu','Fri']
scores=[70,85,60,90,75]
plt.show()
plt.plot(days,scores)
plt.title('My Quiz score tracker')
plt.xlabel('Days of the week')
plt.ylabel('Score')
plt.grid(True)

plt.ylim(0,100)
plt.show()
plt.plot(days,scores,color='blue',linestyle='dashed',marker='o',linewidth=2)
plt.title('My Quiz score tracker')
plt.xlabel('Days of the week')
plt.ylabel('Score')
plt.grid(True)

plt.ylim(0,100)
plt.show()
plt.bar(days, scores, color='orange')
plt.title('My Quiz Score Bar Chart')
plt.xlabel('Days of the week')
plt.ylabel('Score')
plt.ylim(0,100)
plt.show()

