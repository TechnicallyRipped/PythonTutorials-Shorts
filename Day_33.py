
import matplotlib.pyplot as plt 


date_ = ['1-1-2020', '1-1-2021','1-1-2022']
books_read1 = [4, 10, 8]
books_read2 = [9, 2, 11]
books_read3 = [1, 14, 3]

plt.plot(date_, books_read1, color='blue')
plt.plot(date_,books_read2, color='red')
plt.plot(date_,books_read3, color='green')
plt.xlabel('Date')
plt.ylabel('Books Read Per Year')
plt.title('My Chart')
plt.grid(True)
plt.show()
