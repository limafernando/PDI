import scipy.io.wavfile
import pydub
from pydub.playback import play
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack

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
	
	

def main():
	
	#Lê o arquivo wav: rate é a taxa de amostragem do áudio e audioData são os dados do áudio
	rate, audioData = scipy.io.wavfile.read("audio.wav")
	
	
	print("Rate: ", rate)
	print("Dados do audio: ", audioData)
	print("Tamanho: ", len(audioData))
	
	#Calcula uma variável tempo para utilizar no gráfico
	tempo = np.arange(0, float(len(audioData)), 1) / rate
	
	"""
	#Plota o gráfico
	plt.figure(1)
	plt.plot(tempo, audioData, linewidth=0.1, alpha=1,color='blue')
	plt.xlabel('Tempo (s)')
	plt.ylabel('Amplitude')
	plt.show()
	"""
	
	dct = fftpack.dct(audioData, norm = 'ortho') #Calcula a dct dos dados do áudio
	
	dctFiltrada = questao1(50, dct)
	#dctFiltrada = passaBaixa(dct)
	
	
	#Plota o gráfico
	plt.figure(1)
	plt.subplot(211)
	plt.plot(tempo, dct, linewidth=0.1, alpha=1.0, color='blue')
	plt.xlabel('Tempo (s)')
	plt.ylabel('Frequencia')
	plt.subplot(212)
	plt.plot(tempo, dctFiltrada, linewidth=0.1, alpha=1.0, color='blue')
	plt.xlabel('Tempo (s)')
	plt.ylabel('Frequencia')
	plt.show()
	
	
	novoAudio = fftpack.idct(dctFiltrada, norm = 'ortho')
	
	scipy.io.wavfile.write("audio1.wav", rate, novoAudio)
	
	#Lê o arquivo wav
	#wav = pydub.AudioSegment.from_wav("audio.wav")
	
	#Toca a música
	#play(wav)
	
main()