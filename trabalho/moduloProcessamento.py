from PIL import Image
import numpy as np
import math

##########################################################################################
def leImagem(nomeArquivo):

	#Função para ler a imagem
	#A função open abre o arquivo só em mode de leitura
	#Para manipular será preciso fazer uma cópia da imagem

	return Image.open(nomeArquivo)


##########################################################################################
def imagemToArray(imagem):
	#Função para ter acesso ao array da imagem
	return np.asarray(imagem)


##########################################################################################
def arrayToImagem(array):
	#Função para converter o array para imagem
	return Image.fromarray(array, mode='RGB')

##########################################################################################
def exibeImagem(imagem):
	#Função para exibir imagem
	imagem.show()


##########################################################################################
def salvaImagem(nomeArquivo, imagem):
	'''aux = nomeArquivo.split('.')
	tipoArquivo = aux[1]
	imagem.save(nomeArquivo, tipoArquivo)
	imagem.save(nomeArquivo, tipoArquivo)'''
	
##########################################################################################
def RGBtoYIQ(imagemRGB, largura, altura):
	#Função que converte imagens do padrão RGB para o padrão YIQ
	
	imagemYIQ = imagemRGB.astype(float)
	
	for i in range(altura):
		for j in range(largura):
			imagemYIQ[i][j][0] = 0.299*imagemRGB[i][j][0] + 0.587*imagemRGB[i][j][1] + 0.114*imagemRGB[i][j][2]
			imagemYIQ[i][j][1] = 0.596*imagemRGB[i][j][0] - 0.274*imagemRGB[i][j][1] - 0.322*imagemRGB[i][j][2]
			imagemYIQ[i][j][2] = 0.211*imagemRGB[i][j][0] - 0.523*imagemRGB[i][j][1] + 0.312*imagemRGB[i][j][2]
	
	return imagemYIQ

<<<<<<< HEAD
##########################################################################################
def YIQtoRGB():
	pass

##########################################################################################
def bandaIndividual(arrayDaImagem, largura, altura, banda):
	if banda is 'r' or banda is 'R':
		for i in range(altura):
			for j in range(largura):
				arrayDaImagem[i][j][1] = 0
				arrayDaImagem[i][j][2] = 0
		return arrayDaImagem

	elif banda is 'g' or banda is 'G':
		for i in range(altura):
			for j in range(largura):
				arrayDaImagem[i][j][0] = 0
				arrayDaImagem[i][j][2] = 0
		return arrayDaImagem

	elif banda is 'b' or banda is 'B':
		for i in range(altura):
			for j in range(largura):
				arrayDaImagem[i][j][0] = 0
				arrayDaImagem[i][j][1] = 0
		return arrayDaImagem

	else:
		return arrayDaImagem

##########################################################################################
=======
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def YIQtoRGB(imagemYIQ, largura, altura, a):
	
	imagemRGB = imagemYIQ.astype(float)
	
	for i in range(altura):
		for j in range(largura):
			imagemRGB[i][j][0] = math.ceil(1.000*imagemYIQ[i][j][0] + 0.956*imagemYIQ[i][j][1] + 0.621*imagemYIQ[i][j][2])
			imagemRGB[i][j][1] = math.ceil(1.000*imagemYIQ[i][j][0] - 0.272*imagemYIQ[i][j][1] - 0.647*imagemYIQ[i][j][2])
			imagemRGB[i][j][2] = math.ceil(1.000*imagemYIQ[i][j][0] - 1.106*imagemYIQ[i][j][1] + 1.703*imagemYIQ[i][j][2])
			if imagemRGB[i][j][0] > 255:
				imagemRGB[i][j][0] = 255
			if imagemRGB[i][j][1] > 255:
				imagemRGB[i][j][1] = 255
			if imagemRGB[i][j][2] > 255:
				imagemRGB[i][j][2] = 255
	imagemRGB = imagemRGB.astype(int)
	for i in range(altura):
		for j in range(largura):
			if imagemRGB[i][j][0] != a[i][j][0] or imagemRGB[i][j][1] != a[i][j][1] or imagemRGB[i][j][2] != a[i][j][2]:
					print('rgb:', imagemRGB[i][j], 'imagemoriginal:', a[i][j])
			
	return imagemRGB
	

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def bandaIndividual():
	pass

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def monocromatica(imagem, largura, altura):
	
	imagemMonocromatica = imagem.copy()
	
	for i in range(altura):
		for j in range(largura):
			menor = imagem[i][j][0]
			if imagem[i][j][1] < menor:
				menor = imagem[i][j][1]
			if imagem[i][j][2] < menor:
				menor = imagem[i][j][2]
			
			imagemMonocromatica[i][j][0] = menor
			imagemMonocromatica[i][j][1] = menor
			imagemMonocromatica[i][j][2] = menor
			
	return imagemMonocromatica

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
>>>>>>> 8bcc0074f38ea359578733d41c7908b4d3523391
def negativo():
	pass

##########################################################################################
def controleDeBrilho():
	pass

##########################################################################################
def convolucao():
	pass

##########################################################################################
def filtroMediana():
	pass

##########################################################################################
def limiarizacao():
	pass