import scipy.io.wavfile
import pydub
from pydub.playback import play
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
from PIL import Image

def passaBaixa(dct):

	dctFiltrada = dct.copy()
	
	for i in range(0, len(dctFiltrada)):
		if abs(dctFiltrada[i]) < 12520:
			dctFiltrada[i] = 0
	
	return dctFiltrada
	
def questao1(n, dct):
	
	dctFiltrada = dct.copy()
	
	listadct = dctFiltrada.tolist() 
	indicesMax = []
	
	for i in range(0, len(listadct)):
		listadct[i] = abs(listadct[i])
		
	aux = listadct.copy()
	
	for i in range(0,n):
		indicesMax.append(listadct.index(max(aux)))
		indiceAux = aux.index(max(aux))
		aux.pop(indiceAux)
	
	for i in range(0, len(dctFiltrada)):
		if i not in indicesMax:
			dctFiltrada[i] = 0
	
	return dctFiltrada
	
def questao2(n):

	imagem = Image.open("lena.bmp")
	imagem.show()
	imagem = np.asarray(imagem)
	print(imagem)
	
	rc = len(imagem)*len(imagem[0]) #linha coluna
	
	print("RC: ", rc)	
	
	dct = fftpack.dct(fftpack.dct(imagem.T, norm = 'ortho').T, norm = 'ortho') #Calcula a dct dos dados do áudio
	
	"""
	im = Image.fromarray(dct)
	
	im.show()
	"""
	
	listadct = dct.copy()

	list(listadct)
	
	listadct = listadct.tolist()
	
	aux = listadct.copy()
	indices = []
	
	for i in range(0,n):
		
		maior = max([valor for linha in aux for valor in linha])
		
		x = [x for x in aux if maior in x][0]
		
		linha = listadct.index(x)
		coluna = x.index(maior)
	
		aux[linha][coluna] = -1
		
		indices.append(str(linha)+','+str(coluna))
	
	listadct = dct.copy()
	
	for i in range(0, len(imagem)):
		for j in range(0, len(imagem[0])):
			indice = (str(i)+','+str(j))
			if indice not in indices:
				listadct[i][j] = 0
				
	dctFiltrada = np.asarray(listadct)	
	
	idct = fftpack.idct(fftpack.idct(dctFiltrada.T, norm = 'ortho').T, norm = 'ortho')
	
	im = Image.fromarray(idct)
	
	im.show()
	
	
def questao3(c, dct):

	dctFiltrada = dct.tolist()
	
	if c > 0:
		manter = len(dctFiltrada) - c
		
		lista1 = dctFiltrada[0:manter]
		
		lista2 = [0]*c
		
		dctFiltrada = lista2+lista1
	
	elif(c < 0):
		
		lista1 = dctFiltrada[abs(c):]
		lista2 = [0]*abs(c)
		
		dctFiltrada = lista1+lista2
		
	else:
		pass

		
	dctFiltrada = np.asarray(dctFiltrada)
	
	return dctFiltrada 
	
def main():
	
	#Lê o arquivo wav: rate é a taxa de amostragem do áudio e audioData são os dados do áudio
	rate, audioData = scipy.io.wavfile.read("audio.wav")
	
	questao2(65536)
	
	"""
	print("Rate: ", rate)
	print("Dados do audio: ", audioData)
	print("Tamanho: ", len(audioData))
	"""
	
	#Calcula uma variável tempo para utilizar no gráfico
	tempo = np.arange(0, float(len(audioData)), 1) / rate
	
	"""
	#Plota o gráfico
	plt.figure(1)
	plt.plot(tempo, audioData, linewidth=0.1, alpha=1,color='blue')
	plt.ylabel('Amplitude')
	plt.show()
	"""
	
	dct = fftpack.dct(audioData, norm = 'ortho') #Calcula a dct dos dados do áudio
	
	#dctFiltrada = questao1(50, dct)
	#dctFiltrada = passaBaixa(dct)
	#dctFiltrada = questao3(-75204, dct)
	
	
	#Plota o gráfico
	plt.figure(1)
	plt.subplot(211)
	plt.plot(tempo, dct, linewidth=0.1, alpha=1.0, color='blue')
	plt.ylabel('Frequencia')
	plt.subplot(212)
	plt.plot(tempo, dctFiltrada, linewidth=0.1, alpha=1.0, color='blue')
	plt.ylabel('Frequencia')
	plt.show()
	
	
	novoAudio = fftpack.idct(dctFiltrada, norm = 'ortho')
	
	scipy.io.wavfile.write("audio1.wav", rate, novoAudio)
	
	#Lê o arquivo wav
	#wav = pydub.AudioSegment.from_wav("audio.wav")
	
	#Toca a música
	#play(wav)
	
main()