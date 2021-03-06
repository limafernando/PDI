from PIL import Image
import numpy as np
import math

global media 
media = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
#media = np.array([[1/49,1/49,1/49,1/49,1/49,1/49,1/49],[1/49,1/49,1/49,1/49,1/49,1/49,1/49],[1/49,1/49,1/49,1/49,1/49,1/49,1/49],[1/49,1/49,1/49,1/49,1/49,1/49,1/49],[1/49,1/49,1/49,1/49,1/49,1/49,1/49],[1/49,1/49,1/49,1/49,1/49,1/49,1/49],[1/49,1/49,1/49,1/49,1/49,1/49,1/49]])
#media = np.array([[1/21,1/21,1/21],[1/21,1/21,1/21],[1/21,1/21,1/21],[1/21,1/21,1/21],[1/21,1/21,1/21],[1/21,1/21,1/21],[1/21,1/21,1/21]])

global sobelVertical
sobelVertical = np.array([[1,2,1],[0,0,0],[-1,-2,-1]]) #Detecta bordas horizontais
global sobelHorizontal
sobelHorizontal = np.array([[1,0,-1], [2,0,-2], [1,0,-1]])#Detecta bordas verticais 

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
	#return Image.fromarray(array, mode='RGB')

	im = Image.fromarray(array, mode='RGB')
	
	return im


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

	
##########################################################################################
def RGBtoYIQ(imagemRGB, largura, altura):
	#Função que converte imagens do padrão RGB para o padrão YIQ
	
	imagemYIQ = imagemRGB.copy()
	imagemYIQ = imagemYIQ.astype(float)
	
	for i in range(altura):
		for j in range(largura):
			imagemYIQ[i][j][0] = 0.299*imagemRGB[i][j][0] + 0.587*imagemRGB[i][j][1] + 0.114*imagemRGB[i][j][2]
			imagemYIQ[i][j][1] = 0.596*imagemRGB[i][j][0] - 0.274*imagemRGB[i][j][1] - 0.322*imagemRGB[i][j][2]
			imagemYIQ[i][j][2] = 0.211*imagemRGB[i][j][0] - 0.523*imagemRGB[i][j][1] + 0.312*imagemRGB[i][j][2]
	
	return imagemYIQ


##########################################################################################
def YIQtoRGB(imagemYIQ, largura, altura):			
	
	imagemRGB = imagemYIQ.astype(int)
	
	
	for i in range(altura):
		for j in range(largura):
			
			valor = int(1.000*imagemYIQ[i][j][0] + 0.956*imagemYIQ[i][j][1] + 0.621*imagemYIQ[i][j][2])
			if valor > 255:
				imagemRGB[i][j][0] = 255
			elif valor < 0:
				imagemRGB[i][j][0] = 0
			else:
				imagemRGB[i][j][0] = valor
				
			valor = int(1.000*imagemYIQ[i][j][0] - 0.272*imagemYIQ[i][j][1] - 0.647*imagemYIQ[i][j][2])
			
			if valor > 255:
				imagemRGB[i][j][1] = 255
			elif valor < 0:
				imagemRGB[i][j][1] = 0
			else:
				imagemRGB[i][j][1] = valor
				
			valor = int(1.000*imagemYIQ[i][j][0] - 1.106*imagemYIQ[i][j][1] + 1.703*imagemYIQ[i][j][2])
				
			if valor > 255:
				imagemRGB[i][j][2] = 255
			elif valor < 0:
				imagemRGB[i][j][2] = 0
			else:
				imagemRGB[i][j][2] = valor

	imagemRGB = np.uint8(imagemRGB)
	#print("Tipo" ,imagemRGB.dtype)
	
	return imagemRGB
	

