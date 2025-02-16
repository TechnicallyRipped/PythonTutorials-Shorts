
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def on_button_clicked(event):
    print("Button clicked!")

x = [1, 2, 3, 4, 5]
y = [4, 2, 3, 6, 1]

plt.plot(x,y)

button_ax = plt.axes([.24, 0.9, 0.2, 0.075]) 
button = Button(button_ax, 'Click Me!')

button.on_clicked(on_button_clicked)

plt.show()









