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
	
	#RGB YIQ
	"""
	b = mp.RGBtoYIQ(a, largura, altura)
	c = mp.YIQtoRGB(b, largura, altura, a)
	print(np.array_equal(a,b))
	
	imagem2 = mp.arrayToImagem(c)
	mp.exibeImagem(imagem2)
	"""
	
	#Monocromatica
	arrayMono = mp.monocromatica(a, largura, altura)
	imagemMono = mp.arrayToImagem(arrayMono)
	mp.exibeImagem(imagemMono)
	
	
	


	

if __name__ == '__main__':
	main()