##########################################################################################
def bandaIndividual(arrayDaImagem, largura, altura, banda):
	arrayDaImagem = arrayDaImagem.copy()
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
def monocromatica(imagem, largura, altura, banda):
	
	imagemMonocromatica = imagem.copy()
	
	if banda is 'r' or banda is 'R':
		for i in range(altura):
			for j in range(largura):
				imagemMonocromatica[i][j][1] = imagem[i][j][0]
				imagemMonocromatica[i][j][2] = imagem[i][j][0]
				
		return imagemMonocromatica
		
	elif banda is 'g' or banda is 'G':
		for i in range(altura):
			for j in range(largura):
				imagemMonocromatica[i][j][0] = imagem[i][j][1]
				imagemMonocromatica[i][j][2] = imagem[i][j][1]
				
		return imagemMonocromatica

	elif banda is 'b' or banda is 'B':
		for i in range(altura):
			for j in range(largura):
				imagemMonocromatica[i][j][0] = imagem[i][j][2]
				imagemMonocromatica[i][j][1] = imagem[i][j][2]
				
		return imagemMonocromatica
	
	else:
		return imagemMonocromatica

##########################################################################################

def negativoRGB(imagem, largura, altura):
	
	imagemNegativa = imagem.copy()
	
	for i in range(altura):
		for j in range(largura):
		
			imagemNegativa[i][j][0] = 255 - imagem[i][j][0]
			imagemNegativa[i][j][1] = 255 - imagem[i][j][1]
			imagemNegativa[i][j][2] = 255 - imagem[i][j][2]
	
	return imagemNegativa
	
##########################################################################################
def negativoYIQ(imagem, largura, altura):
	
	imagemNegativa = imagem.copy()
	
	for i in range(altura):
		for j in range(largura):
			imagemNegativa[i][j][0] = 255 - imagem[i][j][0]
	
	return imagemNegativa

##########################################################################################
def controleDeBrilhoAditivoRGB(imagem, largura, altura, c):

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
def controleDeBrilhoAditivoYIQ(imagem, largura, altura, c):

	imagemResultante = imagem.copy()

	if type(c) != int:
		c = int(c)

	#a biblioteca pil percorre de maneira circular
	#255+1 = 0
	for i in range(altura):
		for j in range(largura):
			#somando em Y
			valor = imagemResultante[i][j][0].copy()
			limite = valor + c
			
			if limite > 255:
				imagemResultante[i][j][0] = 255
			elif limite < 0:
				imagemResultante[i][j][0] = 0
			else:
				imagemResultante[i][j][0] += c

	return imagemResultante

##########################################################################################
def controleDeBrilhoMultiplicativoRGB(imagem, largura, altura, c):
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

	
	return imagemResultante
	
##########################################################################################
def controleDeBrilhoMultiplicativoYIQ(imagem, largura, altura, c):

	imagemResultante = imagem.copy()
	
	if c < 0:
		return YIQtoRGB(imagemResultante, largura, altura) #Se o c for inválido, será retornado a imagem resultante só que convertida em RGB para a exibição

	for i in range(altura):
		for j in range(largura):
		
			#multiplicando em Y
			
			valor = imagemResultante[i][j][0].copy()
			limite = valor * c
			
			if limite < 255:
				imagemResultante[i][j][0] = limite
			else:
				imagemResultante[i][j][0] = 255
	
	return imagemResultante

##########################################################################################
def convolucaoRGB(imagem, larguraImagem, alturaImagem, mascara):
	
	global media, sobelVertical, sobelHorizontal
	
							
	if mascara == "media":
		mascara = media
							
	elif mascara == "sobelVertical":
		mascara = sobelVertical
		
		
		aux = mascara[0].copy()
		mascara[0] = mascara[2].copy()
		mascara[2] = aux.copy()
		
							
		for i in range(0,len(mascara)):
			aux = mascara[i][0].copy()
			mascara[i][0] = mascara[i][2].copy()
			mascara[i][2] = aux.copy()
	
	elif mascara == "sobelHorizontal":
		mascara = sobelHorizontal

		
		aux = mascara[0].copy()
		mascara[0] = mascara[2].copy()
		mascara[2] = aux.copy()
		
		
		for i in range(0,len(mascara)):
			aux = mascara[i][0].copy()
			mascara[i][0] = mascara[i][2].copy()
			mascara[i][2] = aux.copy()
	
							
	imagemConvolucionada = imagem.copy()
	
	limiteAlturaMascara = math.floor(len(mascara)/2)
	limiteLarguraMascara = math.floor(len(mascara[0])/2)

	sinal = mascara.copy()


	sinal = np.zeros((len(mascara), len(mascara[0]), 3), dtype = int)

	
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
					
					
			imagemConvolucionada[i][j][0] = int(resultadoR)
			imagemConvolucionada[i][j][1] = int(resultadoG)
			imagemConvolucionada[i][j][2] = int(resultadoB)

			resultadoR = 0
			resultadoG = 0
			resultadoB = 0
	
	return imagemConvolucionada
	
