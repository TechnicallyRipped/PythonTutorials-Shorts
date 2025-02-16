



# pip install python-barcode

import barcode
from barcode.writer import ImageWriter


barcode_id = '123456789012'

code = barcode.get('ean13', barcode_id,
                    writer=ImageWriter())

code.save('example_barcode')

























