from PyPDF2 import PdfFileReader

def Extract_Pdf(filename):
    fp = open(filename,'rb')
    pdfFile = PdfFileReader(fp)
    data=""
    for pageNum in range(pdfFile.getNumPages()):
        currentPage = pdfFile.getPage(pageNum)
        try:
            data += currentPage.extractText()
        except:
            continue
    fp.close()
    return data
