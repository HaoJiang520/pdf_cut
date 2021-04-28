# -*- Coding: utf-8 -*-
# -*- Author:Jiang Hao -*-
# -*- Time:2021-4-28 -*-

'''
pdf切割
'''

from PyPDF2 import PdfFileWriter, PdfFileReader

def pdf_Fenge(start_page,end_page,source_file_path,out_file_path):
    # 开始页
    start_page = start_page  #int

    # 截止页
    end_page = end_page  #int

    source_file_path = source_file_path

    out_file_path = out_file_path

    output = PdfFileWriter()
    pdf_file = PdfFileReader(open(source_file_path, "rb"))

    # 保存input.pdf中的start_page至end_page页到output.pdf
    for i in range(start_page, end_page):
        output.addPage(pdf_file.getPage(i))

    outputStream = open(out_file_path, "wb")
    output.write(outputStream)
    outputStream.close()

if __name__ == "__main__":
    start_page = 0
    end_page = 100
    source_file_path = ""   #自己添加源文件路径
    out_file_path = ""  #自己添加导出文件路径
    pdf_Fenge(start_page=start_page,end_page=end_page,source_file_path=source_file_path,out_file_path=source_file_path)
