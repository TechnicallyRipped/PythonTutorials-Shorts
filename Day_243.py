




import matplotlib.pyplot as plt
from docx import Document

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.savefig('chart_image.png')

doc = Document()
doc.add_picture('chart_image.png')
doc.save('word_document_with_chart.docx')
























