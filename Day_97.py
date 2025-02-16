

import PyPDF2

with open('test.pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        pdf_text = ''

        for page in reader.pages:
            pdf_text += page.extract_text()

print(pdf_text)
























