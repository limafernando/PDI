from PIL import Image
import numpy as np
import math

global media 
media = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

##########################################################################################
def leImagem(caminhoArquivo):

	#Função para ler a imagem
	#A função open abre o arquivo só em mode de leitura
	#Para manipular será preciso fazer uma cópia da imagem

	return Image.open(caminhoArquivo)


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
def salvaImagem(imagem, caminhoArquivo):
	aux = caminhoArquivo.split('.')
	caminhoArquivo = aux[0] + 'Modificado.' + aux[1]
	tipoArquivo = aux[1]
	imagem.save(caminhoArquivo, tipoArquivo)
	#imagem.save(caminhoArquivo, tipoArquivo)
	
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


##########################################################################################
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

##########################################################################################

def negativo(imagem, largura, altura):
	
	imagemNegativa = imagem.copy()
	
	for i in range(altura):
		for j in range(largura):
			imagemNegativa[i][j][0] = 255 - imagem[i][j][0]
			imagemNegativa[i][j][1] = 255 - imagem[i][j][1]
			imagemNegativa[i][j][2] = 255 - imagem[i][j][2]
	
	return imagemNegativa

##########################################################################################
def controleDeBrilhoAditivo(imagem, largura, altura, c):
	imagemResultante = imagem.copy()

	if type(c) != int:
		c = int(c)

	#a biblioteca pil percorre de maneira circular
	#255+1 = 0
	for i in range(altura):
		for j in range(largura):
			#somando em R
			valor = imagemResultante[i][j][0].copy()
			limite = valor + c
			if limite > 255:
				imagemResultante[i][j][0] = 255
			elif limite < 0:
				imagemResultante[i][j][0] = 0
			else:
				imagemResultante[i][j][0] += c

			#somando em G
			valor = imagemResultante[i][j][1].copy()
			limite = valor + c
			if limite > 255:
				imagemResultante[i][j][1] = 255
			elif limite < 0:
				imagemResultante[i][j][1] = 0
			else:
				imagemResultante[i][j][1] += c

			#somando em B
			valor = imagemResultante[i][j][2].copy()
			limite = valor + c
			if limite > 255:
				imagemResultante[i][j][2] = 255
			elif limite < 0:
				imagemResultante[i][j][2] = 0
			else:
				imagemResultante[i][j][2] += c

	return imagemResultante

##########################################################################################
def controleDeBrilhoMultiplicativo(imagem, largura, altura, c):
	imagemResultante = imagem.copy()
	
	if c < 0:
		return imagemResultante

	for i in range(altura):
		for j in range(largura):
			#multiplicando em R
			valor = imagemResultante[i][j][0].copy()
			limite = valor * c
			if limite < 255:
				imagemResultante[i][j][0] = limite
			else:
				imagemResultante[i][j][0] = 255

			#multiplicando em G
			valor = imagemResultante[i][j][1].copy()
			limite = valor * c
			if limite < 255:
				imagemResultante[i][j][1] = limite
			else:
				imagemResultante[i][j][1] = 255

			#multiplicando em B
			valor = imagemResultante[i][j][2].copy()
			limite = valor * c
			if limite < 255:
				imagemResultante[i][j][2] = limite
			else:
				imagemResultante[i][j][2] = 255

			
			#print(imagemResultante[i][j])
	
	return imagemResultante
##########################################################################################
def convolucao(imagem, mascara, larguraImagem, alturaImagem):
	
	global media
	
	if mascara == "media":
		mascara = media
	
	
	imagemConvolucionada = imagem.copy()
	
	limiteAlturaMascara = math.floor(len(mascara)/2)
	limiteLarguraMascara = math.floor(len(mascara[0])/2)
	
	sinal = mascara.copy()
	#sinal = np.array([[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])
	
	#sinal = [[],[]]
	
	"""for i in range(len(mascara)):
		for j in range(len(mascara[0])):
			sinal[i][j] = np.append(sinal[i][j], [0,0,0])
	"""
	
	resultadoR = 0
	resultadoG = 0
	resultadoB = 0
	
	for i in range(limiteAlturaMascara, alturaImagem - limiteAlturaMascara):
		for j in range(limiteLarguraMascara, larguraImagem - limiteLarguraMascara):
			
			contAltura = limiteAlturaMascara
			contLargura = limiteLarguraMascara
			
			for m in range(len(mascara)):
				for n in range(len(mascara[0])):
					sinal[m][n] = imagem[i - contAltura][j - contLargura]
					contLargura -= 1
				contAltura -= 1
				contLargura = limiteLarguraMascara
				
			for m in range(len(mascara)):
				for n in range(len(mascara[0])):
					resultadoR += sinal[m][n][0] * mascara[m][n]
					resultadoG += sinal[m][n][1] * mascara[m][n]
					resultadoB += sinal[m][n][2] * mascara[m][n]
					
			imagemConvolucionada[i][j][0] = resultadoR
			imagemConvolucionada[i][j][1] = resultadoG
			imagemConvolucionada[i][j][2] = resultadoB
	
	return imagemConvolucionada

##########################################################################################
def filtroMediana():
	pass

##########################################################################################
def limiarizacao():
	pass