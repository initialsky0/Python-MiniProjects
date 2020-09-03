import sys
import PyPDF2

PATH = './pdf-processing/miscs/'


def merge_watermark(doc_pdf_path, mark_pdf_path, save_path):
    writter = PyPDF2.PdfFileWriter()
    with open(mark_pdf_path, 'rb') as mark_pdf:
        # can be combined to mark_reader = PyPDF2.PdfFileReader(open(mark_pdf_path, 'rb'))
        mark_reader = PyPDF2.PdfFileReader(mark_pdf)
        mark_page = mark_reader.getPage(0)
        with open(doc_pdf_path, 'rb') as doc_pdf:
            doc_reader = PyPDF2.PdfFileReader(doc_pdf)
            for page in range(doc_reader.numPages):
                doc_page = doc_reader.getPage(page)
                # adding doc_page with watermark to the writter
                # .mergePage does not return a new page obj
                doc_page.mergePage(mark_page)
                writter.addPage(doc_page)
            with open(save_path, 'wb') as product:
                writter.write(product)


def merge_pdf(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(PATH + pdf)
    merger.write(f'{PATH}merged.pdf')

    return 0


def read_pdf():
    with open(f'{PATH}dummy.pdf', 'rb') as pdf:
        # 'rb' is read binary for binary mode
        reader = PyPDF2.PdfFileReader(pdf)
        page = reader.getPage(0)
        # print(reader.numPages)
        rotate_page = page.rotateCounterClockwise(90)
        # write pdf
        writter = PyPDF2.PdfFileWriter()
        writter.addPage(rotate_page)
        with open(f'{PATH}rotate_dummy.pdf', 'wb') as mod_pdf:
            writter.write(mod_pdf)


def main():
    # inputs = sys.argv[1:]
    # read_pdf()
    # merge_pdf(inputs)

    # paths for the pdfs
    doc_pdf = f'{PATH}merged.pdf'
    mark_pdf = f'{PATH}wtr.pdf'
    save_path = f'{PATH}marked.pdf'

    merge_watermark(doc_pdf, mark_pdf, save_path)
    return 0


if __name__ == "__main__":
    main()
