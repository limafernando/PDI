import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np

import moduloProcessamento as mp

def main():
	print('escolha o arquivo')
	
	#<Para selecionar o arquivo por GUI
	Tk().withdraw()
	filename = askopenfilename()
	filename=os.path.basename(filename)
	#Para selecionar o arquivo por GUI>

	imagem = mp.leImagem(filename)
	mp.exibeImagem(imagem)
	a = mp.imagemToArray(imagem)
	b = a.copy()
	pixel = b[0][0]
	pixel[0] = 254
	pixel[1] = 0
	pixel[2] = 0
	imagemManipulada = mp.arrayToImagem(b)
	mp.exibeImagem(imagemManipulada)

if __name__ == '__main__':
	main()