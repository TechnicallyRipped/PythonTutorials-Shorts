


# pip install python-docx
import docx

file = docx.Document("test.docx")

for i, paragraph in enumerate(file.paragraphs):
    print(f'{i} --> {paragraph.text}')

























