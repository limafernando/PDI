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
	
	altura = len(a)
	largura = len(a[0])
	
	"""
	Teste RGB para YIQ
	
	b = a.copy()
	pixel = b[0][0]
	pixel[0] = 0
	pixel[1] = 100
	pixel[2] = 0
	
	mp.RGBtoYIQ(b, largura, altura)
	"""
	
	#mp.RGBtoYIQ(a, largura, altura)

	"""
	b = a.copy()
	pixel = b[0][0]
	pixel[0] = 254
	pixel[1] = 0
	pixel[2] = 0
	imagemManipulada = mp.arrayToImagem(b)
	mp.exibeImagem(imagemManipulada)
	"""
	#banda individual
	b = a.copy()
	b = mp.bandaIndividual(b, largura, altura, 'b')
	imagemManipulada = mp.arrayToImagem(b)
	mp.exibeImagem(imagemManipulada)
	

if __name__ == '__main__':
	main()