import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np

import moduloProcessamento as mp

def main():
	print('escolha o arquivo')
	
	#<Para selecionar o arquivo por GUI
	Tk().withdraw()
	caminhoArquivo = askopenfilename()
	#caminhoArquivo=os.path.basename(caminhoArquivo) #pega só o nome, mas é importante pegar o caminho
	#Para selecionar o arquivo por GUI>

	imagem = mp.leImagem(caminhoArquivo)
	mp.exibeImagem(imagem)
	a = mp.imagemToArray(imagem)
	
	altura = len(a)
	largura = len(a[0])
	
	#RGB YIQ
	"""
	b = a.copy()
	pixel = b[0][0]
	pixel[0] = 0
	pixel[1] = 0
	pixel[2] = 0
	print(pixel)
	"""
	
	
	b = mp.RGBtoYIQ(a, largura, altura)
	#pixel = b[0][0]
	#print(pixel)
	c = mp.YIQtoRGB(b, largura, altura, a)
	print(a)
	print(c)
	
	
	"""
	for i in range(largura):
		for j in range(altura):
			print(c[i][j])
	"""
	
	#pixel = b[0][0]
	#print(pixel)
	#print(np.array_equal(a,b))
	
	
	#imagem2 = mp.arrayToImagem(mp.YIQtoRGB(mp.RGBtoYIQ(a, largura, altura), largura, altura, a))
	imagem2 = mp.arrayToImagem(c.copy())
	mp.exibeImagem(imagem2)
	#NÃO FAZE SENTIDOOOOOOOO
	
	
	#banda individual
	"""
	b = a.copy()

	b = mp.bandaIndividual(b, largura, altura, 'b')
	imagemManipulada = mp.arrayToImagem(b)
	mp.exibeImagem(imagemManipulada)
	"""
	
	#Monocromatica
	"""
	arrayMono = mp.monocromatica(a, largura, altura, 'r')
	imagemMono = mp.arrayToImagem(arrayMono)

	mp.exibeImagem(imagemMono)
	arrayMono = mp.monocromatica(a, largura, altura, 'g')
	imagemMono = mp.arrayToImagem(arrayMono)

	mp.exibeImagem(imagemMono)
	arrayMono = mp.monocromatica(a, largura, altura, 'b')
	imagemMono = mp.arrayToImagem(arrayMono)

	mp.exibeImagem(imagemMono)
	"""
	
	#Negativo
	"""
	arrayNegativo = mp.negativo(a, largura, altura)
	imagemNegativa = mp.arrayToImagem(arrayNegativo)
	mp.exibeImagem(imagemNegativa)
	mp.salvaImagem(imagemNegativa, caminhoArquivo)
	"""
	
	#Brilhos
	"""
	b = a.copy()
	b = mp.controleDeBrilhoAditivo(a, largura, altura, 50)
	imagemManipulada = mp.arrayToImagem(b)
	mp.exibeImagem(imagemManipulada)
	"""
	
	#Convolução Media
	"""
	arrayConvolucao = mp.convolucao(a, "sobelHorizontal", largura, altura)
	imagemConvolucionada = mp.arrayToImagem(arrayConvolucao)
	mp.exibeImagem(imagemConvolucionada)
	"""
	
	#Filtro Mediana
	"""
	arrayMediana = mp.filtroMediana(a, largura, altura, 3, 3)
	imagemFiltrada = mp.arrayToImagem(arrayMediana)
	mp.exibeImagem(imagemFiltrada)
	"""
	
	#Limiarização
	"""
	arrayLimiarizacao = mp.limiarizacao(a, largura, altura, 100)
	imagemLimiarizada = mp.arrayToImagem(arrayLimiarizacao)
	mp.exibeImagem(imagemLimiarizada)
	"""



if __name__ == '__main__':
	main()