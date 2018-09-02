from PIL import Image
import numpy as np

def leImagem(nomeArquivo):
	#Função para ler a imagem
	#A função open abre o arquivo só em mode de leitura
	#Para manipular será preciso fazer uma cópia da imagem
	return Image.open(nomeArquivo)

def imagemToArray(imagem):
	#Função para ter acesso ao array da imagem
	return np.asarray(imagem)

def arrayToImagem(array):
	#Função para converter o array para imagem
	return Image.fromarray(array, mode='RGB')

def exibeImagem(imagem):
	#Função para exibir imagem
	imagem.show()

def salvaImagem(nomeArquivo, imagem):
	'''aux = nomeArquivo.split('.')
	tipoArquivo = aux[1]
	imagem.save(nomeArquivo, tipoArquivo)'''

def RGBtoYIQ():
	pass
def YIQtoRGB():
	pass
def bandaIndividual():
	pass
def negativo():
	pass
def controleDeBrilho():
	pass
def convolucao():
	pass
def filtroMediana():
	pass
def limiarizacao():
	pass