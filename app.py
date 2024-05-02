from flask import Flask,request
from flask_restful import Api, Resource
import fitz

app = Flask(__name__)
api = Api(app)
def count_pages(pdf_path): #นับจำนวนแผ่น
    pdf_document = fitz.open(pdf_path)
    num_pages = pdf_document.page_count
    pdf_document.close()
    return num_pages

def pdf2img(pdffile,countPage): #แปลงไฟล์เป็น img
    doc = fitz.open(pdffile)
    for x in range(countPage): 
        page = doc.load_page(x)  # number of page
        pix = page.get_pixmap()
        output = "./output_images/outfile_"+str(x)+".png"
        pix.save(output)
    doc.close()

class convertpdf2image(Resource):
    def post(self):
        data = request.form
        pdf_path =data['pdf_file']
        num_pages = count_pages(pdf_path)
        pdf2img(pdf_path,num_pages)
        return data['pdf_file']
   
api.add_resource(convertpdf2image, '/convertpdf2image')

if __name__ == '__main__':
    app.run(debug=True)