##########################################################################################
def convolucaoYIQ(imagem, larguraImagem, alturaImagem, mascara):
	
	global media, sobelVertical, sobelHorizontal
	
							
	if mascara == "media":
		mascara = media
							
	elif mascara == "sobelVertical":
		mascara = sobelVertical
		
		
		aux = mascara[0].copy()
		mascara[0] = mascara[2].copy()
		mascara[2] = aux.copy()
		
							
		for i in range(0,len(mascara)):
			aux = mascara[i][0].copy()
			mascara[i][0] = mascara[i][2].copy()
			mascara[i][2] = aux.copy()
	
	elif mascara == "sobelHorizontal":
		mascara = sobelHorizontal

		
		aux = mascara[0].copy()
		mascara[0] = mascara[2].copy()
		mascara[2] = aux.copy()
		
		
		for i in range(0,len(mascara)):
			aux = mascara[i][0].copy()
			mascara[i][0] = mascara[i][2].copy()
			mascara[i][2] = aux.copy()
	
							
	imagemConvolucionada = imagem.copy()
	
	limiteAlturaMascara = math.floor(len(mascara)/2)
	limiteLarguraMascara = math.floor(len(mascara[0])/2)

	sinal = mascara.copy()


	sinal = np.zeros((len(mascara), len(mascara[0]), 3), dtype = int)

	
	resultadoY = 0

	
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
					resultadoY += sinal[m][n][0] * mascara[m][n]

					
					
			imagemConvolucionada[i][j][0] = int(resultadoY)

			resultadoY = 0
	
	return imagemConvolucionada

##########################################################################################
def filtroMedianaRGB(imagem, larguraImagem, alturaImagem, m, n):
	
	imagemFiltrada = imagem.copy()
	
	limiteAltura = math.floor(m/2)
	limiteLargura = math.floor(n/2)
	
	sinalR = np.zeros((m, n), dtype = int)
	sinalG = np.zeros((m, n), dtype = int)
	sinalB = np.zeros((m, n), dtype = int)
	
	soma = 0
	mediana = 0
	
	for i in range(limiteAltura, alturaImagem - limiteAltura):
		for j in range(limiteLargura, larguraImagem - limiteLargura):
	
			contAltura = limiteAltura
			contLargura = limiteLargura
			
			for k in range(m):
				for l in range(n):
					sinalR[k][l] = imagem[i - contAltura][j - contLargura][0]
					contLargura -= 1
				contAltura -= 1
				contLargura = limiteLargura
				
			sinalOrdenadoR = np.sort(sinalR, axis = None)
			
			if len(sinalOrdenadoR)%2 == 0:
				soma += sinalOrdenadoR[len(sinalOrdenadoR)/2]
				soma += sinalOrdenadoR[(len(sinalOrdenadoR)/2) - 1]
				mediana = int(soma/2)
			else:
				mediana = sinalOrdenadoR[math.floor(len(sinalOrdenadoR)/2)]
	
			imagemFiltrada[i][j][0] = mediana
			
			mediana = 0
			soma = 0
			contAltura = limiteAltura
			contLargura = limiteLargura
			
			for k in range(m):
				for l in range(n):
					sinalG[k][l] = imagem[i - contAltura][j - contLargura][1]
					contLargura -= 1
				contAltura -= 1
				contLargura = limiteLargura
				
			sinalOrdenadoG = np.sort(sinalG, axis = None)
			
			if len(sinalOrdenadoG)%2 == 0:
				soma += sinalOrdenadoG[len(sinalOrdenadoG)/2]
				soma += sinalOrdenadoG[(len(sinalOrdenadoG)/2) - 1]
				mediana = int(soma/2)
			else:
				mediana = sinalOrdenadoG[math.floor(len(sinalOrdenadoG)/2)]
	
			imagemFiltrada[i][j][1] = mediana
		
			mediana = 0
			soma = 0
			contAltura = limiteAltura
			contLargura = limiteLargura
			
			for k in range(m):
				for l in range(n):
					sinalB[k][l] = imagem[i - contAltura][j - contLargura][2]
					contLargura -= 1
				contAltura -= 1
				contLargura = limiteLargura
				
			sinalOrdenadoB = np.sort(sinalB, axis = None)
			
			if len(sinalOrdenadoB)%2 == 0:
				soma += sinalOrdenadoB[len(sinalOrdenadoB)/2]
				soma += sinalOrdenadoB[(len(sinalOrdenadoB)/2) - 1]
				mediana = int(soma/2)
			else:
				mediana = sinalOrdenadoB[math.floor(len(sinalOrdenadoB)/2)]
	
			
			imagemFiltrada[i][j][2] = mediana
			
			
	return imagemFiltrada
	
