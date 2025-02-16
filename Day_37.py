


import matplotlib.pyplot as plt

plt.axhline(y=0.5, color='red', 
            linestyle='-', label='Solid line')

plt.axhline(y=1, color='blue', 
            linestyle='--', label='Dashed Line')

plt.axhline(y=1.5, color='green', 
            linestyle='-.', label='Dash-dot Line')

plt.axhline(y=2, color='purple', 
            linestyle=':', label='Dotted Line')

plt.legend()
plt.show()








































