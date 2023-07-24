from pdf2image import convert_from_path

pdf_images = convert_from_path('my_pdf.pdf')

for idx in range(len(pdf_images)):
    pdf_images[idx].save('pdf_page_'+ str(idx+1) +'.png', 'PNG')
print("Successfully converted PDF to images")