##########################################################################################
def filtroMedianaYIQ(imagem, larguraImagem, alturaImagem, m, n):
	
	imagemFiltrada = imagem.copy()
	
	limiteAltura = math.floor(m/2)
	limiteLargura = math.floor(n/2)
	
	sinalY = np.zeros((m, n), dtype = int)
	
	soma = 0
	mediana = 0
	
	for i in range(limiteAltura, alturaImagem - limiteAltura):
		for j in range(limiteLargura, larguraImagem - limiteLargura):
	
			contAltura = limiteAltura
			contLargura = limiteLargura
			
			for k in range(m):
				for l in range(n):
					sinalY[k][l] = imagem[i - contAltura][j - contLargura][0]
					contLargura -= 1
				contAltura -= 1
				contLargura = limiteLargura
				
			sinalOrdenadoY = np.sort(sinalY, axis = None)
			
			if len(sinalOrdenadoY)%2 == 0:
				soma += sinalOrdenadoY[len(sinalOrdenadoY)/2]
				soma += sinalOrdenadoY[(len(sinalOrdenadoY)/2) - 1]
				mediana = int(soma/2)
			else:
				mediana = sinalOrdenadoY[math.floor(len(sinalOrdenadoY)/2)]
	
			imagemFiltrada[i][j][0] = mediana
	
	return imagemFiltrada

##########################################################################################
def limiarizacaoRGB(imagem, largura, altura, limiar, banda):
	
	imagemLimiarizada = imagem.copy()
	
	if banda is 'r' or banda is 'R':
		for i in range(altura):
			for j in range(largura):
				if imagemLimiarizada[i][j][0] <= limiar:
					imagemLimiarizada[i][j][0] = 0
					imagemLimiarizada[i][j][1] = 0
					imagemLimiarizada[i][j][2] = 0
				else:
					imagemLimiarizada[i][j][0] = 255
					imagemLimiarizada[i][j][1] = 255
					imagemLimiarizada[i][j][2] = 255
				
		return imagemLimiarizada
	
	elif banda is 'g' or banda is 'G':
		for i in range(altura):
			for j in range(largura):
				if imagemLimiarizada[i][j][1] <= limiar:
					imagemLimiarizada[i][j][0] = 0
					imagemLimiarizada[i][j][1] = 0
					imagemLimiarizada[i][j][2] = 0
				else:
					imagemLimiarizada[i][j][0] = 255
					imagemLimiarizada[i][j][1] = 255
					imagemLimiarizada[i][j][2] = 255

		return imagemLimiarizada
	
	elif banda is 'b' or banda is 'B':
		for i in range(altura):
			for j in range(largura):
				if imagemLimiarizada[i][j][2] <= limiar:
					imagemLimiarizada[i][j][0] = 0
					imagemLimiarizada[i][j][1] = 0
					imagemLimiarizada[i][j][2] = 0
				else:
					imagemLimiarizada[i][j][0] = 255
					imagemLimiarizada[i][j][1] = 255
					imagemLimiarizada[i][j][2] = 255
				
		return imagemLimiarizada
	
	else:
		return imagemLimiarizada
		
##########################################################################################
def limiarizacaoYIQ(imagem, largura, altura, limiar):
	
	imagemLimiarizada = imagem.copy()
	

	for i in range(altura):
		for j in range(largura):
			if imagemLimiarizada[i][j][0] <= limiar:
				imagemLimiarizada[i][j][0] = 0

			else:
				imagemLimiarizada[i][j][0] = 255
				
	return imagemLimiarizada