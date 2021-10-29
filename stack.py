import matplotlib.pyplot as plt

days = [1,2,3,4,5]

age =[72,82,61,11,27]

weight =[17,28,72,52,32]

plt.plot([],[],color='y', label='age', linewidth=5)

plt.plot([],[],color='r', label='weight', linewidth=5)

plt.stackplot(days,age,weight,colors=['y','r'])

plt.xlabel('x')

plt.ylabel('y')

plt.title('Area Plot')

plt.legend()

plt.show()
