from PIL import Image
import numpy as np

def leImagem(nomeArquivo):
	return Image.open(arquivo)

def imagemToArray(imagem):
	return np.asarray(imagem)

def exibeImagem(imagem):
	imagem.show()

def salvaImagem(nomeArquivo, imagem):
	aux = nomeArquivo.split('.')
	tipoArquivo = aux[1]
	imagem.save(nomeArquivo, tipoArquivo)

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