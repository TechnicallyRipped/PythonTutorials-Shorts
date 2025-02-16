

#pip install PyMuPDF
import fitz

pdf_file = fitz.open('test.pdf')

for page_num in range(pdf_file.page_count):
    page = pdf_file.load_page(page_num)
    
    image_list = page.get_images()

    for index, image in enumerate(image_list):
        xref = image[0]
        base_image = pdf_file.extract_image(xref)
    
        image_file = f"page{page_num}-image{index}.jpg"
        
        with open(image_file, "wb") as img_file:
            img_file.write(base_image["image"])

























































