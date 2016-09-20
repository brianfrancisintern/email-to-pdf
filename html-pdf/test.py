import pdfkit
from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch


pdfmetrics.registerFont(TTFont('RealTextOffc-Bold', 'fonts/RealTextOffc/RealTextOffc-Bold.ttf'))
packet = StringIO.StringIO()
# create a new PDF with Reportlab
options = {
    'page-size': 'Letter',
    'margin-left': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-top': '0mm'
}
pdfkit.from_file('index.html', 'test/test4.pdf', options = options)
can = canvas.Canvas(packet, pagesize=letter)
can.setFont('RealTextOffc-Bold', 15)
can.translate(inch,inch)
can.drawString(1.8*inch, 2.700*inch, "LMAU343A")
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file("test/test4.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = file("test/replace4.pdf", "wb")
output.write(outputStream)
outputStream.close()

# from pyPdf import PdfFileWriter, PdfFileReader
# import StringIO
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# def hello(c):
#     from reportlab.lib.units import inch
#     # move the origin up and to the left
#     c.translate(inch,inch)
#     # define a large font
#     c.setFont("Helvetica", 14)
#     # choose some colors
#     c.setStrokeColorRGB(0.2,0.5,0.3)
#     c.setFillColorRGB(1,0,1)
#
#     # change color
#     c.setFillColorRGB(0,0,0.77)
#     # say hello (note after rotate the y coord needs to be negative!)
#     c.drawString(2.3125*inch, 3.1089*inch, "Code")
# code = StringIO.StringIO()
# c = canvas.Canvas(code, pagesize=letter)
# hello(c)
# #move to the beginning of the StringIO buffer
# code.seek(0)
# new_pdf = PdfFileReader(code)
# # read your existing PDF
# existing_pdf = PdfFileReader(file("test/test4.pdf", "rb"))
# output = PdfFileWriter()
# # add the "watermark" (which is the new pdf) on the existing page
# page = existing_pdf.getPage(0)
# page.mergePage(new_pdf.getPage(0))
# output.addPage(page)
# # finally, write "output" to a real file
# outputStream = file("replacetest1.pdf", "wb")
# output.write(outputStream)
# outputStream.close()


#c.showPage()
#c.save()
