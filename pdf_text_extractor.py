import PyPDF2

def extract_text(pdf_file):
    pdf = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in range(len(pdf.pages)): 
        text += pdf.pages[page].extract_text()
    return(text)

if __name__ == '__main__':
    text = extract_text("/Users/sanjana/Downloads/Sanjana Devarajan Resume (1).pdf")
    print(text)
    