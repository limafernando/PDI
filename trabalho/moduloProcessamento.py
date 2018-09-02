from PIL import Image
import numpy as np

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def leImagem(nomeArquivo):

	#Função para ler a imagem
	#A função open abre o arquivo só em mode de leitura
	#Para manipular será preciso fazer uma cópia da imagem

	return Image.open(nomeArquivo)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def imagemToArray(imagem):
	#Função para ter acesso ao array da imagem
	return np.asarray(imagem)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def arrayToImagem(array):
	#Função para converter o array para imagem
	return Image.fromarray(array, mode='RGB')


def exibeImagem(imagem):
	#Função para exibir imagem
	imagem.show()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def salvaImagem(nomeArquivo, imagem):
	'''aux = nomeArquivo.split('.')
	tipoArquivo = aux[1]
	imagem.save(nomeArquivo, tipoArquivo)
	imagem.save(nomeArquivo, tipoArquivo)'''
	
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def RGBtoYIQ(imagemRGB, largura, altura):
	#Função que converte imagens do padrão RGB para o padrão YIQ
	
	imagemYIQ = imagemRGB.astype(float)
	
	for i in range(altura):
		for j in range(largura):
			imagemYIQ[i][j][0] = 0.299*imagemRGB[i][j][0] + 0.587*imagemRGB[i][j][1] + 0.114*imagemRGB[i][j][2]
			imagemYIQ[i][j][1] = 0.596*imagemRGB[i][j][0] - 0.274*imagemRGB[i][j][1] - 0.322*imagemRGB[i][j][2]
			imagemYIQ[i][j][2] = 0.211*imagemRGB[i][j][0] - 0.523*imagemRGB[i][j][1] + 0.312*imagemRGB[i][j][2]
	
	return imagemYIQ

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def YIQtoRGB():
	pass

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def bandaIndividual():
	pass

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def negativo():
	pass

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def controleDeBrilho():
	pass

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def convolucao():
	pass

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def filtroMediana():
	pass

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def limiarizacao():
	pass