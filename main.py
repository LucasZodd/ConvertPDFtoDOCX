from pdf2docx import Converter
import os

for _,_, arquivos in os.walk('pdf'):
    for arquivo in arquivos:
        print("arquivo: ", arquivo)

        try:
            novoArquivo = arquivo.split(".")[0]
            cv = Converter(f'pdf/{arquivo}')
            cv.convert(f'precisaConverter/{novoArquivo}'+'.docx', start=0, end=None)
            cv.close()
            print(arquivo)
        except:
            print("Erro arquivo: ", arquivo)
            pass
