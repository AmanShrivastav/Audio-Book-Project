#import packages
import pyttsx3
import PyPDF2

book = open('Introduction_to_Machine_Learning.pdf', 'rb')       #read PDF
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages                                       #read pages in PDF
#print(pages)                                                    #no of pages in PDF
speaker = pyttsx3.init()                                         #create speaker
#page = pdfReader.getPage(9)                                     #read single page

for num in range(8, pages):                                      #read certain range of pdf
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)

    speaker.runAndWait()


